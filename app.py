import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DATABASE = "users.db"
SCHEMA = "schema.sql"


def init_db():
    db = sqlite3.connect(DATABASE)
    with open(SCHEMA, "r", encoding="utf-8") as f:
        db.executescript(f.read())
    db.commit()
    db.close()


@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()

            # INTENTIONALLY INSECURE FOR TEACHING
            query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            result = cursor.execute(query).fetchone()

            if result:
                message = f"Login successful. Welcome {username}."
            else:
                message = "Login failed. Invalid username or password."

            db.close()

        except Exception as e:
            message = f"Database error: {e}"

        return render_template("result.html", message=message)

    return render_template("login.html")


if __name__ == "__main__":
    if not os.path.exists(DATABASE):
        init_db()
        print("Database created.")

    app.run(debug=True)