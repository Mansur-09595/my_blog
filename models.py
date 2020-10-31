from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    __tablename__ = "qwer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    mail = db.Column(db.String, nullable=False)
    commen = db.Column(db.String, nullable=False)

class Passenger(db.Model):
    __tablename__ = "asdf"
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("qwer.id"), nullable=False)