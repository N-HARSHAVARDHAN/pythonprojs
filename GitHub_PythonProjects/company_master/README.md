````md id="7f4a91"
# Company Master - Maharashtra

## Aim

The aim of this project is to analyze Maharashtra company registration data and generate meaningful visualizations using Python and matplotlib.

---

## Dataset Source

Company master data of Maharashtra:

https://data.gov.in/catalog/company-master-data

Zipcode reference data was used to map company registration addresses to districts.

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

---

## Run

### Problem 1: Histogram of Authorized Capital

```bash id="cm1"
python src/Authorized_capital.py
```

### Problem 2: Company registrations by year

```bash id="cm2"
python src/year_wise_registrations.py
```

### Problem 3: Company registration in 2015 by district

```bash id="cm3"
python src/district_wise_registration_2015.py
```

### Problem 4: Grouped Bar Plot by Principal Business Activity

```bash id="cm4"
python src/registrationcount_over_year_PBA.py
```

---

## Output

All generated plots will be saved in the `plots/` directory.

---

## Problems Solved

1. Histogram of Authorized Capital
2. Company registrations by year
3. District-wise company registrations in 2015
4. Grouped bar plot of registrations by Principal Business Activity

---

## Technologies Used

* Python 3
* matplotlib
* csv module
* collections

---

## Project Structure

```text
company_master/
│
├── .venv/
├── data/
│   ├── Maharashtra.csv
│   └── zipcodes.csv
│
├── plots/
│   ├── authorized_cap.jpg
│   ├── registrations_by_year.jpg
│   ├── district_registration_2015.jpg
│   └── grouped_bar_plot_top5_pba.jpg
│
├── src/
│   ├── Authorized_capital.py
│   ├── year_wise_registrations.py
│   ├── district_wise_registration_2015.py
│   └── registrationcount_over_year_PBA.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

```
```
