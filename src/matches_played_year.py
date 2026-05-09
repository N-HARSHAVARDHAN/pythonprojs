import csv
import matplotlib.pyplot as plt
def calculate():
    matches_played_year={}
    with open("../data/matches.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            season=i['season']
            if season in matches_played_year:
                matches_played_year[season]+=1
            else:
                matches_played_year[season]=1
    return matches_played_year
def plot(data):
    seasons = list(data.keys())
    counts = list(data.values())
    plt.figure(figsize=(10,5))
    plt.bar(seasons, counts)
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.title("Matches Played Per Year (IPL)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../plots/matches_per_year.png")
def execute():
    data=calculate()
    plot(data)
execute()