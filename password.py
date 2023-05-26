import pyotp    #generates one-time passwords
import sqlite3  #database for username/passwords
import hashlib  #secure hashes and message digests
import uuid     #for creating universally unique identifiers
from flask import Flask, request
app = Flask(__name__) #Be sure to use two underscores before and after "name"

db_name = 'test.db' 


######################################### Plain Text #########################################################
@app.route('/signup/v1', methods=['POST'])
def signup_v1():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_PLAIN
           (USERNAME  TEXT    PRIMARY KEY NOT NULL,
            PASSWORD  TEXT    NOT NULL);''')
    conn.commit()
    try:
        c.execute("INSERT INTO USER_PLAIN (USERNAME,PASSWORD) "
                  "VALUES ('{0}', '{1}')".format(request.form['username'], request.form['password']))
        conn.commit()
    except sqlite3.IntegrityError:
        return "El nombre de usuario ha sido registrado."
    print('username: ', request.form['username'], ' password: ', request.form['password'])
    return "Acceso completado."

def verify_plain(username, password):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    query = "SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = '{0}'".format(username)
    c.execute(query)
    records = c.fetchone()
    conn.close()
    if not records:
        return False
    return records[0] == password

@app.route('/login/v1', methods=['GET', 'POST'])
def login_v1():
    error = None
    if request.method == 'POST':
        if verify_plain(request.form['username'], request.form['password']):
            error = 'Acceso correcto'
        else:
            error = 'Nombre de usuario o contraseña invalido.'
    else:
        error = 'Invalid Method'
    return error

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, ssl_context='adhoc')
