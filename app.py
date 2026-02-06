from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create Database
def init_db():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            rating TEXT,
            message TEXT
        )
    """)

    conn.commit()
    conn.close()


init_db()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["name"]
        rating = request.form["rating"]
        message = request.form["message"]

        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()

        c.execute("INSERT INTO feedback VALUES (NULL,?,?,?)",
                  (name, rating, message))

        conn.commit()
        conn.close()

        return redirect("/thanks")

    return render_template("chat.html")


@app.route("/thanks")
def thanks():
    return "<h2 style='text-align:center;margin-top:50px;'>Thank You for Your Feedback! ✅</h2>"


if __name__ == "__main__":
    app.run(debug=True)
