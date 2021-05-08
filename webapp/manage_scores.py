import csv

def extract_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        players = []
        for line in reader:
            players.append(line)
    return players

def process_score(players):
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
    data = extract_data(filename)
    scores = process_score(data)
    return scores

def main():
    get_scores()

if __name__ == "__main__":
    main()