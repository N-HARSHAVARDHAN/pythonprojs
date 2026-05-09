import csv
import numpy as np
import matplotlib.pyplot as plt
def calculate():
    def aggregationCount_year():
        data_count={
            "years":{},
            "pba":{}
        }
        with open("../data/Maharashtra.csv") as f:
            data=csv.DictReader(f)
            for i in data:
                date=i['CompanyRegistrationdate_date'].strip()
                if "-" in date:
                    parts= date.split("-")
                    if len(parts[0]) == 4:
                        year = parts[0]  
                    else:
                        year = parts[2]
                    year=int(year)
                    if year>=2015 and year<=2026:
                        pba = i["CompanyIndustrialClassification"].strip()
                        if year in data_count["years"]:
                            data_count["years"][year]+=1
                        else:
                            data_count["years"][year]=1
                        if pba not in data_count['pba']:
                            data_count['pba'][pba]={}
                        if year in data_count['pba'][pba]:
                            data_count['pba'][pba][year]+=1
                        else:
                            data_count['pba'][pba][year]=1

        return data_count
    def top5_pba(data):
        total_counts = {}
        for pba in data:
            total_counts[pba] = sum(data[pba].values())
        sorted_pba = sorted(
            total_counts,
            key=total_counts.get,
            reverse=True
        )
        return sorted_pba[:5]

    return top5_pba() , aggregationCount_year()
def plot(data,top5):
    years = list(range(2015, 2025))
    x = np.arange(len(years))
    width = 0.15
    plt.figure(figsize=(16,8))
    for index, pba in enumerate(top5):
        counts = []
        for year in years:
            if year in data['pba'][pba]:
                counts.append(data['pba'][pba][year])
            else:
                counts.append(0)
        plt.bar(
            x + index * width,
            counts,
            width,
            label=pba
)
    plt.xlabel("Year")
    plt.ylabel("Registration Count")
    plt.title("Top 5 Principal Business Activities (2015-2024)")
    plt.xticks(x + width * 2, years)
    plt.legend()
    plt.tight_layout()
    plt.savefig( "../plots/grouped_bar_plot_top5_pba.jpg")
def execute():
    data,top5=calculate()
    plot(data,top5)
execute()

