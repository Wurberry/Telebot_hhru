import json
import requests
import os
import time
import sqlite3

# метод получения страниц с необходимым нам фильтром
def getPage(page = 0):
    params = dict(text='1C',area=44,only_with_salary='true', page = page, per_page = 10)
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode(encoding='UTF8')
    req.close()
    return data

#в цикле получаем страницы и записываем их в файлы, в папку для страниц
for page in range(0, 20):
    jsObj = json.loads(getPage(page))
    nextFileName = './docs/pagination/{}.json'.format(len(os.listdir(('./docs/pagination'))))
    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(jsObj, ensure_ascii=False))
    f.close()

    if(jsObj['pages'] - page) <= 1:
        break

    time.sleep(0.25)
