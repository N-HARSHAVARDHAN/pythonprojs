import csv
import matplotlib.pyplot as plt
def calculate():
    umpire_country={}
    with open("../data/umpire_country.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            umpire_country[i['umpire']]=i['country']
    country_cnt={}
    with open("../data/matches.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            for umpire in i['umpire1'] , i['umpire2'] , i['umpire3']:
                if umpire in umpire_country:
                    if umpire_country[umpire].upper()!='INDIA':
                        if umpire_country[umpire] in country_cnt:
                            country_cnt[umpire_country[umpire]]+=1
                        else:
                            country_cnt[umpire_country[umpire]]=1
    return country_cnt
def plot(data):
    country=data.keys()
    count=data.values()
    plt.figure(figsize=(10,5))
    plt.bar(country,count)
    plt.xlabel("Umpire Country")
    plt.ylabel("Count of empires")
    plt.title("Total count of foriegn umpires in IPL")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../plots/foreign_umpires_cnt.jpg")

def execute():
    data=calculate()
    plot(data)
execute()
