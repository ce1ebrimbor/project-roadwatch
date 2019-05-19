from project.server import db
from project.server.resources import AccidentList, LieuList, UsagerList
from project.server.resources import VehiculeList, UsagerRelationship
from project.server.resources import LieuDetail, AccidentDetail, UsagerDetail
from project.server.resources import VehiculeDetail, AccidentRelationship
from project.server.resources import LieuRelationship, VehiculeRelationship
from project.server.resources import DepartementList, DepartementDetail
from project.server.resources import DepartementRelationship

API_ROUTES = [
    (
        AccidentList,  # Resource manager
        'accident_list',  # View name 
        [
            '/api/v1/accident',  # Path list
            '/api/v1/departement/<string:id>/accident'
        ]
    ),

    (
        AccidentDetail,
        'accident_detail',
        [
            '/api/v1/accident/<int:id>',
            '/api/v1/usager/<int:uid>/accident',
            '/api/v1/lieu/<int:lid>/accident',
            '/api/v1/vehicule/<int:vid>/accident',
        ]
    ),

    (
        AccidentRelationship,
        'accident_usagers',
        [
            '/api/v1/accident/<int:id>/relationships/usager'
        ]
    ),

    (
        AccidentRelationship,
        'accident_lieu',
        [
            '/api/v1/accident/<int:id>/relationships/lieu'
        ]
    ),

    (
        AccidentRelationship,
        'accident_vehicule',
        [
                '/api/v1/accident/<int:id>/relationships/vehicule'
        ]
    ),

    (
        LieuList,
        'lieu_list',
        [
            '/api/v1/lieu'
        ]
    ),

    (
        LieuDetail,
        'lieu_detail',
        [
            '/api/v1/lieu/<int:id>',
            '/api/v1/accident/<int:aid>/lieu'
        ]
    ),

    (
        LieuRelationship,
        'lieu_accident',
        [
            '/api/v1/lieu/<int:id>/relationships/accident'
        ]
    ),

    (
        UsagerList,
        'usager_list',
        [
            '/api/v1/usager',
            '/api/v1/accident/<int:id>/usager'
        ]
    ),

    (
        UsagerDetail,
        'usager_detail',
        [
            '/api/v1/usager/<int:id>'
        ]
    ),

    (
        UsagerRelationship,
        'usager_accident',
        [
            '/api/v1/usager/<int:id>/relationships/accident'
        ]
    ),

    (
        VehiculeList,
        'vehicule_list',
        [
            '/api/v1/vehicule',
            '/api/v1/accident/<int:id>/vehicule'
        ]
    ),

    (
        VehiculeDetail,
        'vehicule_detail',
        [
            '/api/v1/vehicule/<int:id>'
        ]
    ),

    (
        VehiculeRelationship,
        'vehicule_accident',
        [
            '/api/v1/vehicule/<int:id>/relationships/accident'
        ]
    ),
    (
        DepartementList,
        'departement_list',
        [
            '/api/v1/departement'
        ]
    ),
    (
        DepartementDetail,
        'departement_detail',
        [
            '/api/v1/departement/<string:id>'
        ]
    ),
    (
        DepartementRelationship,
        'departement_accidents',
        [
            '/api/v1/departement/<string:id>/relationships/accident'
        ]
    )
]
