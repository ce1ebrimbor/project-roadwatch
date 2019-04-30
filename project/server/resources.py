from flask_rest_jsonapi import ResourceDetail, ResourceList
from flask_rest_jsonapi import ResourceRelationship
from flask_rest_jsonapi.exceptions import ObjectNotFound

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields
from sqlalchemy.orm.exc import NoResultFound
from project.server import db
from project.server.models import Accident, Lieu, Usager, Vehicule, Departement


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
    lieu = Relationship(attribute='lieu',
                        self_view='accident_lieu',
                        self_view_kwargs={'id': '<id>'},
                        related_view='lieu_detail',
                        related_view_kwargs={'aid': '<id>'},
                        schema='LieuSchema',
                        type_='lieu')
    vehicule = Relationship(attribute='vehicule',
                            self_view='accident_vehicule',
                            self_view_kwargs={'id': '<id>'},
                            related_view='vehicule_list',
                            related_view_kwargs={'id': '<id>'},
                            many=True,
                            schema='VehiculeSchema',
                            type_='vehicule')


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
    accident = Relationship(attribute='accident',
                            self_view='lieu_accident',
                            self_view_kwargs={'id': '<id>'},
                            related_view='accident_detail',
                            related_view_kwargs={'lid': '<id>'},
                            schema='AccidentSchema',
                            type_='accident')


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
    accident = Relationship(attribute='accident',
                            self_view='usager_accident',
                            self_view_kwargs={'id': '<id>'},
                            related_view='accident_detail',
                            related_view_kwargs={'uid': '<id>'},
                            schema='AccidentSchema',
                            type_='accident')


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
    accident = Relationship(attribute='accident',
                            self_view='vehicule_accident',
                            self_view_kwargs={'id': '<id>'},
                            related_view='accident_detail',
                            related_view_kwargs={'vid': '<id>'},
                            many=True,
                            schema='AccidentSchema',
                            type_='accident')



class DepartementSchema(Schema):
    class Meta:
        type_ = 'departement'
        self_view = 'departement_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'departement_list'

    id = fields.String(as_String=True,dump_only=True)
    geometry = fields.String()
    nom = fields.String()
    accident = Relationship(attribute='accident',
                            self_view='departement_accidents',
                            self_view_kwargs={'id': '<id>'},
                            related_view='accident_list',
                            related_view_kwargs={'id': '<id>'},
                            many=True,
                            schema='AccidentSchema',
                            type_='accident')


# Resource managers
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
                                     "Accident: {} not found".format(
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
    methods = ['GET']
    data_layer = {'session': db.session,
                  'model': Usager,
                  'methods': {'query': query,
                              'before_create_object': before_create_object}}



class UsagerDetail(ResourceDetail):
    schema = UsagerSchema
    methods = ['GET']
    data_layer = {'session': db.session,
                  'model': Usager}


class AccidentList(ResourceList):

    def query(self, view_kwargs):
        query_ = self.session.query(Accident)
        if view_kwargs.get('id') is not None:
            try:
                self.session.query(Departement)\
                            .filter_by(id=view_kwargs['id'])\
                            .one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'},
                                     "Departement: {} not found".format(
                                                            view_kwargs['id']))
            else:
                query_ = query_.join(Departement, Departement.id == Accident.dep) \
                               .filter(
                                    Accident.dep == view_kwargs['id']
                                    )
        return query_

    def before_create_object(self, data, view_kwargs):
        if view_kwargs.get('id') is not None:
            dep = self.session.query(Departement)\
                                   .filter_by(id=view_kwargs['id'])\
                                   .one()
            data['departement_id'] = dep.id

    schema = AccidentSchema
    methods = ['GET']
    data_layer = {'session': db.session,
                'model': Accident,
                'methods': {'query': query,
                            'before_create_object': before_create_object}}

