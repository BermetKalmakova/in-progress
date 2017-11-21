from flask import Flask, render_template, request, session, redirect, url_for, flash
import urllib2, json, sqlite3, os, csv

my_app = Flask(__name__)
my_app.secret_key = os.urandom(32)

@my_app.route('/', methods=['GET','POST'])
def root():
    if ('user' in session):
        return redirect(url_for("home"))
    return render_template('login.html')

@my_app.route('/login', methods=['GET','POST'])
def login():
    user = request.form['name']
    password = request.form['password']
    db = sqlite3.connect("data/users.db")
    c = db.cursor()
    found = c.execute("SELECT count(*) FROM users WHERE username = '%s' AND password = '%s'" %(user, password))
    for num in found:
        db.commit()
        db.close()
        return (num[0] == 1)

@my_app.route('/home', methods=['GET','POST'])
def home():
    if ('user' in session):
        return render_template('home.html')
    return redirect(url_for('root'))

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
