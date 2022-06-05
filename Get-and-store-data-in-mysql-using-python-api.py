from flask import Flask, redirect, url_for, request
import mysql.connector
import json

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="test"
)
mycursor = mydb.cursor()
app = Flask(__name__)

@app.route('/success/')
def success(name):
    return 'welcome %s' % name

def get():
    id = request.args.get('id')

    mycursor.execute("SELECT * FROM api_table WHERE id = '%s' ;" % id)
    row_headers=[x[0] for x in mycursor.description] #this will extract row headers
    rv = mycursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data)

def post():
    a_char = request.form['a_char']
    a_varchar = request.form['a_varchar']
    a_text = request.form['a_text']
    a_integer = request.form['a_integer']
    a_decimal = request.form['a_decimal']
    a_float = request.form['a_float']
    a_double = request.form['a_double']
    a_boolean = request.form['a_boolean']

    sql = "INSERT INTO `api_table`(`a_char`, `a_varchar`, `a_text`, `a_integer`, `a_decimal`, `a_float`, `a_double`, `a_boolean`) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
    val = (a_char, a_varchar, a_text, a_integer, a_decimal, a_float, a_double, a_boolean)
    mycursor.execute(sql, val)
    mydb.commit()
    return (mycursor.lastrowid)

@app.route('/all',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        id = post()
        return json.dumps({"id": id})

    elif request.method == 'GET':
        usr = get()
        return usr

if __name__ == '__main__':
    app.run(debug = True)