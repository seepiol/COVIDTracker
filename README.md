# COVID TRACKER

MOVED TO GITLAB (https://gitlab.com/seepiol/covidtracker) 

Simple COVID-19 tracker written in python3. 

![COVIDTracker](https://user-images.githubusercontent.com/60071372/75629114-91318e00-5bdf-11ea-8907-626c48308853.gif)

## Data Sources

The italian data are fetched from the Italian Civil Protection (Presidenza del Consiglio dei Ministri - Dipartimento della Protezione Civile) [github repository](https://github.com/pcm-dpc/COVID-19) and there are more accurate information like the collocation of the infected etc.

## About COVID-19

For more information about the COVID-19, SARS-CoV-2 and 2019-2020 Coronavirus Outbreak:

1. [WHO](https://www.who.int/emergencies/diseases/novel-coronavirus-2019)
2. [CDC](https://www.cdc.gov/coronavirus/2019-nCoV/)
3. [ECDC](https://www.ecdc.europa.eu/en/novel-coronavirus-china)
4. [CCDC](http://www.chinacdc.cn/en/COVID19/)
5. [CDC Communication Resources](https://www.cdc.gov/coronavirus/2019-ncov/communication/index.html)
6. [COVID-19 Global Cases by Johns Hopkins CSSE](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
7. [IT] [Italian minister of health](http://www.salute.gov.it/nuovocoronavirus)

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

if you have windows, click the ["Download zip button"](https://github.com/seepiol/COVIDTracker/archive/master.zip)

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
python3 main.py
```

the italian data will be displayed

**Thanks to Dipartimento della Protezione Civile for the data publication**
