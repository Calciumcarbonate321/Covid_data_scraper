def data_obtaining(user_country):
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import dask.dataframe as dd
    import warnings
    import csv

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
        data_csv=list(csv.reader('extracted_data0.csv'))
        data_file='extracted_data0.csv'
        with open(data_file,'r') as covid_database:
            csvfile=csv.reader(covid_database)
            for i in csvfile:
                if user_country in i:
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
        return cases_reported
        return cases_reported_today
        return total_deaths
        return total_deaths_today
        return total_recovered
        return total_recovered_today
        return total_active_cases
        return total_serious_cases
