#### Реализованная функциональность
* Ищет полярных медведей аэрофотосъемке
* Интерфейс реализован в качестве telegram-бота
#### Основной стек технологий
* Python
* OpenCV, Telethon 
* Git, Github
#### Демо
Telegram-бот [@bearfindbot](https://t.me/bearfindbot)
#### Среда запуска
* Развертывание сервиса производится на debian-like linux (debian 9+) / windows 7 и выше
* Для установки требуется python 3.6+ и пакетный менеджер pip (в случае с linux)
#### Установка и запуск своего бота (не обязательно)
1. Скачайте проект и распакуйте его
2. Перейдите в папку с проектом и активируйте среду venv
	##### Windows:
	~~~
	cd path/to/project
	python3 -m venv venv
	venv\Scripts\activate.bat
	~~~
	##### Linux:
	~~~
	cd path/to/project
	python3 -m venv venv
	source venv/bin/activate
	~~~
4. Установите зависимости
	~~~
	pip install -r requirements.txt
	~~~
5. В файле bot_setings.py укажите настройки бота


	Перейдите на https://my.telegram.org, войдите в свой аккаунт. Создайте приложение (app), если оно не создано и запишите в app_id и app_hash (в файле bot_setings.py) значения из сайта соответственно. Далее зайдите в [@BotFather](https://t.me/BotFather), напишите /start -> /newbot и создайте бота по инструкции. В конце регистрации бота вы получите токен бота, вставьте его в файле в значение bot_token

6. Запустите файл с ботом
	~~~
	python main.py
	~~~
