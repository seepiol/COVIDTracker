# COVID TRACKER
Simple COVID-19 tracker written in python.


## How To Install
### Install GIT
if you have a debian-based distro
```
sudo apt install git
```
if you have an arch-based distro
```
sudo pamac install git
```

if you have windows (why?), click the ["Download zip button"](https://github.com/seepiol/COVIDTracker/archive/master.zip)

### Install Dependencies
Extract the files from master.zip and open your terminal (or the command prompt) into the "master" folder.
Verify to be in the right directory, and type
```
pip install -r requirements.txt
```
This will install all the python modules that the program need

## Run The Program
In the same folder, type
```
python main.py
```
insert the contry that you want and view the spreading data.

If you want to write the country as a cli argument, type for example
```
python3 main.py iran
```


## About COVID-19

For more information about the COVID-19, SARS-CoV-2 and 2019-2020 Coronavirus Outbreak:
1. [WHO](https://www.who.int/emergencies/diseases/novel-coronavirus-2019)
2. [CDC](https://www.cdc.gov/coronavirus/2019-nCoV/)
3. [ECDC](https://www.ecdc.europa.eu/en/novel-coronavirus-china)
4. [CCDC](http://www.chinacdc.cn/en/COVID19/)
5. [CDC Communication Resources](https://www.cdc.gov/coronavirus/2019-ncov/communication/index.html)
6. [COVID-19 Global Cases by Johns Hopkins CSSE](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
7. [IT] [Italian minister of health](http://www.salute.gov.it/nuovocoronavirus)

## Data Sources
The data fetching process is different from country to country.
Generally the data are obtained through the CSV files posted daily on github by John Hopkins University
The italian data are fetched by the Italian department of health by web scraping

When the world situation is selected, all the data, included the italian, come from the JHU repo.

In this way, the world and all the other countries' data are updated daily, while the italian statistics are updated twice a day (11AM and 5PM UTC).


World: JHU CSSE [github repository](https://github.com/CSSEGISandData/COVID-19) daily report <br />
Italy: Italian minister of health [official situation](https://bit.ly/2PsV33c)