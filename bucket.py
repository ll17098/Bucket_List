from operator import countOf
from platform import node
from re import I, L
import sqlite3
from bottle import route, run, debug, error
from bottle import template, request, redirect, view




#connects to databsse
conn = sqlite3.connect("mydatabase.db")


#landing page / login page
@route("/")
@view("templates/login")
def login():
    pass

 #register page   
@route("/reg")
def register():
    return template("templates/reg.html")

#register page
@route("/Home")
def index():
    return template("templates/index.html", uname=uname)


@route("/login_validation", method="POST")
def checklogin():
    global uname
    uname = request.forms["username"]
    pword = request.forms["password"]
    c = conn.cursor()
    c.execute("SELECT * FROM userInfo WHERE username = '{}' AND password = '{}'".format(uname, pword))
    result = c.fetchone()
    if result:
        return redirect("/Home")

    else:
        msg = "Inccorect Username / Password"
        return template("templates/errorlogin.html", msg=msg)

#Records users new log in details into sql
@route("/reg_validation", method="POST")
def checkRegister():
    global uname
    uname = request.forms["username"]
    pword = request.forms["password"]
    pword2 = request.forms["password2"]
    
    

    c = conn.cursor()
    c.execute("SELECT * FROM userInfo WHERE username = '{}'".format(uname))
    result = c.fetchone()

    if result:
        msg1 = "Username Already Exsists"
        return template("templates/errorreg.html", msg=msg1)

    if pword2 != pword:
        msg2 = "Password does not match bro"
        return template("templates/errorreg.html", msg=msg2)
        

    else:
        c = conn.cursor()
        c.execute("INSERT INTO userInfo (username,password) VALUES (?,?)", (uname,pword))
        c.execute("CREATE TABLE IF NOT EXISTS '{}' (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)".format(uname))
        c.execute("INSERT INTO '{}'(task, status) VALUES('Add Your New Milestone ', 'Incomplete')".format(uname))
        c.execute("INSERT INTO '{}'(task, status) VALUES('Add Your New Milestone ', 'Complete')".format(uname))
        conn.commit()
        return redirect("/Home")

#Displays user"s incompletedbucket list 
@route("/bucket", method="GET")
def bucket_list():
    while True:
        try:
            c = conn.cursor()
            c.execute("SELECT id, task FROM '{}' WHERE status = '{}'".format(uname, "Incomplete"))
            result = c.fetchall()

            noRows = c.execute("SELECT COUNT(*) FROM '{}'".format(uname))
            result2 = noRows.fetchone()
            for amt in result2:
                numTotal = amt

            noRows2 = c.execute("SELECT COUNT(*) FROM '{}' WHERE status LIKE '{}'".format(uname, "Incomplete"))
            result3 = noRows2.fetchone()
            for i in result3:
                numInc = i

            c.close()
            return template("templates/make_table", rows=result, num1=numTotal, num2=numInc)

        except NameError:
             return redirect("/")
    

#displays user's complete bucket list
@route("/doneBucket", method="GET")
def bucket_list2():
    while True:
        try:
            c = conn.cursor()
            c.execute("SELECT id, task FROM '{}' WHERE status = '{}'".format(uname, "Complete"))
            result = c.fetchall()

            noRows = c.execute("SELECT COUNT(*) FROM '{}'".format(uname))
            result2 = noRows.fetchone()
            for amt in result2:
                numTotal = amt

            noRows2 = c.execute("SELECT COUNT(*) FROM '{}' WHERE status LIKE '{}'".format(uname, "Complete"))
            result3 = noRows2.fetchone()
            for i in result3:
                numInc = i
            c.close()
            return template("templates/make_table2", rows=result, num1=numTotal, num2=numInc)
        
        except NameError:
            return redirect("/")




#Add a new task to the list
@route("/new", method="GET")
def new_item():
    #when save is clicked, it will count rows in users table
    if request.GET.save:
        c = conn.cursor()
        num_id = c.execute("SELECT COUNT(*) from '{}'".format(uname))
        result_id = num_id.fetchone()

        for i in result_id:
            result = i
            
            #limit of rows
            if result < 15:
                new = request.GET.task.strip()
                c = conn.cursor()
                c.execute("INSERT INTO '{}' (task,status) VALUES ('{}','{}')".format(uname,new, "Incomplete"))
                conn.commit()
                return redirect("/bucket")

            else:
                msg = ("Sorry {}, there is a milestone limit.".format(uname))
                return template("templates/erroradd.html", msg=msg)

#edits current task
@route("/edit/<no:int>", method="GET")
def edit_item(no):

    while True:
        try:
            edit = request.GET.task.strip()
            status = request.GET.status.strip()

            #update table or update the task and status of it
            if request.GET.save:
                if status == "Complete":
                    status = "Complete"
                else:
                    status = "Incomplete"
                    
                c = conn.cursor()
                c.execute("UPDATE '{}' SET task = '{}', status = '{}' WHERE id LIKE '{}'".format(uname, edit, status, no))
                conn.commit()
                return redirect("/bucket")

            #deletes task
            elif request.GET.delete:
                c = conn.cursor()
                c.execute("DELETE FROM '{}' WHERE task = '{}' AND id = '{}'".format(uname, edit, no))
                conn.commit()
                return redirect("/bucket")

            #shows task by selecting the task where the id equals that task
            else:
                c = conn.cursor()
                c.execute("SELECT task FROM '{}' WHERE id LIKE '{}'".format(uname,str(no)))
                cur_data = c.fetchone()
                return template("templates/edit_task", old=cur_data, no=no)

        except NameError:
            return redirect("/")


#catach an error
@error(404)
def mistake404(code):
    return "Sorry, this page does not exist!"


debug(True)
run(reloader=True)