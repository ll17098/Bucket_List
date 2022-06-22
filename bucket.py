from operator import countOf
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

@route("/login_validation", method="POST")
def checklogin():
    global uname2
    uname2 = request.forms["username"]
    pword2 = request.forms["password"]
    c = conn.cursor()
    c.execute("SELECT * FROM userInfo WHERE username = '{}' AND password = '{}'".format(uname2, pword2))
    result = c.fetchone()
    if result:
        return redirect("/bucket")

    else:
        return "Incorrect Username / Password<br><button type='submit'><a href='/'>LOGIN AGAIN</a></button>"

#Records users new log in details into sql
@route("/reg_validation", method="POST")
def checkRegister():
    global uname2
    uname2 = request.forms["username"]
    pword2 = request.forms["password"]
    c = conn.cursor()
    c.execute("SELECT * FROM userInfo WHERE username = '{}'".format(uname2))
 
    result = c.fetchone()

    if result:
        return "username already exists<br><button type='submit'><a href='/reg'>REGISTER AGAIN</a></button>"

    else:
        c = conn.cursor()
        c.execute("INSERT INTO userInfo (username,password) VALUES (?,?)", (uname2,pword2))
        c.execute("CREATE TABLE IF NOT EXISTS '{}' (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)".format(uname2))
        c.execute("INSERT INTO '{}'(task, status) VALUES('Add Your New Milestone ', 'Incomplete')".format(uname2))
        conn.commit()
        return redirect("/bucket")

#Displays user"s bucket list / Home page
@route("/bucket", method="GET")
def bucket_list():
    c = conn.cursor()
    c.execute("SELECT * FROM '{}'".format(uname2))
    result = c.fetchall()
    c.close()
    return template("templates/make_table", rows=result)

#Add a new task to the list
@route("/new", method="GET")
def new_item():
 if request.GET.save:
    new = request.GET.task.strip()
    c = conn.cursor()
    c.execute("INSERT INTO '{}' (task,status) VALUES ('{}','{}')".format(uname2,new, "Incomplete"))
    conn.commit()
    return redirect("/bucket")

 else:
     return template("templates/new_task.html")

#edits current task
@route("/edit/<no:int>", method="GET")
def edit_item(no):
    edit = request.GET.task.strip()
    status = request.GET.status.strip()
    if request.GET.save:
        if status == "Complete":
            status = "Complete"
        else:
            status = "Incomplete"
            
        c = conn.cursor()
        c.execute("UPDATE '{}' SET task = '{}', status = '{}' WHERE id LIKE '{}'".format(uname2, edit, status, no))
        conn.commit()
        return redirect("/bucket")

#deletes task
    elif request.GET.delete:
        c = conn.cursor()
        c.execute("DELETE FROM '{}' WHERE task = '{}' AND id = '{}'".format(uname2, edit, no))
        conn.commit()
        return redirect("/bucket")

    else:
        c = conn.cursor()
        c.execute("SELECT task FROM '{}' WHERE id LIKE '{}'".format(uname2,str(no)))
        cur_data = c.fetchone()
        return template("templates/edit_task", old=cur_data, no=no)


#catach an error
@error(404)
def mistake404(code):
    return "Sorry, this page does not exist!"

debug(True)
run(reloader=True)