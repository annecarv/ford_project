uvicorn app.api.main:app --reload
uvicorn app.main:app --reload

source venv/bin/activate
python -m app.db.init
python -m app.db.seed

alembic init alembic
