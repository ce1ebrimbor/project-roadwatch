# project/server/models.py


import datetime

from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from project.server import db

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)


# Api Models
class Accident(db.Model):

    id = db.Column('id', db.Integer(), primary_key=True)
    lum = db.Column('lum', db.Integer())
    agg = db.Column('agg', db.Integer())
    int = db.Column('int', db.Integer())
    atm = db.Column('atm', db.Integer())
    col = db.Column('col', db.Integer())
    adr = db.Column('adr', db.Text())
    comm = db.Column('comm', db.String(5))
    gps = db.Column('gps', db.String(1))
    dep = db.Column('dep', db.String(3), db.ForeignKey('departement.id'))
    lat = db.Column('lat', db.Float())
    long = db.Column('long', db.Float())
    date = db.Column('date', db.DateTime())
    usager = db.relationship('Usager',
                             backref='accident_usager',
                             lazy=True)
    lieu = db.relationship('Lieu',
                           uselist=False,
                           backref='accident_lieu',
                           lazy=True)
    vehicule = db.relationship('Vehicule',
                               backref='accident_vehicule',
                               lazy=True)

    def __init__(self, id, lum, agg, int, atm, col,
                 adr, comm, gps, dep, lat, long, date):
        self.id = id
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
        return '<Accident {0} >'.format(self.id)


class Lieu(db.Model):

    id = db.Column('id', db.Integer(), primary_key=True )
    accident_id = db.Column('accident_id', db.Integer(),
                            db.ForeignKey('accident.id'))
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
    accident = db.relationship('Accident', foreign_keys=accident_id)

    def __init__(self, accident_id, catr, voie, circ, nbv, pr, pr1, vosp,
                 prof, plan, surf, infra, situ):
        self.accident_id = accident_id
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


class Usager(db.Model):

    id = db.Column('id', db.Integer(), primary_key=True)
    accident_id = db.Column('accident_id', db.Integer(),
                            db.ForeignKey('accident.id'))
    place = db.Column('place', db.Integer())
    catu = db.Column('catu', db.Integer())
    grav = db.Column('grav', db.Integer())
    sexe = db.Column('sexe', db.Integer())
    trajet = db.Column('trajet', db.Integer())
    secu = db.Column('secu', db.Integer())
    locp = db.Column('locp', db.Integer())
    actp = db.Column('actp', db.Integer())
    etatp = db.Column('etatp', db.Integer())
    an_nais = db.Column('an_nais', db.Integer())
    num_veh = db.Column('num_veh', db.Text())
    accident = db.relationship('Accident', foreign_keys=accident_id, lazy=True)

    def __init__(self, accident_id, place, catu, grav, sexe, trajet, secu, locp,
                 actp, etatp, an_nais, num_veh):
        self.accident_id = accident_id
        self.place = place
        self.catu = catu
        self.grav = grav
        self.sexe = sexe
        self.trajet = trajet
        self.secu = secu
        self.locp = locp
        self.actp = actp
        self.etatp = etatp
        self.an_nais = an_nais
        self.num_veh = num_veh

    def __repr__(self):
        return '<Usager {0}>'.format(self.id)


class Vehicule(db.Model):

    id = db.Column('id', db.Integer(), primary_key=True)
    accident_id = db.Column('accident_id', db.Integer(),
                            db.ForeignKey('accident.id'))
    senc = db.Column('senc', db.Integer())
    catv = db.Column('catv', db.Integer())
    occutc = db.Column('occutc', db.Integer())
    obs = db.Column('obs', db.Integer())
    obsm = db.Column('obsm', db.Integer())
    choc = db.Column('choc', db.Integer())
    manv = db.Column('manv', db.Integer())
    num_veh = db.Column('num_veh', db.Text())
    accident = db.relationship("Accident", backref='vehicules')

    def __init__(self, accident_id, senc, catv, occutc, obs, obsm, choc,
                 manv, num_veh):
        self.accident_id = accident_id
        self.senc = senc
        self.catv = catv
        self.occutc = occutc
        self.obs = obs
        self.obsm = obsm
        self.choc = choc
        self.manv = manv
        self.num_veh = num_veh

    def __repr__(self):
        return '<Vehicule {0}>'.format(self.id)



class Departement(db.Model):

    id = db.Column('id', db.Text(), primary_key=True)
    geometry = db.Column('geometry', db.Text())
    nom = db.Column('nom', db.Text())
    accident = db.relationship('Accident', backref='departement')

    def __init__(self, id, geometry, nom):
        self.id = id
        self.geometry = geometry
        self.nom = nom
        #accident = db.relationship('Accident', backref=db.backref('departements'))

    def __repr__(self):
        return '<Departement {0}>'.format(self.id)
