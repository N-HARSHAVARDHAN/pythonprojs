import csv
import matplotlib.pyplot as plt
def calculate():
    team_matches={}
    with open("../data/matches.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            season=i['season']
            team1=i['team1']
            team2=i['team2']
            if  season not in team_matches:
                team_matches[season]={}
            if team1 in team_matches[season]:
                team_matches[season][team1]+=1
            else:
                team_matches[season][team1]=1
            if team2 in team_matches[season]:
                team_matches[season][team2]+=1
            else:
                team_matches[season][team2]=1
    return team_matches
def plot(data):
    seasons = sorted(data.keys())
    teams = set()
    for s in data:
        teams.update(data[s].keys())
    teams = list(teams)
    bottom = [0] * len(seasons)
    for team in teams:
        values = []
        for s in seasons:
            values.append(data[s].get(team, 0))
        plt.bar(seasons, values, bottom=bottom, label=team)
        bottom = [bottom[i] + values[i] for i in range(len(values))]
    plt.xlabel("Season")
    plt.ylabel("Matches Played")
    plt.title("Matches Played by Team by Season")

    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.tight_layout()
    plt.savefig("../plots/no_of_games_played_team.png")
def execute():
    data=calculate()
    plot(data)
execute()
