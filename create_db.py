from my_flask_app import app, db
from models import Item

with app.app_context():
    db.drop_all()
    db.create_all()
