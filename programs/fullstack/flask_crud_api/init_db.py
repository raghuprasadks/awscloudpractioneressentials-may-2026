# To initialize the database tables, run this script once after updating your DB credentials in app.py
from app import db

db.create_all()
print('Database tables created.')
