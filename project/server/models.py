# project/server/models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound

from flask_rest_jsonapi import ResourceDetail, ResourceList
from flask_rest_jsonapi import ResourceRelationship
from flask_rest_jsonapi.exceptions import ObjectNotFound

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

db = SQLAlchemy()


# Database Models
class Accident(db.Model):

    __tablename__ = 'caracteristiques'

    id = db.Column('id', db.Integer(), primary_key=True)
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
    usager = db.relationship('Usager', backref='caracteristiques', lazy=True)

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

    __tablename__ = 'lieux'

    id = db.Column('id', db.Integer(), primary_key=True, autoincrement=True)
    accident_id = db.Column('accident_id', db.Integer(),
                            db.ForeignKey('caracteristiques.id'))
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

    __tablename__ = 'usagers'

    id = db.Column('id', db.Integer(), primary_key=True, autoincrement=True)
    accident_id = db.Column('accident_id', db.Integer(),
                            db.ForeignKey('caracteristiques.id'))
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

    __tablename__ = 'vehicules'

    id = db.Column('id', db.Integer(), primary_key=True, autoincrement=True)
    accident_id = db.Column('accident_id', db.Integer(),
                            db.ForeignKey('caracteristiques.id'))
    senc = db.Column('senc', db.Integer())
    catv = db.Column('catv', db.Integer())
    occutc = db.Column('occutc', db.Integer())
    obs = db.Column('obs', db.Integer())
    obsm = db.Column('obsm', db.Integer())
    choc = db.Column('choc', db.Integer())
    manv = db.Column('manv', db.Integer())
    num_veh = db.Column('num_veh', db.Text())
    accident = db.relationship("Accident", backref=db.backref('vehicules'))

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


# Logical Data abstraction
class AccidentSchema(Schema):
    class Meta:
        type_ = 'accident'
        self_view = 'accident_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'accident_list'

    id = fields.Integer(as_String=True, dump_only=True)
    lum = fields.Integer(as_String=True)
    agg = fields.Integer(as_String=True)
    int = fields.Integer(as_String=True)
    atm = fields.Integer(as_String=True)
    col = fields.Integer(as_String=True)
    adr = fields.Str()
    comm = fields.Str()
    gps = fields.Str()
    dep = fields.Str()
    lat = fields.Float(as_String=True)
    long = fields.Float(as_String=True)
    date = fields.Date()
    usager = Relationship(self_view='accident_usagers',
                          self_view_kwargs={'id': '<id>'},
                          related_view='usager_list',
                          related_view_kwargs={'id': '<id>'},
                          many=True,
                          schema='UsagerSchema',
                          type_='usager')


class LieuSchema(Schema):
    class Meta:
        type_ = 'lieu'
        self_view = 'lieu_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'lieu_list'

    id = fields.Integer(as_String=True, dump_only=True)
    accident_id = fields.Integer(as_String=True)
    catr = fields.Integer(as_String=True)
    voie = fields.Integer(as_String=True)
    circ = fields.Integer(as_String=True)
    nbv = fields.Integer(as_String=True)
    pr = fields.Integer(as_String=True)
    pr1 = fields.Integer(as_String=True)
    vosp = fields.Integer(as_String=True)
    prof = fields.Integer(as_String=True)
    plan = fields.Integer(as_String=True)
    surf = fields.Integer(as_String=True)
    infra = fields.Integer(as_String=True)
    situ = fields.Integer(as_String=True)


class UsagerSchema(Schema):
    class Meta:
        type_ = 'usager'
        self_view = 'usager_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'usager_list'

    id = fields.Integer(as_String=True, dump_only=True)
    accident_id = fields.Integer(as_String=True)
    place = fields.Integer(as_String=True)
    catu = fields.Integer(as_String=True)
    grav = fields.Integer(as_String=True)
    sexe = fields.Integer(as_String=True)
    trajet = fields.Integer(as_String=True)
    secu = fields.Integer(as_String=True)
    locp = fields.Integer(as_String=True)
    actp = fields.Integer(as_String=True)
    etatp = fields.Integer(as_String=True)
    an_nais = fields.Integer(as_String=True)
    num_veh = fields.String()
    accident = Relationship(attribute='usagers',
                            self_view='accident_usager',
                            self_view_kwargs={'id': '<id>'},
                            related_view='accident_detail',
                            related_view_kwargs={'accident_id': '<id>'},
                            schema='AccidentSchema',
                            type_='accident')


class AccidentRelationship(ResourceRelationship):
    schema = AccidentSchema
    data_layer = {'session': db.session,
                  'model': Accident}


class VehiculeSchema(Schema):
    class Meta:
        type_ = 'vehicule'
        self_view = 'vehicule_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'vehicule_list'

    id = fields.Integer(as_String=True, dump_only=True)
    accident_id = fields.Integer(as_String=True)
    senc = fields.Integer()
    catv = fields.Integer()
    occutc = fields.Integer()
    obs = fields.Integer()
    obsm = fields.Integer()
    choc = fields.Integer()
    manv = fields.Integer()
    num_veh = fields.String()


# resource managers
class UsagerList(ResourceList):
    def query(self, view_kwargs):
        query_ = self.session.query(Usager)
        if view_kwargs.get('id') is not None:
            try:
                self.session.query(Accident)\
                            .filter_by(id=view_kwargs['id'])\
                            .one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'},
                                     "Person: {} not found".format(
                                                            view_kwargs['id']))
            else:
                query_ = query_.join(Accident) \
                               .filter(Usager.accident_id == view_kwargs['id'])
        return query_

    def before_create_object(self, data, view_kwargs):
        if view_kwargs.get('id') is not None:
            accident = self.session.query(Accident)\
                                   .filter_by(id=view_kwargs['id'])\
                                   .one()
            data['accident_id'] = accident.id

    schema = UsagerSchema
    data_layer = {'session': db.session,
                  'model': Usager,
                  'methods': {'query': query,
                              'before_create_object': before_create_object}}


class UsagerDetail(ResourceDetail):
    schema = UsagerSchema
    data_layer = {'session': db.session, 'model': Usager}


class AccidentList(ResourceList):
    schema = AccidentSchema
    data_layer = {'session': db.session, 'model': Accident}


class AccidentDetail(ResourceDetail):

    def before_get_object(self, view_kwargs):
        if view_kwargs.get('accident_id') is not None:
            try:
                accident = self.session\
                               .query(Accident)\
                               .filter_by(id=view_kwargs['accident_id'])\
                               .one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'accident_id'},
                                     "Computer: {} not found"
                                     .format(view_kwargs['accident_id']))
            else:
                if accident.usager is not None:
                    view_kwargs['id'] = accident.usager.id
                else:
                    view_kwargs['id'] = None

    schema = AccidentSchema
    data_layer = {'session': db.session,
                  'model': Accident,
                  'methods': {'before_get_object': before_get_object}}


class LieuList(ResourceList):
    schema = LieuSchema
    data_layer = {'session': db.session, 'model': Lieu}


class LieuDetail(ResourceDetail):
    schema = LieuSchema
    data_layer = {'session': db.session, 'model': Lieu}


class VehiculeList(ResourceList):
    schema = VehiculeSchema
    data_layer = {'session': db.session, 'model': Vehicule}


class VehiculeDetail(ResourceDetail):
    schema = VehiculeSchema
    data_layer = {'session': db.session, 'model': Vehicule}
