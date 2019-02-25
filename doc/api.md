# Project Roadwatch API

This api serves as a repository for the road accidents data published by the French Interior Ministry.
The main goal was to build a flexible and easy to access api wich will do the **heavy** work such as
sorting and filtering of the data.

The api was implemented according to the [JSON:API 1.0](https://jsonapi.org/format/) specification. Using Flask and [flask-rest-jsonapi](https://github.com/miLibris/flask-rest-jsonapi).

## Resources

### Accident

Accident resource contains some key data related to the event.

| Attribute | Type |Description |
|-----------|------|-------------|
|id         | integer | A unique number attributed to the event. |
|agg        | integer | Localisation type. |
|int        | integer | Intersection type. |
|atm        | integer | Weather conditions. |
|col        | integer | Colision type.      |
|adr        | string  | Address.            |
|gps        | string  | Region descriptor.  |
|lat        | number  | Latitude.           |
|long       | number  | Longitude.          |
|date       | date-time | The time the accident occured. |

### Vehicule

Vehicule resource contains details on involved vehicles.

| Attribute | Type |Description |
|-----------|------|-------------|
|id         | integer | A unique id.     |
|accident_id | integer | A reference to the accident. |
|senc        | integer | Moving direction. |
|catv       | integer | Vehicle category.  |
|obs        | integer | Hit a fixed obstacle.     |
|obsm       | integer | Hit a moving obstacle. |
|choc       | integer | Impact point. |
|manv       | integer | Maneuver before the accident. |
|occutc     | integer | Number of people in public transport. |


### Usager


Usager describes the individuals involved in the accident.

| Attribute | Type |Description |
|-----------|------|-------------|
|id         | integer | A unique id.     |
|accident_id | integer | A reference to the accident |
|num_veh     | string  | A vehicle identifier |
|place       | integer | The place occupied by the person in the vehicle. |
|catu        | integer | Category. |
|grav        | integer | Accident Gravity |
|sexe        | integer | Biological sex. |
|an_nais     | integer | birth year |
|trajet      | integer | itinerary |


### Lieu

Lieu describes the road type and location of the accident.

| Attribute | Type |Description |
|-----------|------|-------------|
|id         | integer | A unique id.     |
|accident_id | integer | A reference to the accident. |
|catr        | integer | Road type. |
|voie        | integer | Road number. |
|circ        | integer | Traffic type. |
|nbv         | integer | Number of lanes |
|vosp        | integer | Signals the existance of a reserved lane. |
|prof        | integer | Road gradient. |
|pr          | integer | Attached milestone. |
|pr1         | integer | Distance to the milestone (in meters). |
|plan        | integer | Trajectory. |
|surf        | integer | The ground state. |
|infra       | integer | The presence of an infrastructure |
|situ        | integer | Accident location. |
