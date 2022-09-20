set -a
. .env
alembic upgrade head
set +a