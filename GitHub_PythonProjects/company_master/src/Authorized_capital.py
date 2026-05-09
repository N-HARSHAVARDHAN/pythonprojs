import csv
import matplotlib.pyplot as plt
def Calculate():
    interval = {
        "<=1L": 0,
        "1L-10L": 0,
        "10L-1Cr": 0,
        "1Cr-10Cr": 0,
        ">10Cr": 0
    }
    with open("../data/Maharashtra.csv") as f:
        data = csv.DictReader(f)

        for i in data:
            cap = (float(i["AuthorizedCapital"]))

            if cap <= 100000:  
                interval["<=1L"] += 1

            elif cap <= 1000000: 
                interval["1L-10L"] += 1

            elif cap <= 10000000: 
                interval["10L-1Cr"] += 1

            elif cap <= 100000000: 
                interval["1Cr-10Cr"] += 1

            else:
                interval[">10Cr"] += 1
    return interval
def plot(data):
    labels = list(data.keys())
    values = list(data.values())
    plt.figure(figsize=(8,5))
    plt.bar(labels, values)
    plt.title("Histogram of Authorized Capital")
    plt.xlabel("Capital Range")
    plt.ylabel("Number of Companies")
    plt.xticks(rotation=30)
    plt.savefig("../plots/AuthorizedCap.jpg")
def execute():
    data=Calculate()
    plot(data)
execute()