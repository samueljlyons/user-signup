from flask import Flask, request, redirect, render_template
import cgi
import os

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
    return render_template('signup.html', username_error='', password_error='',verify_error='',
    email_error='', username='',password='', verify='', email='')



@app.route('/', methods=['POST'])
def welcome():
    username=request.form['username']
    #print(name)
    return '<h1> Welcome ' + username + '!</h1>'
#def input_valid():
 #   try:
  #      user_input=input(username)
       # return True
    #except ValueError:
     #   return False

@app.route('/', methods=['POST'])
def validate_info():
    username=request.form['username']
    password=request.form['password']
    verify=request.form['verify']
    email=request.form['email']

    username_error=''
    password_error=''
    verify_error=''
    email_error=''

    if username=='':
        username_error='Please enter a username'
    elif len(username)>20 or len(username)<3:
        username_error='Username is too short or too long'

    if not '@' in email or not '.' in email:
        email_error='Not a valid email address'
    if not username_error and not password_error and not verify_error and not email_error:
        return welcome
    else:
        return render_template("signup.html",
        username_error=username_error,password_error=password_error,
        verify_error=verify_error,email_error=email_error,username=username,password=password,
        verify=verify,email=email)





app.run()