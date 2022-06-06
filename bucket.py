import sqlite3
from bottle import route, run, template, request, debug, error, redirect, view


#connects to databsse
conn = sqlite3.connect("mydatabase.db")

#Login page / landing page
@route("/")
def login():
    checklogin()
    return template("templates/login.html")

#validates a users login inout
@route("/", method=["POST"])
def checklogin():
    uname = request.GET.username.strip()
    pword = request.GET.password.strip()
    c = conn.cursor()
    c.execute("SELECT username, password FROM userInfo WHERE username LIKE ? AND password LIKE ? ", (uname, pword))

    
    

#Records users new log in details into sql
@route("/reg", method="GET")
def register():
    if request.method =="GET":
        return template("templates/reg.html")

    if request.GET.save and len(usernamecheck) == 0:
        username = request.GET.username.strip()
        password = request.GET.password.strip()
        usernamecheck = c.execute("SELECT COUNT(*) FROM userInfo WHERE username LIKE ?", username=username)
        
        
        c = conn.cursor()
        c.execute("INSERT INTO userInfo (username, password) VALUES (?,?)", (username, password))
        conn.commit()
        return "registered<br><a href='/bucket'>Home</a>"

    elif request.GET.save and len(usernamecheck) > 0:
        return "usename already Exists"

        
        
#Displays user"s bucket list / Home page
@route("/bucket", method="GET")
def bucket_list():
    c = conn.cursor()
    c.execute("SELECT id, task, status FROM bucket")
    result = c.fetchall()
    c.close()
    return template("templates/make_table", rows=result)

#Add a new task to the list
@route("/new", method="GET")
def new_item():
 if request.GET.save:
    new = request.GET.task.strip()
    c = conn.cursor()
    c.execute("INSERT INTO bucket (task,status) VALUES (?,?)", (new, "Incomplete"))
    conn.commit()
    return bucket_list()

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
        c.execute("UPDATE bucket SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()
        return bucket_list()

#deletes task
    elif request.GET.delete:
        c = conn.cursor()
        c.execute("DELETE FROM bucket WHERE task = ? AND id = ?", (edit, no))
        conn.commit()
        return bucket_list()

    else:
        c = conn.cursor()
        c.execute("SELECT task FROM bucket WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()
        return template("templates/edit_task", old=cur_data, no=no)


#catach an error
@error(404)
def mistake404(code):
    return "Sorry, this page does not exist!"

debug(True)
run(reloader=True)