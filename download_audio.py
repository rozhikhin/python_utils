import requests
import time
import os
import datetime
from bs4 import BeautifulSoup


# Создание базового каталога.
base_dir = r'\\server\AudioRecords'
# Созддание каталога с текущей датой
today_dir_name = datetime.date.today().strftime('%d-%m-%Y')
# Полный путь к файлу
ful_path = os.path.join(base_dir, today_dir_name)

# Создаем каталог
try:
    os.mkdir(ful_path)
except OSError:
    print ("Creation of the directory %s failed" % ful_path)
else:
    print ("Successfully created the directory %s " % ful_path)

# Ссылка на профиль и данные для авторизации
base_url = (r'http://voice.agtel.net/79998877/')
username = 79998877
password = 'sj6CP3X3'

# создает объект для авторизации
basicAuthCredentials = (username, password)

# Отправляем запрос и авторизуемся
response = requests.get(base_url, auth=basicAuthCredentials)

# If the HTTP GET request can be served
if response.status_code == 200:
    # print(response.text)
    # парсим html
    soup = BeautifulSoup(response.text, 'html.parser')
    # Находим все строки в таблице
    trs = soup.find(class_ = 'DirTable').findAll('tr')

    for tr in trs:
        time.sleep(1)
        # Находим сылки
        a = tr.find('td').find('a')
        if a:
            # Получаем полную ссылку
            download_url = base_url + a['href']
            file_name = os.path.join(ful_path, a.text)
            print(download_url)
            print(file_name)

            r = requests.get(download_url, stream=True, auth=basicAuthCredentials)
            # Скачиваем файл
            with open(file_name, 'wb') as f:
                f.write(r.content)
