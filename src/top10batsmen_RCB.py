import csv
import matplotlib.pyplot as plt
def calculate():
    team_data={}
    with open("../data/deliveries.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            batsman=i['batsman']
            batsman_runs=int(i['batsman_runs'])
            if i['batting_team']=='Royal Challengers Bangalore':
                if batsman in team_data:
                    team_data[batsman]+=batsman_runs
                else:
                    team_data[batsman]=batsman_runs
    return team_data
def plot(data):
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_data[:10]
    names = [i[0] for i in top_10]
    runs = [i[1] for i in top_10]
    plt.figure(figsize=(10,5))
    plt.bar(names, runs)
    plt.xlabel("Batsmen")
    plt.ylabel("Total Runs")
    plt.title("Top 10 RCB Batsmen by Runs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../plots/top10batsmen_RCB.png")
def execute():
    data=calculate()
    plot(data)
execute()
