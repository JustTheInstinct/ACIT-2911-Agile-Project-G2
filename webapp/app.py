from flask import Flask, render_template
import os
from pathlib import Path
import sqlite3

def get_sql():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "pvzscore.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    rows = c.execute('''SELECT * FROM users''').fetchall()
    dict_list = []
    for player in rows:
        score_dict = {}
        score_dict["name"] = player[1]
        score_dict["id"] = player[0]
        score_dict["level"] = player[2]
        score_dict["score"] = player[3]
        dict_list.append(score_dict)
    return dict_list

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/scoreboard")
def score():
    scores = get_sql()
    return render_template("scoreboard.html", scores = scores)

@app.route("/scoreboard/<int:player_id>")
def player(player_id):
    scores = get_sql()
    for score in scores:
        if score["id"] == player_id:
            return render_template("player.html", score = score)

@app.route("/units")
def units():
    return render_template("units.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
    get_sql()