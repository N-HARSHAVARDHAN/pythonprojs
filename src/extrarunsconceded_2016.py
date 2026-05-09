import csv
import matplotlib.pyplot as plt
def calculate():
    extra_runs_2016={}
    match_id=set()
    with open("../data/matches.csv") as f:
        id_data=csv.DictReader(f)
        for i in id_data:
            if i['season']=='2016':
                match_id.add(i['id'])
    with open("../data/deliveries.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            if i['match_id'] in match_id:
                team=i['bowling_team']
                extra_runs=int(i['extra_runs'])
                if team in extra_runs_2016:
                    extra_runs_2016[team]+=extra_runs
                else:
                    extra_runs_2016[team]=extra_runs
    return extra_runs_2016
def plot(data):
    teams = list(data.keys())
    runs = list(data.values())

    plt.figure(figsize=(10,5))
    plt.bar(teams, runs)

    plt.xlabel("Teams")
    plt.ylabel("Extra Runs Conceded")
    plt.title("Extra Runs Conceded by Teams in IPL 2016")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("../plots/extra_runs_2016.png")
def execute():
    data=calculate()
    plot(data)
execute()
