import os
import psycopg2
from app import create_app
from app.database.database import *
from config import app_config

app = create_app('DEFAULT')

"""Set your development database credentials"""

db = Database(app_config['DEFAULT'].DATABASE_URL)

if __name__ == '__main__':
    db.create_tables()
    app.run()
