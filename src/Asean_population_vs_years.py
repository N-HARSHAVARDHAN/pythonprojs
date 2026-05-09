import csv
import numpy as np
import matplotlib.pyplot as plt
def calculte():
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
    populationOverYears={}
    with open("../data/population_estimates.csv") as f:
        data=csv.DictReader(f)
        for i in data:
            country=i['Region']
            if country in asean and i['Population']!='None':
                if country not in populationOverYears:
                    populationOverYears[country]={}
                populationOverYears[i['Region']][i["Year"]]=int(i["Population"])
    return populationOverYears
def plot(data):

    years = [str(year) for year in range(2004, 2015)]

    countries = list(data.keys())

    x = np.arange(len(years))

    width = 0.07

    plt.figure(figsize=(18,8))

    for index, country in enumerate(countries):

        population = []

        for year in years:

            if year in data[country]:
                population.append(data[country][year])
            else:
                population.append(0)

        plt.bar(
            x + index * width,
            population,
            width,
            label=country
        )

    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.title("ASEAN Population vs Years (2004-2014)")

    plt.xticks(x + width * 5, years)

    plt.legend()

    plt.tight_layout()

    plt.savefig("../plots/asean_grouped_bar_chart.jpg")
def execute():
    data=calculte()
    plot(data)
execute()
