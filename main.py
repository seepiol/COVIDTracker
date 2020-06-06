# COVIDTracker, 2020
# Simple CLI tool written in python to track the spreading of the SARS-CoV-2 outbreak


import requests
import sys
import json

spec_data_source = ["Italy"]

print("\033[91m\033[1m== ☣ COVID-19 - SARS-CoV-2 Italy Spread Tracker ☣ ==\033[0m")
print("\nFetching latest data.....", end="")

#### ITALIAN DATA
# The procedure to get italian data is more simple. The daily repost is saved on a .json file. All the daily data are
# saved in the same file, so it's enough to get the json file and convert it in a dict with the json module.

it_json_url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json"
it_json = json.loads(requests.get(it_json_url).text)
it_current_data = it_json[len(it_json)-1]

print(" OK \n")

region = "Italy"

if region == "Italy":
    print(f"""
====================================================
\033[0;31m\033[1m☣ COVID-19 ☣\033[0m
ITALY REPORT

🛑 \033[94m\033[1mTOTAL CONFIRMED CASES = {it_current_data.get("totale_casi")}\033[0m
➕ \033[94m\033[1mTODAY NEW CASES = {it_current_data.get("nuovi_positivi")}\033[0m
🌡  \033[0;36m\033[1mTOTAL CURRENT INFECTED CASES = {it_current_data.get("terapia_intensiva")+it_current_data.get("totale_ospedalizzati")+it_current_data.get("isolamento_domiciliare")}\033[0m
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

print(
    """
More information about the SARS-CoV-2 outbreak and COVID-19 disease here: 
\033[4mhttps://github.com/seepiol/COVIDTracker#about-covid-19\033[0m

Data sources:
Italy: \033[4mhttps://github.com/pcm-dpc/COVID-19\033[0m
"""
)
