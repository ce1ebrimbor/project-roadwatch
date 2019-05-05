# project/server/populate.py

from rw_data_proc import caracteristics
from rw_data_proc import departements
from rw_data_proc import lieux
from rw_data_proc import vehicules
from rw_data_proc import usagers
from project.server import db
from project.server.models import Accident
from project.server.models import Departement
from project.server.models import Lieu
from project.server.models import Vehicule
from project.server.models import Usager

import numpy as np

def populate_accidents():
    df = caracteristics.process(path='project/server/db/files/caracteristiques-2017.csv')
    db.session.bulk_insert_mappings(Accident, df.to_dict(orient="records"))


def populate_departements():
    df = departements.process(path='project/server/db/files/geojson/departements-avec-outre-mer.geojson')
    db.session.bulk_insert_mappings(Departement, df.to_dict(orient="records"))


def populate_lieux():
    df = lieux.process(path='project/server/db/files/lieux-2017.csv')
    db.session.bulk_insert_mappings(Lieu, df.to_dict(orient="records"))

def populate_vehicules():
    df = vehicules.process(path='project/server/db/files/vehicules-2017.csv')
    db.session.bulk_insert_mappings(Vehicule, df.to_dict(orient="records"))

def populate_usagers():
    df = usagers.process(path='project/server/db/files/usagers-2017.csv')
    db.session.bulk_insert_mappings(Usager, df.to_dict(orient="records"))
