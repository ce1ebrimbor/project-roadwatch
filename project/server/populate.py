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
import os

app_settings = os.getenv(
    "APP_SETTINGS", "project.server.config.ProductionConfig"
)

if app_settings == "project.server.config.ProductionConfig":
    YEARS = ['2005', '2006', '2007', '2008', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
else:
    YEARS = ['2017']


def populate_accidents():
    for y in YEARS:
        pt = 'project/server/db/files/caracteristiques_{}.csv'.format(y)
        df = caracteristics.process(path=pt)
        db.session.bulk_insert_mappings(Accident, df.to_dict(orient="records"))
        print('[LOADED] {}'.format(pt))


def populate_departements():
    pt = 'project/server/db/files/geojson/departements-avec-outre-mer.geojson'
    df = departements.process(path=pt)
    db.session.bulk_insert_mappings(Departement, df.to_dict(orient="records"))
    print('[LOADED] {}'.format(pt))

def populate_lieux():
    for y in YEARS:
        pt = 'project/server/db/files/lieux_{}.csv'.format(y)
        df = lieux.process(path=pt)
        db.session.bulk_insert_mappings(Lieu, df.to_dict(orient="records"))
        print('[LOADED] {}'.format(pt))

def populate_vehicules():
    for y in YEARS:
        pt = 'project/server/db/files/vehicules_{}.csv'.format(y)
        df = vehicules.process(path=pt)
        db.session.bulk_insert_mappings(Vehicule, df.to_dict(orient="records"))
        print('[LOADED] {}'.format(pt))


def populate_usagers():
    for y in YEARS:
        pt = 'project/server/db/files/usagers_{}.csv'.format(y)
        df = usagers.process(path=pt)
        db.session.bulk_insert_mappings(Usager, df.to_dict(orient="records"))
        print('[LOADED] {}'.format(pt))
