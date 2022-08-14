from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
import os
outfile = '../data/news.csv'

if os.path.isfile(outfile):
    os.remove(outfile)

root = f'https://google.com/'
f'{root}search?q=occidental%20petroleum%20when%3A1d&hl=en-US&gl=US&ceid=US%3Aen'
endpoint = f'{root}search?q=occidental+petroleum&tbm=nws&sxsrf=ALiCzsYwB53AiHTT2X2PwZ0ZtYdMDfVDTA:1660497166127&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwjK7_L96cb5AhXhkWoFHS6tBjIQpwV6BAgBEBY&biw=1920&bih=947&dpr=1'

rs = Request(endpoint, headers = {'User-Agent': "Mozilla/5.0"})

webpage = urlopen(rs).read()

data = []

with requests.Session() as c:
    soup = BS(webpage, 'html5lib')
    soup is None
    items = soup.find_all('div',attrs={'class':'Gx5Zad fP1Qef xpd EtOod pkphOe'})
    for item in items:
        raw_link =item.find('a', href=True)['href']
        link = raw_link.split("/url?q=")[1]
        if link.__contains__('&sa=U&'):
            link = link.split('&sa=U&')[0]
            
        description_chunk = item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).get_text().split(".")
        
        row = {'title': item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).get_text(),
               'description': description_chunk[0],
               'link': link,
               'time': description_chunk[1]}
        
        data.append(row)

data = pd.DataFrame(data)
data.to_csv(path_or_buf=outfile)





