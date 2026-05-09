import csv
import matplotlib.pyplot as plt
def calculate():
    matches_won={}
    with open("../data/matches.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            season=i['season']
            winner=i['winner']
            if season not in matches_won:
                matches_won[season]={}
            if winner in matches_won[season]:
                matches_won[season][winner]+=1
            else:
                matches_won[season][winner]=1
    return matches_won
def plot(data):
    seasons = sorted(data.keys())

    teams = set()
    for s in data:
        teams.update(data[s].keys())
    teams = list(teams)

    bottom = [0] * len(seasons)

    plt.figure(figsize=(12,6))

    for team in teams:
        values = []
        for s in seasons:
            values.append(data[s].get(team, 0))

        plt.bar(seasons, values, bottom=bottom, label=team)

        bottom = [bottom[i] + values[i] for i in range(len(values))]

    plt.xlabel("Season")
    plt.ylabel("Matches Won")
    plt.title("Matches Won Per Team Per Year")

    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.tight_layout()

    plt.savefig("../plots/matches_won.png")

def execute():
    data=calculate()
    plot(data)
execute()