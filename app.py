from datetime import datetime as date
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = 'some_super_secret_key' # This is required for logins because flask uses that key to generate secure cookies

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

def User(user, pass):
    @attribute
    username = user
    password = pass
    
def main():
    add_users = true
    userList = []
    while add_users:
        username = input("What is the username: ")
        password = input("What is the password: ")
        userList.append(User(username, password)
        add_more_users = input("Would you like to add more users? ")
        if add_more_users == 'n':
            add_users = False

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
​
user_database = []

user_database.append(User("admin", "1234qwer"))

user_database.append(User("user1", "pass1"))
​
print("Password database is ")
for i in user_database:
    print("User: {}, Password: {}".format(i.username, i.password))

​change_password = input("Would you like to change a password? ")

if 'y' in change_password:
    username = input("What user would you like to change? ")
    for i in user_database:
        if i.username == username:
            current_password = input("What is the current password: ")

            if current_password == i.password:
                new_password = input("What is the new password: ")
                new_password2 = input("Re-enter the new password: ")
          
                if new_password == new_password2:
                    i.password = new_password
                    print("New password of {} is {}".format(i.username, i.password))
                else:
                    print("new passes didn't match")
            else:
                print("Current password entered incorrectly")
        else:
            continue
else:
    print("Thank you for using the password changer")

for i in user_database:
    print("User: {}, Password: {}".format(i.username, i.password))

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



