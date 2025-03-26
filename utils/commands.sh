uvicorn app.api.main:app --reload
uvicorn app.main:app --reload

source venv/bin/activate

python -m app.db.init
python -m app.db.seed

alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

flutter --version flutter config --enable-macos-desktop 
flutter create frontend_pwa 
cd frontend_pwa 
flutter pub add http 
flutter devices 
flutter run -d chrome
flutter run #Hot reload
