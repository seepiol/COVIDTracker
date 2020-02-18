import csv
import datetime
import requests


# Getting the latest informations
i=0
date = datetime.date.today()
date = date.strftime("%m-%d-%Y")
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + date + ".csv"
daily_report = requests.get(url)
while daily_report.status_code != 200:
    i += 1
    date = datetime.date.today() - datetime.timedelta(i)
    date = date.strftime("%m-%d-%Y")
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + date + ".csv"
    daily_report = requests.get(url)


with open("covid.csv","w") as file:
    file.write(str(daily_report.content.decode("ascii")))

region = input("Insert your country or region: ").title()

if len(region)==2:
    region=region.upper()

total_confirmed=0
total_deaths=0
total_recovered=0

states = []
confirmed = 0
deaths = 0
recovered = 0

with open("covid.csv") as daily_report:
    parsed_daily_report = csv.reader(daily_report, delimiter=",")
    for row in parsed_daily_report:
        if row[0] == "Province/State":
            pass
        else:
            total_confirmed+=int(row[3])
            total_deaths+=int(row[4])
            total_recovered+=int(row[5])

        if row[1] == region:
            print(f"{row[0]}: Confirmed Case = {row[3]} Death = {row[4]} Recovered = {row[5]}")
            states.append(row[0])
            confirmed+=int(row[3])
            deaths+=int(row[4])
            recovered+=int(row[5])


print(f"""
{region} ({len(states)} states) REPORT:

CONFIRMED CASES = {confirmed}/{total_confirmed}
DEATHS = {deaths}/{total_deaths}
RECOVERED CASES = {recovered}/{total_recovered}

Last update: {date}
""")


