import sqlite3
from bottle import route, run, template, request, debug, static_file, error, view

@route("/")
@view("index")
def index():
    pass

@route('/bucket', method='GET')
def todo_list():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT id, task, status FROM bucket")
    result = c.fetchall()
    c.close()
    return template('make_table', rows=result)

@route('/new', method='GET')
def new_item():
    
 if request.GET.save:
    new = request.GET.task.strip()

    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    c.execute("INSERT INTO bucket (task,status) VALUES (?,?)", (new, 0))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
 else:
     return template('new_task.tpl')

@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1

        else:
            status = 0
            
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute("UPDATE bucket SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no

    elif request.GET.save:
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute("DELETE FROM bucket WHERE id = ?", (no))
        conn.commit()

        return '<p>The item number %s was successfully deleted</p>' % no
    else:
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        c.execute("SELECT task FROM bucket WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)

@route('/item<item:re:[0-9]+>')
def show_item(item):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT task FROM bucket WHERE id LIKE ?", (item,))
    result = c.fetchall()
    c.close()
    if not result:
        return 'This item number does not exist!'
    else:
        return 'Task: %s' % result[0]

@route('/help')
def help():
    return static_file('help.html', root='/path/to/file')

@route('/json<json:re:[0-9]+>')
def show_json(json):
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute("SELECT task FROM bucket WHERE id LIKE ?", (json,))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task': 'This item number does not exist!'}
    else:
        return {'task': result[0]}

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

debug(True)
run(reloader=True)