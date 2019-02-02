# project/server/models.py
from project.server import db, marshmallow
from sqlalchemy.orm import relationship
from marshmallow_jsonapi.flask import Schema, Relationship 

class Accident(db.Model):

    __tablename__ = 'caracteristiques'

    num_acc = db.Column('num_acc', db.Integer(), primary_key=True)
    lum = db.Column('lum', db.Integer())
    agg = db.Column('agg', db.Integer())
    int = db.Column('int', db.Integer())
    atm = db.Column('atm', db.Integer())
    col = db.Column('col', db.Integer())
    adr = db.Column('adr', db.Text())
    comm = db.Column('comm', db.String(5))
    gps = db.Column('gps', db.String(1))
    dep = db.Column('dep', db.String(3))
    lat = db.Column('lat', db.Float())
    long = db.Column('long', db.Float())
    date = db.Column('date', db.DateTime())
    lieu = relationship("Lieu", uselist=False, back_populates='accident')


    def __init__(self, num_acc, lum, agg, int, atm, col,
                 adr, comm, gps, dep, lat, long, date):
        self.num_acc = num_acc
        self.lum = lum
        self.agg = agg
        self.int = int
        self.atm = atm
        self.col = col
        self.adr = adr
        self.comm = comm
        self.gps = gps
        self.dep = dep
        self.lat = lat
        self.long = long
        self.date = date

    def __repr__(self):
        return '<Accident {0} >'.format(self.num_acc)

class Lieu(db.Model):

    __tablename__ = 'lieux'

    id = db.Column('id', db.Integer(), primary_key=True, autoincrement=True)
    num_acc = db.Column('num_acc', db.Integer(), db.ForeignKey('caracteristiques.num_acc'))
    catr = db.Column('catr', db.Integer())
    voie = db.Column('voie', db.Integer())
    circ = db.Column('circ', db.Integer())
    nbv = db.Column('nbv', db.Integer())
    pr = db.Column('pr', db.Integer())
    pr1 = db.Column('pr1', db.Integer())
    vosp = db.Column('vosp', db.Integer())
    prof = db.Column('prof', db.Integer())
    plan = db.Column('plan', db.Integer())
    surf = db.Column('surf', db.Integer())
    infra = db.Column('infra', db.Integer())
    situ = db.Column('situ', db.Integer())
    accident = db.relationship("Accident", back_populates="lieu")

    def __init__(self, num_acc, catr, voie, circ, nbv, pr, pr1, vosp,
              prof, plan, surf, infra, situ):
        self.num_acc = num_acc
        self.catr = catr
        self.voie = voie
        self.circ = circ
        self.nbv = nbv
        self.pr = pr
        self.pr1 = pr1
        self.vosp = vosp
        self.prof = prof
        self.plan = plan
        self.surf = surf
        self.infra = infra
        self.situ = situ

    def __repr__(self):
        return '<Lieu {0}>'.format(self.id)
