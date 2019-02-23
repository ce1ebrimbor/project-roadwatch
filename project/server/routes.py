from project.server.resources import AccidentList, LieuList, UsagerList
from project.server.resources import VehiculeList, UsagerRelationship
from project.server.resources import LieuDetail, AccidentDetail, UsagerDetail
from project.server.resources import VehiculeDetail, AccidentRelationship
from project.server.resources import LieuRelationship, VehiculeRelationship

API_ROUTES = [
    (
        AccidentList,  # Resource manager
        'accident_list',  # View name 
        [
            '/accident'  # Path list
        ]
    ),

    (
        AccidentDetail,
        'accident_detail',
        [
            '/accident/<int:id>',
            '/usager/<int:uid>/accident',
            '/lieu/<int:lid>/accident',
            '/vehicule/<int:vid>/accident'
        ]
    ),

    (
        AccidentRelationship,
        'accident_usagers',
        [
            '/accident/<int:id>/relationships/usager'
        ]
    ),

    (
        AccidentRelationship,
        'accident_lieu',
        [
            '/accident/<int:id>/relationships/lieu'
        ]
    ),

    (
        AccidentRelationship,
        'accident_vehicule',
        [
                '/accident/<int:id>/relationships/vehicule'
        ]
    ),

    (
        LieuList,
        'lieu_list',
        [
            '/lieu'
        ]
    ),

    (
        LieuDetail,
        'lieu_detail',
        [
            '/lieu/<int:id>',
            '/accident/<int:aid>/lieu'
        ]
    ),

    (
        LieuRelationship,
        'lieu_accident',
        [
            '/lieu/<int:id>/relationships/accident'
        ]
    ),

    (
        UsagerList,
        'usager_list',
        [
            '/usager',
            '/accident/<int:id>/usager'
        ]
    ),

    (
        UsagerDetail,
        'usager_detail',
        [
            '/usager/<int:id>'
        ]
    ),

    (
        UsagerRelationship,
        'usager_accident',
        [
            '/usager/<int:id>/relationships/accident'
        ]
    ),

    (
        VehiculeList,
        'vehicule_list',
        [
            '/vehicule',
            '/accident/<int:id>/vehicule'
        ]
    ),

    (
        VehiculeDetail,
        'vehicule_detail',
        [
            '/vehicule/<int:id>'
        ]
    ),

    (
        VehiculeRelationship,
        'vehicule_accident',
        [
            '/vehicule/<int:id>/relationships/accident'
        ]
    )
]
