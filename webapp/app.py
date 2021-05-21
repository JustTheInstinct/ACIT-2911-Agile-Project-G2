from flask import Flask, render_template
import csv, os, pandas
from pathlib import Path
import sqlite3
def load_scores(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        players = []
        for line in reader:
            players.append(line)
    return players

def process_scores(players):
    dict_list = []
    for player in players:
        score_dict = {}
        score_dict["name"] = player["name"]
        score_dict["id"] = player["id"]
        score_dict["level"] = player["level"]
        score_dict["score"] = player["score"]
        dict_list.append(score_dict)
    return dict_list

def get_scores():
    filename = 'pvzscore.csv'
    data = load_scores(filename)
    scores = process_scores(data)
    return scores

def get_sql():
    conn = sqlite3.connect('pvzscore.db')
    c = conn.cursor()
    rows = c.execute('''SELECT * FROM users''').fetchall()
    dict_list = []
    for player in rows:
        score_dict = {}
        score_dict["name"] = player["name"]
        score_dict["id"] = player["id"]
        score_dict["level"] = player["level"]
        score_dict["score"] = player["score"]
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
        if score["id"] == str(player_id):
            return render_template("player.html", score = score)

@app.route("/units")
def units():
    return render_template("units.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
    get_sql()