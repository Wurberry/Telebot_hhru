import json
import requests
import os
import time
import sqlite3

#открываем файл со страницами и каждую обрабатываем циклом на вытаскивание вакансий
for fl in os.listdir('./docs/pagination'):
    f = open('./docs/pagination/{}'.format(fl), encoding='utf8')
    jsonText = f.read()
    f.close()

    jsonObj = json.loads(jsonText)

    # цикл вытаскивающий вакансии из страниц
    for v in jsonObj['items']:
        req = requests.get(v['url'])
        data = req.content.decode(encoding='utf8')
        req.close()

        #заполнение файла вакансиями
        fileName = './docs/vacancies/{}.json'.format(v['id'])
        f = open(fileName, mode='w', encoding='utf8')
        f.write(data)
        f.close()

        time.sleep(0.25)
