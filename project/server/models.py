# project/server/models.py


import datetime

from flask import current_app

from project.server import db, bcrypt

class Accident(db.Model):

    __tablename__ = "caracteristiques"

    id = db.Column(db.Integer, primary_key=True)
    lum = db.Column(db.Integer)
    agg = db.Column(db.Integer)
    int = db.Column(db.Integer)
    atm = db.Column(db.Integer)
    adr = db.Column(db.Text)
    comm = db.Column(db.String(5))
    dep = db.Column(db.String(3))
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    date = db.Column(db.DateTime)


    def __init__(self, id, lum, agg, int, atm, adr, comm, dep, lat, long, date):
        self.id = id
        self.lum = lum
        self.agg = agg
        self.int = int
        self.atm = atm
        self.adr = adr
        self.comm = comm
        self.dep = dep
        self.lat = lat
        self.long = long
        self.date = date

    def __repr__(self):
        return '<Accident {0} >'.format(self.id)
