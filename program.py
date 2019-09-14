# python 3.5+
from flask import Flask, render_template, request
import sqlite3
from email_sender import email_sender


def calculate_average(data):
    total_height = 0
    for item in data:
        total_height += int(item[0])
    return round(total_height / len(data), 2), len(data)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/answer", methods=["POST"])
def answer():
    if request.method == "POST":
        email = request.form["email_name"]
        height = int(request.form["height_name"])
        connection = sqlite3.connect("height_db.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS height_table("
                       "email TEXT UNIQUE PRIMARY KEY, height INTEGER);")
        connection.commit()
        try:
            cursor.execute("INSERT INTO height_table VALUES(?, ?);",
                           (email, height))
            connection.commit()
        except sqlite3.IntegrityError:
            connection.close()
            return render_template("error.html")
        heights = cursor.execute("SELECT height from height_table")
        data = heights.fetchall()
        connection.close()
        average_height = calculate_average(data)
        email_sender(email, height, average_height, len(data))
    return render_template("success.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
