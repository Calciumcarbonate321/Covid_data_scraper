import requests
from bs4 import BeautifulSoup
import pandas as pd
import dask.dataframe as dd
import warnings

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

df.to_csv('./Extracted_data/data-*.csv')
#simply
