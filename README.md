# Инструкция по развертыванию проекта

## Шаг 1: Установка необходимых компонентов

Установите следующие пакеты на сервере:

- Python 3.12
- python3-pip
- python3-dev
- libpq-dev
- PostgreSQL и PostgreSQL-contrib
- Nginx

## Шаг 2: Создание базы данных PostgreSQL

Создайте базу данных PostgreSQL, которая будет использоваться проектом.

## Шаг 3: Клонирование проекта на сервер
<pre>
git clone https://github.com/Ronny884/mxbt789.git
</pre>

## Шаг 4: Установка зависимостей проекта
<pre>
pip install -r requirements.txt
</pre>

## Шаг 5: Активация виртуального окружения и установка Gunicorn
Убедитесь, что виртуальное окружение активировано и установите Gunicorn:
<pre>
source env/bin/activate
pip install gunicorn
</pre>

## Шаг 6: Конфигурация .env файла
В файле конфигурации проекта .env установите необходимые значения для работы базы данных и проекта.

## Шаг 7: Создание файла сокета для Gunicorn
Создайте файл сокета для Gunicorn:
<pre>
sudo nano /etc/systemd/system/gunicorn.socket
</pre>
Содержимое файла:
<pre>
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
</pre>

## Шаг 8: Создание служебного файла systemd для Gunicorn
Создайте служебный файл systemd для Gunicorn:
<pre>
sudo nano /etc/systemd/system/gunicorn.service
</pre>
Содержимое файла:
<pre>
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=user_name # имя юзера для запуска
Group=www-data
WorkingDirectory=/home/user_name/mxbt789
ExecStart=*здесь указывается путь к виртуальному окружению проекта* \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          mxbt789.wsgi:application

[Install]
WantedBy=multi-user.target
</pre>

## Шаг 9: Запуск и активация сокета Gunicorn
Запустите и активируйте сокет Gunicorn:
<pre>
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
</pre>

## Шаг 10: Создание и настройка серверного блока Nginx
Создайте и настройте серверный блок Nginx:
<pre>
sudo nano /etc/nginx/sites-available/mxbt789
</pre>
Содержимое файла:
<pre>
server {
    listen 80;
    server_name *IP-адрес сервера или доменное имя*;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/user_name/mxbt789;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
</pre>

## Шаг 11: Активация файла Nginx
Активируйте файл серверного блока Nginx:
<pre>
sudo ln -s /etc/nginx/sites-available/mxbt789 /etc/nginx/sites-enabled
</pre>

## Шаг 12: Перезапуск Nginx
Перезапустите Nginx:
<pre>
sudo systemctl restart nginx
</pre>

## Шаг 13: Настройка брандмауэра
Разрешите трафик для Nginx:
<pre>
sudo ufw allow 'Nginx Full'
</pre>
Теперь проект должен быть развернут и доступен на сервере.
