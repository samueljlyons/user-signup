from flask import Flask, request, redirect, render_template
import cgi
import os

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
    return render_template('signup.html')



@app.route('/welcome', methods=['POST'])
def welcome():
    username=request.form['username']
    #print(name)
    return '<h1> Welcome ' + name + '!</h1>'




app.run()