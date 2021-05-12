import csv

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
    filename = 'webapp/pvzscore.csv'
    data = load_scores(filename)
    scores = process_scores(data)
    return scores

def main():
    get_scores()

if __name__ == "__main__":
    main()