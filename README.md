# 🐉 Dragon Age (back-end)

This is the back end part of my project about Dragon Age, the popular fantasy videogame.
I create a server linked to a database where you can add:
- games
- characters
- dlc
- goals

## ⚙️How to install
This project is developed using **Python/Django** and **PostegreSQL** for data storage

1) Clone this repository in your PC and open with you Visual Studio Code
2) Create a new PostgreSQL database
3) Create a file named .env inside the main folder of the project with the follow environment variables and add your personal data:
- SECRET_KEY 
- DEBUG 
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
4) Create an admin:
```bash
python manage.py createsuperuser
```
5) Create migrations:
```bash
python manage.py makemigrations
```
 and
```bash
python manage.py migrate
```
6) Run the project:
```bash
python manage.py runserver
```
7) Import all csv file that you can find inside the folder named **data** in this repository to your database to have all data or add your data using the Django Admin Interface
8) You can use this in a frontend app downloading the following project : https://github.com/NoemiP94/dragon-age


### 🖊️ Author

Noemi Pusceddu 🦋

🧑‍💻 [LinkedIn](https://www.linkedin.com/in/noemi-pusceddu-developer/)

