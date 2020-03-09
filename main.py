# COVIDTracker, 2020
# Simple CLI tool written in python to track the spreading of the SARS-CoV-2 outbreak

import csv
import datetime
import requests
import sys
import json

spec_data_source = ["Italy"]

print("\033[91m\033[1m== ☣ COVID-19 - SARS-CoV-2 Spread Tracker ☣ ==\033[0m")
print("\nFetching latest data.....", end="")

#### INTERNATIONAL DATA
# the JHU CSSE doesn't provide an official REST API; They upload once a day the situation on github, each day in a
# different file. Because the filename is the current date, this program get the current and request the currentdate.csv
# file. if the http response isn't 200, we assume that the current day file isn't available yet, and we try to decrease
# the currentdate to fetch the last available file. The program save the file in a local .csv file

i = 0
date = datetime.date.today()
date = date.strftime("%m-%d-%Y")
url = (
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
    + date
    + ".csv"
)
daily_report = requests.get(url)
while daily_report.status_code != 200:
    i += 1
    date = datetime.date.today() - datetime.timedelta(i)
    date = date.strftime("%m-%d-%Y")
    url = (
        "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
        + date
        + ".csv"
    )
    daily_report = requests.get(url)

with open("covid.csv", "w") as file:
    file.write(str(daily_report.content.decode("ascii")))


#### ITALIAN DATA
# The procedure to get italian data is more simple. The daily repost is saved on a .json file. All the daily data are
# saved in the same file, so it's enough to get the json file and convert it in a dict with the json module.

it_json_url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json"
it_json = json.loads(requests.get(it_json_url).text)
it_current_data = it_json[len(it_json)-1]

print(" OK \n")

if len(sys.argv) > 1 :
    region = sys.argv[1].title()
    print(f"Selected {region}")
else:
    region = input("Insert country or region (world for all): ").title()

if len(region) == 2:
    region = region.upper()
if region == "*":
    region = True

total_confirmed = 0
total_deaths = 0
total_recovered = 0

states = []
confirmed = 0
deaths = 0
recovered = 0

with open("covid.csv") as daily_report:
    parsed_daily_report = csv.reader(daily_report, delimiter=",")
    for row in parsed_daily_report:
        if region == "Italy":
            break
        elif (region.lower() in row[0].lower() or region.lower() in row[1].lower() or region == "World"):
            if row[0] == "Province/State":
                pass
            else:
                states.append(row[0])
                confirmed += int(row[3])
                deaths += int(row[4])
                recovered += int(row[5])



if region == "Italy":
    print(f"""
====================================================
\033[0;31m\033[1m☣ COVID-19 ☣\033[0m
ITALY REPORT

🛑 \033[94m\033[1mTOTAL CONFIRMED CASES = {it_current_data.get("totale_casi")}\033[0m
➕ \033[94m\033[1mTODAY NEW CASES = {it_current_data.get("nuovi_attualmente_positivi")}\033[0m
🌡  \033[0;36m\033[1mTOTAL CURRENT INFECTED CASES = {it_current_data.get("totale_attualmente_positivi")}\033[0m
🔬 \033[1;36m\033[1mCURRENT INFECTED CASES IN ICU* = {it_current_data.get("terapia_intensiva")}\033[0m
🏥 \033[1;36m\033[1mCURRENT INFECTED CASES HOSPITALISED = {it_current_data.get("totale_ospedalizzati")}\033[0m
🏠 \033[1;36m\033[1mCURRENT INFECTED CASES IN HOME ISOLATION = {it_current_data.get("isolamento_domiciliare")}\033[0m
🧫 \033[0;33m\033[1mUSED TESTS KIT = {it_current_data.get("tamponi")}\033[0m
💀 \033[0;31m\033[1mDEATHS = {it_current_data.get("deceduti")}\033[0m
✅ \033[92m\033[1mRECOVERED CASES = {it_current_data.get("dimessi_guariti")}\033[0m

ICU: intensive care
Last update: {it_current_data.get("data")}
====================================================
""")

else:
    print(
    f"""
====================================================
\033[0;31m\033[1m☣ COVID-19 ☣\033[0m
{region.upper()} REPORT
({len(states)} states)
🛑 \033[94m\033[1mCONFIRMED CASES = {confirmed}\033[0m
💀 \033[0;31m\033[1mDEATHS = {deaths}\033[0m
✅ \033[92m\033[1mRECOVERED CASES = {recovered}\033[0m

Last update: {date}
====================================================
"""
)



print(
    """
More information about the SARS-CoV-2 outbreak and COVID-19 disease here: 
\033[4mhttps://github.com/seepiol/COVIDTracker#about-covid-19\033[0m

Data sources:
World: \033[4mhttps://github.com/CSSEGISandData/COVID-19\033[0m
Italy: \033[4mhttps://github.com/pcm-dpc/COVID-19\033[0m
"""
)
