#this is the template of the backend

from flask import Flask, redirect, render_template, request, session, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

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
    if "user_id" in session:
        return 

    return

@app.route("/register")
def register():
    # Dagim
    '''
    activated: when the "Register" link is pressed from the sign in page

    Get login information and save to the necessary database

    return the register html
    '''
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not email or not password:
            return render_template("placeholder.html", error="All fields are required.")

        password_hash = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                (username, email, password_hash)
            )
            conn.commit()

            user_id = cursor.lastrowid
            session["user_id"] = user_id
            session["username"] = username

            conn.close()
            return redirect(url_for("home"))

        except sqlite3.IntegrityError:
            conn.close()
            return render_template(
                "register.html",
                error="Username or email already exists."
            )

    return render_template("register.html")

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