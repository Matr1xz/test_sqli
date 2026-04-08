from flask import Flask, request, render_template, redirect, session, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "ctf-secret-key"
DB_PATH = os.environ.get("DB_PATH", "lab.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("search"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, username FROM users WHERE username=? AND password=?", (username, password))
        row = cur.fetchone()
        conn.close()

        if row:
            session["user"] = row["username"]
            return redirect(url_for("search"))
        else:
            error = "Invalid credentials"

    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/search", methods=["GET", "POST"])
def search():
    if "user" not in session:
        return redirect(url_for("login"))

    rows = []
    error = None
    debug_query = None

    if request.method == "POST":
        keyword = request.form.get("keyword", "")

        # INTENTIONALLY VULNERABLE FOR CTF TRAINING
        debug_query = f"SELECT id, name, email FROM customers WHERE name LIKE '%{keyword}%'"
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute(debug_query)  # vulnerable on purpose
            rows = cur.fetchall()
            conn.close()
        except Exception as e:
            error = str(e)

    return render_template("search.html", rows=rows, error=error, debug_query=debug_query, user=session["user"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)