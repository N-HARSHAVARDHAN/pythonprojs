import csv
import matplotlib.pyplot as plt
def calculate():
    team_runs={}
    with open("../data/deliveries.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            batting_team=i['batting_team']
            total_runs=int(i['total_runs'])
            if batting_team in team_runs:
                team_runs[batting_team]+=total_runs
            else:
                team_runs[batting_team]=total_runs
    return team_runs
def plot(data):
    teams = list(data.keys())
    runs = list(data.values())

    plt.figure(figsize=(10,5))
    plt.bar(teams, runs)

    plt.xlabel("Teams")
    plt.ylabel("Total Runs")
    plt.title("Total Runs Scored by Each Team (IPL)")

    plt.xticks(rotation=70)
    plt.tight_layout()
    plt.savefig("../plots/totalruns_team.png")

def execute():
    data=calculate()
    plot(data)
execute()