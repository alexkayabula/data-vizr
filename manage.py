from app import create_app
from config import app_config
from app.database.database import Database

app = create_app('PRODUCTION')

db = Database(app_config['PRODUCTION'].DATABASE_URL)

if __name__ == '__main__':
    db.create_tables()
    app.run()
