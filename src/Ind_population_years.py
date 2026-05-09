import csv
import matplotlib.pyplot as plt
def calculte():
    ind_data={}
    with open("../data/population_estimates.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            if i['Region'].lower()=='india' and i['Population']!='None':
                ind_data[i['Year']]=int(float(i['Population']))
    return ind_data
def plot(data):
    year=data.keys()
    population=data.values()
    plt.figure(figsize=(10,5))
    plt.bar(year,population)
    plt.xlabel("Year")
    plt.ylabel("Population count")
    plt.title("INDIA POPULATION OVER YEARS")
    plt.xticks(rotation=85)
    plt.tight_layout()
    plt.savefig("../plots/india_population_byyear.jpg")
def execute():
    data=calculte()  
    plot(data)
execute()
