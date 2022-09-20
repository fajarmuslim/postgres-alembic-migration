# Alembic Migration on Postgres

Hi, in this repo you will learn about how to setup alembic migrations in postgres. You may jump into `app` folder and take a look on README.md file there to be able to run alembic migrations on postgres database

## Folder Structure
 
<img width="438" alt="Screen Shot 2022-09-20 at 07 15 46" src="https://user-images.githubusercontent.com/42022311/191140955-ec287ad1-d8e7-4179-b757-687d81adb168.png">

* `alembic` -> migrations located here
* `db` -> defined base class for table in db
* `models` -> defined table here
* `scripts` -> sh file to run migration