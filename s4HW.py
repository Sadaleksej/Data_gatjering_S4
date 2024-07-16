import requests
from lxml import html
import pandas as pd
import csv


resp = requests.get(url = "https://www.sports.ru/hockey/tournament/nhl/table/", headers = {
    "User_Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) C7hrome/126.0.0.0 Safari/537.36'
    })

tree = html.fromstring(html = resp._content)
print(resp.status_code)


rows = tree.xpath("//table[@class='stat-table']/tbody/tr")

list_data = []
for ite in rows:
    try:
        columns = ite.xpath(".//td/text()")
        list_data.append({
            '№':columns[0].strip(), 
            'Команда': ite.xpath(".//td[2]/div/a/text()")[0].strip(),
            'Матчей сыграно':columns[1].strip(),
            'Выиграно': columns[2].strip(),
            'Выиграно в овертайме':columns[3].strip(),
            'Проиграно':columns[4].strip(),
            'Проиграно в овертайме': columns[5].strip(),
            'Очков': columns[6].strip(),
            'Забитые шайбы':columns[7].strip(),
            'Пропущенные шайбы':columns[8].strip(),
            'Разница шайб':ite.xpath(".//td[11]/span/text()")[0].strip(),
            })
    except:
        print('Парсинг закончился с ошибкой!')


df = pd.DataFrame(list_data)
print(df)

df.to_csv('file_result.csv')