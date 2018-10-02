from flask import Flask, request, redirect, render_template
import cgi
import os

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
    return render_template('signup.html')



@app.route('/welcome')
def welcome():
    welcome=request.args.get('welcome')
    return '<h1> Welcome!</h1>'.format(welcome)

app.run()