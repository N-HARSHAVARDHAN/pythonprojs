import csv
import matplotlib.pyplot as plt
def calculte():
    saarc_population={}
    saarc = [
        "Afghanistan",
        "Bangladesh",
        "Bhutan",
        "India",
        "Maldives",
        "Nepal",
        "Pakistan",
        "Sri Lanka"
    ]
    with open("../data/population_estimates.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            country=i['Region']
            year=i['Year']
            if country in saarc and i['Population']!='None':
                if year in saarc_population:
                    saarc_population[year]+=float(i['Population'])
                else:
                    saarc_population[year]=float(i['Population'])
    return saarc_population
def plot(data):
    year=data.keys()
    population=data.values()
    plt.figure(figsize=(12,6))
    plt.bar(year,population)
    plt.xlabel("year")
    plt.ylabel("Population count")
    plt.title("SAARC POPULATION OVER YEARS")
    plt.xticks(rotation=86)
    plt.tight_layout()
    plt.savefig("../plots/saarc_population_byyear.jpg")
def execute():
    data=calculte()
    plot(data)
execute()
