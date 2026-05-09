import csv
import matplotlib.pyplot as plt
def calculate():
    economy_2015={}
    bowler_data={}
    match_id=set()
    with open("../data/matches.csv") as f:
        id_data=csv.DictReader(f)
        for i in id_data:
            if i['season']=='2015':
                match_id.add(i['id'])
    with open("../data/deliveries.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            if i['match_id'] in match_id:
                bowler=i['bowler']
                runs=int(i['total_runs'])
                wides=int(i['wide_runs'])
                noballs=int(i['noball_runs'])
                if bowler not in bowler_data:
                    bowler_data[bowler]={'runs':0 ,'balls':0} 
                bowler_data[bowler]['runs']+=runs
                if wides==0 and noballs==0:
                    bowler_data[bowler]['balls']+=1
        for bowler in bowler_data:
            balls=bowler_data[bowler]['balls']
            runs=bowler_data[bowler]['runs']
            if balls>0:
                economy_2015[bowler]=(runs/balls)*6
    sorted_bowlers = sorted(economy_2015.items(), key=lambda x: x[1])
    return sorted_bowlers[:10]

def plot(data):
    bowlers = [i[0] for i in data]
    economy = [i[1] for i in data]

    plt.figure(figsize=(10,5))
    plt.bar(bowlers, economy)

    plt.xlabel("Bowlers")
    plt.ylabel("Economy Rate")
    plt.title("Top 10 Economical Bowlers (IPL 2015)")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("../plots/top10_economy_2015.png")

def execute():
    data=calculate()
    plot(data)

execute()
