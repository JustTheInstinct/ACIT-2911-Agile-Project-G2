from flask import Flask, request, jsonify, render_template
from datetime import datetime
from models import GameState
from controllers import GameController
from multiprocessing import Process
import sys


player = sys.argv[1]
users_game_states = {}      #this a dict store all players score
gamestates = GameState(player, 0, 0, 0, 0, False, datetime.now())
users_game_states[player] = gamestates #I ask player enter name and store it as key

def to_dict(player):
    player_state = {}
    gamestate = users_game_states[player]
    player_state["userName"] = gamestate.userName
    player_state["gameLevel"] = gamestate.gameLevel
    player_state["gameScore"] = gamestate.gameScore
    player_state["scoreToNextLevel"] = gamestate.scoreToNextLevel
    player_state["currentGold"] = gamestate.currentGold
    player_state["gameOver"] = gamestate.gameOver
    player_state["gameTime"] = gamestate.gameTime
    return player_state

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", games=[to_dict(player)])

@app.route('/get_game_state', methods= ["post", "get"])
def get_game_stat():
    player_state = to_dict(player)
    return jsonify({"data": [player_state]})

@app.route('/update_game_state', methods=['post', 'get'])
def update_game_state():
    data = request.get_json()
    if data["userName"] in users_game_states:
        game_state = GameState(data["userName"], data["gameLevel"], data["gameScore"],
                               data["scoreToNextLevel"], data["currentGold"], data["gameOver"], data["gameTime"])
        users_game_states[data["userName"]] = game_state
    return jsonify({"status": "success"})


def start_game():
    game = GameController(player)
    game.start_game()

if __name__ == '__main__':
    gameProcess = Process(target=start_game)
    gameProcess.start()
    app.run("localhost", "5000")
