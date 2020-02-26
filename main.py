import csv
import datetime
import requests
import time
from bs4 import BeautifulSoup
import re

print("\033[91m\033[1m== ☣ COVID-19 - SARS-CoV-2 Spread Tracker ☣ ==\033[0m")
print("\nFetching latest data.....", end="")

# INTERNATIONAL DATA
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

# ITALIAN DATA
it_url = "http://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?lingua=italiano&id=5351&area=nuovoCoronavirus&menu=vuoto"
it_gov_page = BeautifulSoup(requests.get(it_url).text, features="html5lib")
numbers = str(it_gov_page.findAll("div", {"class": "col-lg-4 col-md-12 col-sm-12"}))
datas = re.findall(">\d*<", numbers)
it_confirmed = datas[0][1:-1]
it_deaths = datas[1][1:-1]
it_recovered = datas[2][1:-1]


print(" OK \n")


region = input("Insert country or region (world for all): ").title()
print("\n")

if len(region)==2:
    region=region.upper()
if region == '*':
    region = True

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

        if region.lower() in row[0].lower() or region.lower() in row[1].lower() or region == "World":
            if row[0] == "Province/State":
                pass
            elif row[1] == "Italy":
                print("Using italian official real-time data)
                print(f"- {row[0]}, {row[1]}: Confirmed Case = {row[3]} Death = {row[4]} Recovered = {row[5]}")
                states.append(row[0])
                confirmed += int(it_confirmed)
                deaths += int(it_deaths)
                recovered += int(it_recovered)
                time.sleep(0.05)
            else:
                print(f"- {row[0]}, {row[1]}: Confirmed Case = {row[3]} Death = {row[4]} Recovered = {row[5]}")
                states.append(row[0])
                confirmed+=int(row[3])
                deaths+=int(row[4])
                recovered+=int(row[5])
                time.sleep(0.05)


print(f"""


================================
\t\033[91m\033[1m☣ COVID-19 ☣\033[0m
\t{region.upper()} REPORT
\t({len(states)} states)

🛑 \033[94m\033[1mCONFIRMED CASES = {confirmed}/{total_confirmed}\033[0m
💀 \033[91m\033[1mDEATHS = {deaths}/{total_deaths}\033[0m
✅ \033[92m\033[1mRECOVERED CASES = {recovered}/{total_recovered}\033[0m

   Last update: {date}
================================

""")

print_info = input("Do you want to display some coronavirus information? <y/n>: ")
if print_info.lower() in ['y', 'yes']:
    print("""
- About \033[91m\033[1mCOVID-19\033[0m

Coronavirus disease 2019 (COVID-19), formerly known as 2019-nCoV acute respiratory disease, is an infectious disease 
caused by SARS-CoV-2.

The disease is the cause of the 2019-2020 Coronavirus outbreak.
 
It is primarily spread between people via respiratory droplets from infected individuals when they cough or sneeze. 

Time from exposure to onset of symptoms is generally between 2 and 14 days.

Spread can be limited by handwashing and other hygiene measures.


- About \033[91m\033[1mSARS-CoV-2\033[0m

Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), formerly known as the 2019 novel coronavirus (2019-nCoV), 
is a positive-sense single-stranded RNA virus It is contagious among humans and is the cause 
of Coronavirus disease (COVID-19).


- About \033[91m\033[1m2019-2020 Coronavirus Outbreak\033[0m

The 2019-20 coronavirus outbreak is an ongoing epidemic of Coronavirus disease (COVID-19) caused by SARS-CoV-2, 
which started in December 2019. It was first identified in Whuan, capital of Hubei, province of China, 
after 41 people presented with pneumonia of no clear cause. 

- \033[91m\033[1mWHAT SHOULD I DO IF I HAVE COVID-19 SYMPTOMS?\033[0m
\033[1mCDC (Centers for Disease Control and Prevention) says:
If you are sick with COVID-19 or suspect you are infected with the virus that causes COVID-19, 
follow the steps below to help prevent the disease from spreading to people in your home and community.

- Stay home except to get medical care
- Separate yourself from other people and animals in your home
- Call ahead before visiting your doctor
- Wear a facemask
- Cover your coughs and sneezes
- Clean your hands often
- Avoid sharing personal household items
- Clean all “high-touch” surfaces everyday
- Monitor your symptoms
- Discontinuing home isolation

Full post: \033[4mhttps://www.cdc.gov/coronavirus/2019-ncov/about/steps-when-sick.html\033[0m

\033[0m

For a resource list, visit \033[4m https://github.com/seepiol/COVIDTracker/blob/master/README.md\033[0m

    """)

print("""
Data source: 
World: \033[4mhttps://github.com/CSSEGISandData/COVID-19\033[0m
Italy: \033[4mhttps://bit.ly/2PsV33c\033[0m
""")



