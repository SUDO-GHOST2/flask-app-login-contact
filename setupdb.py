from app import app, db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()
    if not User.query.filter_by(email="admin@example.com").first():
        hashed = generate_password_hash("123456")
        db.session.add(User(email="admin@example.com", password=hashed))
        db.session.commit()
        print("[✔] User created: admin@example.com / 123456")
    else:
        print("[i] User already exists.")
