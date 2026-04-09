#this is the template of the backend

from flask import Flask, redirect, render_template, request, session
# find a SQL libray that could work with this

app = Flask(__name__)

@app.route("/")
def index():
    # Dagim
    '''
    This is the landing page
    If there is a cookie/session established, return the home page html file (and fix route?)

    If there is no cookie/session established, return the sign in html page
    '''
    pass

@app.route("/register")
def register():
    # Dagim
    '''
    activated: when the "Register" link is pressed from the sign in page

    Get login information and save to the necessary database

    return the register html
    '''
    pass

@app.route("/home")
def home():
    '''
    From: automatic login, sign in page or register page

    Send the top 5 favorite books, the 4 recent;y read books, and reading stats to HTML to be rendered

    return the home page

    '''
    pass

@app.route("/books")
def books():
    '''
    send currently reading, want to read, frozen(paused), read, did not finish to html file
    (the shelves can be expaneded)

    return the books list page
    '''
    pass

@app.route("/settings")
def setting():
    # TBD
    pass