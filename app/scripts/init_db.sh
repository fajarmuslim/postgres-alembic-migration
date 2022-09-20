set -a
. .env
alembic revision --autogenerate -m "feat: input table and output table"
alembic upgrade head
set +a