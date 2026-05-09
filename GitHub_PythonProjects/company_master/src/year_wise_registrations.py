import csv
import matplotlib.pyplot as plt
def calculate():
    def yearlyRegistrations():
        year_count = {}

        with open("../data/Maharashtra.csv") as f:
            data= csv.DictReader(f)

            for i in data:
                date = i["CompanyRegistrationdate_date"].strip()
                if "-" in date:
                    parts = date.split("-")
                    if len(parts[0]) == 4:
                        year = parts[0]  
                    else:
                            year = parts[2]
                year = int(year)
                if year in year_count:
                    year_count[year] += 1
                else:
                    year_count[year] = 1
        return year_count
    year_count=yearlyRegistrations()
    sorted_years = sorted(year_count.keys())
    counts = [year_count[y] for y in sorted_years]
    return sorted_years,counts
def plot(sorted_years,counts):
    plt.figure(figsize=(10,5))
    plt.bar(sorted_years, counts)
    plt.title("Company Registrations by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Companies")
    plt.xticks(rotation=45)
    plt.savefig("../plots/registrations_by_year.jpg")
def execute():
    sorted_years,counts=calculate()
    plot(sorted_years,counts)
execute()