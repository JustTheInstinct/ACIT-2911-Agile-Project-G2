from flask import Flask, render_template, request
import os
import psycopg2


app = Flask(__name__)

def get_sql():
    conn = psycopg2.connect(
        host="ec2-54-152-185-191.compute-1.amazonaws.com",
        database="d92mgnjut4mfd1",
        user="bpfvqodctmlkfk",
        port="5432",
        password="2e2c399974dd83b5ac8664d0fbe7e0f6c2aad1e335b3d5e2948579fd5e5e0fca")
    c = conn.cursor()
    c.execute("SELECT * FROM scores;")
    rows = c.fetchall()
    dict_list = []
    for player in rows:
        score_dict = {}
        score_dict["name"] = player[1]
        score_dict["id"] = player[0]
        score_dict["level"] = player[2]
        score_dict["score"] = player[3]
        dict_list.append(score_dict)
    return dict_list

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        scores = get_sql()
        for score in scores:
            if score["name"] == username:
                return render_template("player.html", score = score)
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/scoreboard")
def score():
    scores = get_sql()
    return render_template("scoreboard.html", scores = scores)

@app.route("/scoreboard/<string:player_name>")
def player(player_name):
    scores = get_sql()
    for score in scores:
        if score["name"] == player_name:
            return render_template("player.html", score = score)

@app.route("/units")
def units():
    return render_template("units.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
    get_sql()