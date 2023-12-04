from flask import Flask, request, render_template, redirect
import sqlite3
from markupsafe import escape

app = Flask(__name__, template_folder='templates')

# XSS
@app.route("/")
def index():
    name = request.args.get("name", "")
    return f"<h1>Hello, {name}!</h1>"

#SQLI

conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()

@app.route("/sqli/")
def sqli():
    username = request.args.get("username", "")
    password = request.args.get("password", "")
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return "<h1>Login successful.</h1>"
    else:
        return "<h1>Deny</h1>"





############## IDOR


users = [
    {"id": 1, "name": "Роман", "email": "@mail.ru"},
    {"id": 2, "name": "Алексей", "email": "@gmail.com"},
]

@app.route('/idor/')
def idor():
    return render_template('idor.html', users=users)


@app.route('/user/<int:user_id>')
def user_profile(user_id):
    for user in users:
        if user['id'] == user_id:
            return render_template('profile.html', user=user)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

