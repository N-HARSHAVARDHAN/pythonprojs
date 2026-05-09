import csv
import matplotlib.pyplot as plt
def calculate(): 
    asean = [
        "Brunei",
        "Cambodia",
        "Indonesia",
        "Laos",
        "Malaysia",
        "Myanmar",
        "Philippines",
        "Singapore",
        "Thailand",
        "Vietnam",
        "Timor-Leste"
    ]
    asean_population={}
    with open("../data/population_estimates.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            country=i['Region']
            if country in asean:
                if i['Year'] == '2014' and i['Population']!='None':
                    if country in asean_population:
                        asean_population[country]+=float(i['Population'])
                    else:
                        asean_population[country]=float(i['Population'])
    return asean_population
def plot(data):
    country=data.keys()
    population=data.values()
    plt.figure(figsize=(10,5))
    plt.bar(country,population)
    plt.xlabel("Country")
    plt.ylabel("Population count")
    plt.title("ASEAN COUNTRIES POPULATION IN 2014")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../plots/asean_population_2014.jpg")
def execute():
    data=calculate()
    plot(data)
execute()
    