class AccidentDetail(ResourceDetail):

    def before_get_object(self, view_kwargs):
        if view_kwargs.get('aid') is not None:
            try:
                accident = self.session\
                               .query(Accident)\
                               .filter_by(id=view_kwargs['aid'])\
                               .one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'aid'},
                                     "Accident: {} not found"
                                     .format(view_kwargs['aid']))
            else:
                if accident.usager is not None:
                    view_kwargs['id'] = accident.usager.id
                else:
                    view_kwargs['id'] = None

        if view_kwargs.get('uid') is not None:
            try:
                usager = self.session\
                               .query(Usager)\
                               .filter_by(id=view_kwargs['uid'])\
                               .one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'uid'},
                                     "Usager: {} not found"
                                     .format(view_kwargs['uid']))
            else:
                if usager.accident is not None:
                    view_kwargs['id'] = usager.accident.id
                else:
                    view_kwargs['id'] = None

        if view_kwargs.get('lid') is not None:
            try:
                lieu = self.session\
                               .query(Lieu)\
                               .filter_by(id=view_kwargs['lid'])\
                               .one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'lid'},
                                     "Lieu : {} not found"
                                     .format(view_kwargs['lid']))
            else:
                if lieu.accident is not None:
                    view_kwargs['id'] = lieu.accident.id
                else:
                    view_kwargs['id'] = None

        if view_kwargs.get('vid') is not None:
            try:
                vehicule = self.session\
                               .query(Vehicule)\
                               .filter_by(id=view_kwargs['vid'])\
                               .one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'vid'},
                                     "Vehicule: {} not found"
                                     .format(view_kwargs['vid']))
            else:
                if vehicule.accident is not None:
                    view_kwargs['id'] = vehicule.accident.id
                else:
                    view_kwargs['id'] = None

        if view_kwargs.get('depid') is not None:
            try:
                departement = self.session\
                              .query(Departement)\
                              .filter_by(id=view_kwargs['depid'])\
                              .one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'depid'},
                                     "Departement: {} not found"
                                     .format(view_kwargs['depid']))
            else:
                if departement.accident is not None:
                    view_kwargs['depid'] = departement.accident.id
                else:
                    view_kwargs['depid'] = None

    schema = AccidentSchema
    methods = ['GET']
    data_layer = {'session': db.session,
                  'model': Accident,
                  'methods': {'before_get_object': before_get_object}}



class LieuList(ResourceList):
    schema = LieuSchema
    methods = ['GET']
    data_layer = {'session': db.session, 'model': Lieu}


class LieuDetail(ResourceDetail):

    def before_get_object(self, view_kwargs):
        if view_kwargs.get('aid') is not None:
            try:
                accident = self.session\
                               .query(Accident)\
                               .filter_by(id=view_kwargs['aid'])\
                               .one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'aid'},
                                     "Accident: {} not found"
                                     .format(view_kwargs['aid']))
            else:
                if accident.lieu is not None:
                    view_kwargs['id'] = accident.lieu.id
                else:
                    view_kwargs['id'] = None

    schema = LieuSchema
    methods = ['GET']
    data_layer = {'session': db.session,
                  'model': Lieu,
                  'methods': {'before_get_object': before_get_object}}


class VehiculeList(ResourceList):

    def query(self, view_kwargs):
        query_ = self.session.query(Vehicule)
        if view_kwargs.get('id') is not None:
            try:
                self.session.query(Accident)\
                            .filter_by(id=view_kwargs['id'])\
                            .one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'},
                                     "Accident: {} not found".format(
                                                            view_kwargs['id']))
            else:
                query_ = query_.join(Accident) \
                               .filter(
                                    Vehicule.accident_id == view_kwargs['id']
                                    )
        return query_

    def before_create_object(self, data, view_kwargs):
        if view_kwargs.get('id') is not None:
            accident = self.session.query(Accident)\
                                   .filter_by(id=view_kwargs['id'])\
                                   .one()
            data['accident_id'] = accident.id

    schema = VehiculeSchema
    methods = ['GET']
    data_layer = {'session': db.session,
                'model': Vehicule,
                'methods': {'query': query,
                            'before_create_object': before_create_object}}


class VehiculeDetail(ResourceDetail):
    schema = VehiculeSchema
    methods = ['GET']
    data_layer = {'session': db.session, 'model': Vehicule}


class DepartementDetail(ResourceDetail):
    schema = DepartementSchema
    methods = ['GET']
    data_layer = {'session': db.session, 'model': Departement}

class DepartementList(ResourceList):
    schema = DepartementSchema
    methods = ['GET']
    data_layer = {'session': db.session, 'model': Departement}


# Resource relationships
class AccidentRelationship(ResourceRelationship):
    schema = AccidentSchema
    methods = ['GET']
    data_layer = {'session': db.session,
                  'model': Accident}


class LieuRelationship(ResourceRelationship):
    schema = LieuSchema
    methods = ['GET']
    data_layer = {'session': db.session,
                  'model': Lieu}


class UsagerRelationship(ResourceRelationship):
    schema = UsagerSchema
    methods = ['GET']
    data_layer = {'session': db.session,
                  'model': Usager}


class VehiculeRelationship(ResourceRelationship):
    schema = VehiculeSchema
    methods = ['GET']
    data_layer = {'session': db.session,
                  'model': Vehicule}

class DepartementRelationship(ResourceRelationship):
    schema = DepartementSchema
    methods = ['GET']
    data_layer = {'session': db.session,
                  'model': Departement }
