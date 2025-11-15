from flask import Flask, render_template, request, redirect, url_for, session, flash, g
app =Flask

@app.route("/heloo" , methods=["GET","POST"])
def helloPage():
    if request.method =="GET":
         return "Write your name"
   
    if request.method =="GET":
       name = request.form.get("name")
       if name == "":
            return "No name"
       else :
           return f"hello {name}"
       

@app.route("/add", methods =["GET","POST"])
def add():
    if request.method =="GET":
        return "Send two numbers"
    if request.method =="POST":
        num1 = int(request.form.get("number1",""))
        num2 = int(request.form.get("number2",""))
        if num1 =="" or num2 == "":
            return "MISSING NUMBER"  
        else: 
            sum = num1 +num2
            return sum



def get_db():
    return "db"


def get_all_users():
    db = get_db()
    users = db.execute("SELECT id FROM users").fetchall()
    return users

def get_user_by_email(email):
    db = get_db()
    user = db.execute(
        "SELECT id, email, password_hash FROM users WHERE email = ?",
        (email,)
    ).fetchone()
    return user


@app.route("/fake_login",methods=["GET"])
def fake_login():
     session["user_id"]=1
     return "You are now logged in as user 1"


@app.route("/whoami",methods =["GET"])
def whoami():
    if session.get("user_id"):
        return f"You are logged in as user {session.get("user_id")}"
    else:
      return " Not logged in"





       
