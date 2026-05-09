import csv
import re
import matplotlib.pyplot as plt
def calculate():
    def extractZip(adress):
        found=re.search(r"\b\d{6}\b",adress)
        if found:
            return found.group()
        else:
            return None
    def districtRegistrations():
        district_Registrations={}
        distcodes={}
        with open("../data/zipcodes.csv") as f:
            data=csv.DictReader(f)
            for i in data:
                distcodes[i['PinCode']]=i['District']
        
        with open("data/Maharashtra.csv") as f:
            data=csv.DictReader(f)
            for i in data:
                date=i['CompanyRegistrationdate_date'].strip()
                zipcode=extractZip(i['Registered_Office_Address'])
                if "-" in date:
                    parts = date.split("-")
                    if len(parts[0]) == 4:
                        year = parts[0]  
                    else:
                        year = parts[2]
                    year=int(year)
                    if year==2015:
                        if zipcode in distcodes:
                            district=distcodes[zipcode]
                            if district in district_Registrations:
                                district_Registrations[district]+=1
                            else:
                                district_Registrations[district]=1
        print("ZIP:", zipcode)
        print("YEAR:", year)
        print("DISTCODES SIZE:", len(distcodes))
        return district_Registrations
    Registration_district=districtRegistrations()
    return Registration_district
def plot(result):
    districts=list(result.keys())
    count=list(result.values())
    plt.figure(figsize=(12,6))
    plt.bar(districts,count)
    plt.xlabel("District")
    plt.ylabel("Number of Registrations (2015)")
    plt.title("Company Registration in 2015 by District")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../plots/district_registration_2015.jpg")
def execute():
    result=calculate()
    plot(result)
execute()