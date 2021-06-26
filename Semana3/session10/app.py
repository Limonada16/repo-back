from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

@app.route('/')
def index():

    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM producto''')
    results = cur.fetchall()

    return str(results)