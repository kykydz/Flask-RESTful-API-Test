from app import app
from db import db

db.init_app(app)

#flask decorator
@app.before_first_request
def create_table():
    db.create_all() #call SQLAlchemy function to create table and database that SQLAlchemy see in models