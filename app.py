from datetime import datetime as date
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = ' supersecret key 2020'

def validate_password(password):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{12,25}$"
    pattern = re.compile(reg)
    match = re.search(pattern, password)
    if match:
        return True
    else:
        return False

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return redirect('/index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'P@$$w0rd1234' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        f = open("database.txt", "a")
        tname = ""
        for sub in username.split(" "):
            tname = tname + "_" + sub
        if not validate_password(password):
            message = "Password does not match requirements"
            return render_template("register.html", error=message)
        else:
            f.write("%s %s %s\n" % (tname, email, password))
            f.close()
            return render_template("register.html", error="successfully registered")
    else:
        return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        f = open("database.txt", "r")
        data = f.readlines()
        f.close()
        data = [x.split() for x in data]
        for item in data:
            if request.form['email'] == item[1].strip() and request.form['password'] == item[2].strip():
                session['visited'] = True
                return redirect('/index.html')
            else:
                error = "wrong credentials"
                return render_template("login.html", error=error)
    else:
        return render_template("login.html")
if __name__ == '__main__':
     app.run(host='127.0.0.1', port=5000)
@app.route('/')
@app.route('/index.html')
def page1(): # This was called home and was overwriting your earlier function
    return render_template('index.html', date = date.today() )

@app.route('/page2.html')
def page2():
    return render_template('page2.html', date = date.today() )

@app.route('/page3.html')
def page3():
    return render_template('page3.html', date = date.today() )

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == '__main__':
    app.run(debug = True)



