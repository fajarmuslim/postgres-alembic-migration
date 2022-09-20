# Alembic Migration on Postgres

## Spesification
1. Programming language: Python
2. Docker installed


## Prerequisite
1. Install poetry
2. Create database, this can be done with docker </br>
Example: 
```bash
docker run -d \
-p 5432:5432 \
--name iris-db \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=postgres \
-e POSTGRES_DB=iris \
postgres
```

* `-d` means run container on detached mode
* `-p` means port
* `--name` means container name
* `-e` means set environment

## How to Run
1. Create virtual environment with python
```bash
python3 -m venv venv
```
2. Create `.env` file, the example can be found on `.env-example` file. Make sure that you have same variable with your actual postgres db 
3. Change directory into `app`
```bash
cd app
```
4. Run db migration
```bash
./scripts/test.sh
```