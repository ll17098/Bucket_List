import sqlite3
from bottle import route, run, template, request, debug, error



@route('/')
def login():
    return template('templates/login.html')

@route('/checkLogin', method=['POST'])
def checklogin():
    uname = request.GET.username.strip()
    pword = request.GET.password.strip()
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM userInfo WHERE username LIKE ? AND password LIKE ?", (uname, pword))
    result = c.fetchall()
    
    if  result == uname and pword:
        return 'logged in'

    else:
        return 'Incorrect Login'


@route("/reg", method="GET")
def register():
 if request.GET.save:
    username = request.GET.Rusername.strip()
    password = request.GET.Rpassword.strip()

    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    c.execute("INSERT INTO userInfo (username,password) VALUES (?, ?)", (username, password))
    conn.commit()
    c.close()
    return 'registered'
 else:
    return template('templates/reg.html')

@route('/bucket', method='GET')
def bucket_list():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT id, task, status FROM bucket")
    result = c.fetchall()
    c.close()
    return template('templates/make_table', rows=result)

@route('/new', method='GET')
def new_item():
 if request.GET.save:
    new = request.GET.task.strip()

    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    c.execute("INSERT INTO bucket (task,status) VALUES (?,?)", (new, "Incomplete"))
    conn.commit()
    return bucket_list()

 else:
     return template('templates/new_task.html')

@route('/edit', method='GET')
def edit_item(no):

    edit = request.GET.task.strip()
    status = request.GET.status.strip()

    if request.GET.save:
        if status == "Complete":
            status = "Incomplete"

        else:
            status = "Incomplete"
            
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute("UPDATE bucket SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no

    elif request.GET.delete:
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute("DELETE FROM bucket WHERE task = ? AND id = ?", (edit, no))
        conn.commit()

        return '<p>The item number %s was successfully deleted</p>' % no
    else:
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute("SELECT task FROM bucket WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()
        return template('templates/edit_task', old=cur_data, no=no)

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

debug(True)
run(reloader=True)