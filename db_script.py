import json
import requests
import os
import time
import sqlite3

# создание бдшки
conn = sqlite3.connect('vacancies.db')
cur = conn.cursor()
# создание таблицы и параметры, при повторе лишь будет проверять ее на корректность
cur.execute("""CREATE TABLE IF NOT EXISTS vacanci(
    id TEXT PRIMARY KEY,
    salary_from INT,
    salary_to INT,
    name TEXT,
    area TEXT);""")
conn.commit()

#цикл для прохода по страницам
for fl in os.listdir('./docs/pagination'):
    f = open('./docs/pagination/{}'.format(fl), encoding='utf8')
    jsonText = f.read()
    f.close()

    jsonObj = json.loads(jsonText)

    #цикл для обработки вакансий и заполнение бд там можно делать
    for v in jsonObj['items']:
        req = requests.get(v['url'])
        data = req.content.decode(encoding='utf8')
        req.close()

        # Заполнение бд из файла страниц, вакансиями, осталось их сортировать, гоподи, ее боиии
        # vacancie = (str(v['id']),str(v['salary']['from']),
        #             str(v['salary']['to']),str(v['name']),str(v['area']))
        #
        # cur.execute("INSERT INTO vacanci VALUES(?,?,?,?,?);", vacancie)
        # conn.commit()

        time.sleep(0.25)

    # cur.execute("SELECT * FROM vacanci;") #проверка заполнилась ли бд, ее бои, оно заполнилось
    # one_result = cur.fetchall()
    # print(one_result)

    # находит максимальную зарплату в базе
    # cur.execute("SELECT MAX((salary_to+salary_from) / 2) FROM vacanci WHERE salary_to NOT like 'None' AND salary_from NOT like 'None';")
    # result = cur.fetchall()
    # print(result)

    # находит максимальную зарплату в базе
    # cur.execute("SELECT MIN((salary_to+salary_from) / 2) FROM vacanci WHERE salary_to NOT like 'None' AND salary_from NOT like 'None';")
    # result = cur.fetchall()
    # print(result)

    # находит среднюю зарплату в базе
    # cur.execute("SELECT AVG((salary_to+salary_from) / 2) FROM vacanci WHERE salary_to NOT like 'None' AND salary_from NOT like 'None';")
    # result = cur.fetchall()
    # print(result)
