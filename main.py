#IMPORTING ALL NECESSARY FILES
#coding=utf8
import requests
from bs4 import BeautifulSoup
import pandas as pd
import dask.dataframe as dd
import warnings
import csv
import tkinter as tk
from tkinter import ttk


cases_reported=0
cases_reported_today=0
total_deaths=0
total_deaths_today=0
total_recovered=0
total_recovered_today=0
total_active_cases=0
total_serious_cases=0



#INTROFUCTION IN THE GUI
gui_window=tk.Tk()
gui_window.title('Covid data scraper')
gui_window.geometry("420x420")
intro=tk.Label(text='COVID DATA SCRAPER')
intro.place(relx=0.5,
            rely=0.05,
            anchor="center"
)

casesreported=tk.StringVar()
casesreportedtoday=tk.StringVar()
deaths=tk.StringVar()
deathstoday=tk.StringVar()
recovered=tk.StringVar()
recoveredtoday=tk.StringVar()
active=tk.StringVar()
serious=tk.StringVar()

introduction=tk.Label(gui_window,text='This software is used to get the Covid-19 staticstics of your country.')
introduction.place(relx=0.5,
                   rely=0.1,
                   anchor="center"
)

info=tk.Label(text='Please select your country from the drop box given below:')
info.place(relx=0.75,
           rely=0.25,
           anchor="ne",
)

value=tk.StringVar()
user_countr=ttk.Combobox(
                  gui_window,
                  width=27,
                  textvariable=value
)

user_countr['values']=('Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Bulgaria', 'Burkina Faso', 'Burundi', 'CAR', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Caribbean Netherlands', 'Cayman Islands', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'CuraÃ§ao', 'Cyprus', 'Czechia', 'DRC', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faeroe Islands', 'Falkland Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Grenada', 'Guadeloupe', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'RÃ©union', 'S. Korea', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Barth', 'St. Vincent Grenadines', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turks and Caicos', 'UAE', 'UK', 'USA', 'Uganda', 'Ukraine', 'Uruguay', 'Uzbekistan', 'Vatican City', 'Venezuela', 'Vietnam', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe')

user_countr.place(
                   relx=0.46,
                   rely=0.3,
                   anchor="ne"
)




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


def data_obtaining():
    user_country=user_countr.get()
    data_csv=list(csv.reader('extracted_data0.csv'))
    data_file='extracted_data0.csv'
    with open(data_file,'r') as covid_database:
        csvfile=csv.reader(covid_database)
        for i in csvfile:
            if i[2]==user_country:
                cases_reported=i[3]
                if i[4]=='':
                    cases_reported_today=0
                else:
                    cases_reported_today=i[4]
                total_deaths=i[5]
                if i[6]=='':
                    total_deaths_today=0
                else:
                    total_deaths_today=i[6]
                total_recovered=i[7]
                if i[8]=='':
                    total_recovered_today=0
                else:
                    total_recovered_today=i[8]
                total_active_cases=i[9]
                total_serious_cases=i[10]


                cases_reported="Total cases reported: "+str(cases_reported)
                cases_reported_today="Total cases reported today: "+str(cases_reported_today)
                total_deaths="Total deaths: "+str(total_deaths)
                total_deaths_today="Total deaths today: "+str(total_deaths_today)
                total_recovered="Total recovered: "+str(total_recovered)
                total_recovered_today="Total recovered today: "+str(total_recovered_today)
                total_active_cases="Total active cases: "+str(total_active_cases)
                total_serious_cases="Total serious cases: "+str(total_serious_cases)

                casesreported.set(cases_reported)

                casesreportedtoday.set(cases_reported_today)

                deaths.set(total_deaths)

                deathstoday.set(total_deaths_today)

                recovered.set(total_recovered)

                recoveredtoday.set(total_recovered_today)

                active.set(total_active_cases)

                serious.set(total_serious_cases)
            else:
                pass
    gui_window.update()


#PRINTING THE DATA IN THE GUI


casesreported_l=tk.Label(textvariable=casesreported)
casesreported_l.place(relx=0.5,rely=0.50,anchor="ne")

casesreportedtoday_l=tk.Label(textvariable=casesreportedtoday)
casesreportedtoday_l.place(relx=0.5,rely=0.55,anchor="ne")

deaths_l=tk.Label(textvariable=deaths)
deaths_l.place(relx=0.5,rely=0.60,anchor="ne")

deathstoday_l=tk.Label(textvariable=deathstoday)
deathstoday_l.place(relx=0.5,rely=0.65,anchor="ne")

recovered_l=tk.Label(textvariable=recovered)
recovered_l.place(relx=0.5,rely=0.70,anchor="ne")

recoveredtoday_l=tk.Label(textvariable=recoveredtoday)
recoveredtoday_l.place(relx=0.5,rely=0.75,anchor="ne")

active_l=tk.Label(textvariable=active)
active_l.place(relx=0.5,rely=0.80,anchor="ne")

serious_l=tk.Label(textvariable=serious)
serious_l.place(relx=0.5,rely=0.85,anchor="ne")


btn=tk.Button(text = 'Submit',
                  command = data_obtaining)
btn.place(relx=0.5,
          rely=0.98,
          anchor="center"
)


gui_window.mainloop()
