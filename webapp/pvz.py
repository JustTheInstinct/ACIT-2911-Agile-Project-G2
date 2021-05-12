from flask import Blueprint, render_template
from .scoremanager import get_scores

pvz_bp = Blueprint("pvz",__name__)

@pvz_bp.route("/")
def home():
    return render_template("home.html")

@pvz_bp.route("/about")
def about():
    return render_template("about.html")

@pvz_bp.route("/scoreboard")
def score():
    scores = get_scores()
    return render_template("scoreboard.html", scores = scores)

@pvz_bp.route("/scoreboard/<int:player_id>")
def player(player_id):
    scores = get_scores()
    for score in scores:
        if score["id"] == str(player_id):
            return render_template("player.html", score = score)

@pvz_bp.route("/units")
def units():
    return render_template("units.html")
