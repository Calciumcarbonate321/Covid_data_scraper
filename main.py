#IMPORTING ALL NECESSARY FILES
import requests
from bs4 import BeautifulSoup
import pandas as pd
import dask.dataframe as dd
import warnings
import csv

user_country=input("Enter your country name: ")
#SCRAPING THE SITE
page=requests.get("https://www.worldometers.info/coronavirus")
soup=BeautifulSoup(page.content, 'lxml')
table=soup.find('table', attrs={'id':'main_table_countries_today'})

rows=table.find_all("tr",arrs={"style":""})
data=[]

rows=table.find_all("tr",attrs={"style":""})
for i,item in enumerate(rows):
    if i == 0:

        data.append(item.text.strip().split("\n")[:13])

    else:
        data.append(item.text.strip().split("\n")[:12])


warnings.simplefilter(action='ignore', category=FutureWarning)
dt = pd.DataFrame(data)
dt = pd.DataFrame(data[1:], columns=data[0][:12])
df = dd.from_pandas(dt,npartitions=1)

df.to_csv('extracted_data*.csv')

data_csv=list(csv.reader('extracted_data0.csv'))
data_file='extracted_data0.csv'
with open(data_file,'r') as covid_database:
    csvfile=csv.reader(covid_database)
    for i in csvfile:
        if user_country in i:
            print("\n")
            print("Total cases reported: ",i[3])
            if i[4]=='':
                print("\n")
                print("Total new cases reported today: 0 ")
            else:
                print("\n")
                print("Total new cases reported today: ",i[4])
            print("\n")
            print("Total deaths reported: ",i[5])
            if i[6]=='':
                print("\n")
                print("Total deaths reported today: 0")
            else:
                print("\n")
                print("Total deaths reported today: ",i[6])
            print("\n")
            print("Total number of people who recovered: ",i[7])
            if i[8]=='':
                print("\n")
                print("Total number of people who recovered today: 0")
            else:
                print("\n")
                print("Total number of people who recovered today: ",i[8])
            print("\n")
            print("Total number of active cases: ",i[9])
            print("\n")
            print("Total number of serious cases: ",i[10])
