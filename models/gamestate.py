import json
class GameState:
    def __init__(self, userName, gameLevel, gameScore, scoreToNextLevel, currentGold, gameOver, gameTime):
        self.userName = userName
        self.gameLevel = gameLevel
        self.gameScore = gameScore
        self.scoreToNextLevel = scoreToNextLevel
        self.currentGold = currentGold
        self.gameOver = gameOver
        self.gameTime = gameTime

    def to_json(self):
        game_state_dict = {}
        game_state_dict["userName"] = self.userName
        game_state_dict["gameLevel"] = self.gameLevel
        game_state_dict["gameScore"] = self.gameScore
        game_state_dict["scoreToNextLevel"] = self.scoreToNextLevel
        game_state_dict["currentGold"] = self.currentGold
        game_state_dict["gameOver"] = str(self.gameOver)
        game_state_dict["gameTime"] = self.gameTime.strftime('%Y-%m-%d %H:%M:%S')
        return json.dumps(game_state_dict)