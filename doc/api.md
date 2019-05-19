# Project Roadwatch API

This api serves as a repository for the road accidents data published by the French Interior Ministry.
The main goal was to build a flexible and easy to access api wich will do the **heavy** work such as
sorting and filtering the data.

The api was implemented according to the [JSON:API v1.0](https://jsonapi.org/format/) specification.


## Getting Started

The current version of the api lives at `http://api/v1/path`.


##### Versions

| Version | Date | Changes |
|---------|------|---------|
|1.0-alpha   | 10-03-2019     | Initial release.|



> **Note:** In order to interact with our api we recommend you to use one of [these](https://jsonapi.org/implementations/#client-libraries) client libraries.

## Basic API calls

> **Note:** In order to get access to the api you have to register and get an access token. You can generate a token in your Dashboard page.  The token has to be used as a keyword parameter for every request. Example: `GET /accident?token=<your-token>`

* #### `GET /accident`

This endpoint returns the list of accidents.

#### Response example

```
{
  "data" : [
    {
        "attributes": {
            "adr": "68 place de l'hotel de v",
            "agg": 2,
            "atm": 1,
            "col": 6,
            "comm": "59416",
            "date": "2017-10-03T07:10:00",
            "dep": "590",
            "gps": "M",
            "int": 1,
            "long": 2.51553,
            "lat": 50.69162,
            "lum": 5
        },
        "id": 201700000030,
        "links": {
            "self": "/accident/201700000030"
        },
        "relationships": {
            "lieu": {
                "links": {
                    "related": "/accident/201700000030/lieu",
                    "self": "/accident/201700000030/relationships/lieu"
                }
            },
            "usager": {
                "links": {
                    "related": "/accident/201700000030/usager",
                    "self": "/accident/201700000030/relationships/usager"
                }
            },
            "vehicule": {
                "links": {
                    "related": "/accident/201700000030/vehicule",
                    "self": "/accident/201700000030/relationships/vehicule"
                }
            }
        },
        "type": "accident"
      }
    ],
    "jsonapi": {
      "version": "1.0"
    },
    "links": {
      "first": "http://api/v1/accident",
      "last": "http://api/v1/accident?page%5Bnumber%5D=2024",
      "next": "http://api/v1/accident?page%5Bnumber%5D=2",
      "self": "http://api/v1/accident"
    },
    "meta": {
      "count": 60701
    }
}

```




* #### `GET /accident/{id:int}`

This endpoind returns one accident by id.

##### Example with `GET /accident/20`
```
{
    "data": {
        "attributes": {
            "adr": "rue nationale",
            "agg": 2,
            "atm": 1,
            "col": 1,
            "comm": "59477",
            "date": "2017-01-11T18:20:00",
            "dep": "590",
            "gps": "M",
            "int": 1,
            "lat": 50.51326,
            "long": 2.92191,
            "lum": 5
        },
        "id": 201700000001,
        "links": {
            "self": "/accident/201700000001"
        },
        "relationships": {
            "lieu": {
                "links": {
                    "related": "/accident/201700000001/lieu",
                    "self": "/accident/201700000001/relationships/lieu"
                }
            },
            "usager": {
                "links": {
                    "related": "/accident/201700000001/usager",
                    "self": "/accident/201700000001/relationships/usager"
                }
            },
            "vehicule": {
                "links": {
                    "related": "/accident/201700000001/vehicule",
                    "self": "/accident/201700000001/relationships/vehicule"
                }
            }
        },
        "type": "accident"
    },
    "jsonapi": {
        "version": "1.0"
    },
    "links": {
        "self": "/accident/201700000001"
    }
}

```


#### * `GET /usager`

This endpoint returns the list of accident victims.

```
{
    "data": [
        {
            "attributes": {
                "adr": "rue nationale",
                "agg": 2,
                "atm": 1,
                "col": 1,
                "comm": "59477",
                "date": "2017-01-11T18:20:00",
                "dep": "590",
                "gps": "M",
                "int": 1,
                "lat": 50.51326,
                "long": 2.92191,
                "lum": 5
            },
            "id": 201700000001,
            "links": {
                "self": "/accident/201700000001"
            },
            "relationships": {
                "lieu": {
                    "links": {
                        "related": "/accident/201700000001/lieu",
                        "self": "/accident/201700000001/relationships/lieu"
                    }
                },
                "usager": {
                    "links": {
                        "related": "/accident/201700000001/usager",
                        "self": "/accident/201700000001/relationships/usager"
                    }
                },
                "vehicule": {
                    "links": {
                        "related": "/accident/201700000001/vehicule",
                        "self": "/accident/201700000001/relationships/vehicule"
                    }
                }
            },
            "type": "accident"
        },

...

],
  "jsonapi": {
      "version": "1.0"
  },
  "links": {
      "first": "http://api/v1/usager",
      "last": "http://api/v1/usager?page%5Bnumber%5D=4535",
      "next": "http://api/v1/usager?page%5Bnumber%5D=2",
      "self": "http://api/v1/usager"
  },
  "meta": {
      "count": 136021
  }
}

```

* ####  `GET /usager/{id:int}`

This endpoint returns the victim by id.

#####  Example with `GET /usager/1`
```

{
    "data": {
        "attributes": {
            "accident_id": 201700000001,
            "actp": 0,
            "an_nais": 1968,
            "catu": 1,
            "etatp": 0,
            "grav": 3,
            "locp": 0,
            "num_veh": "B01",
            "place": 1,
            "secu": 13,
            "sexe": 1,
            "trajet": 9
        },
        "id": 1,
        "links": {
            "self": "/usager/1"
        },
        "relationships": {
            "accident": {
                "links": {
                    "related": "/usager/1/accident",
                    "self": "/usager/1/relationships/accident"
                }
            }
        },
        "type": "usager"
    },
    "jsonapi": {
        "version": "1.0"
    },
    "links": {
        "self": "/usager/1"
    }
}
```

* #### `GET /vehicule`

This endpoint returns the list of vehicles involved in accidents.

```

{
    "data": [
        {
            "attributes": {
                "accident_id": 201700000001,
                "catv": 7,
                "choc": 3,
                "manv": 9,
                "num_veh": "B01",
                "obs": null,
                "obsm": 2,
                "occutc": null,
                "senc": null
            },
            "id": 1,
            "links": {
                "self": "/vehicule/1"
            },
            "relationships": {
                "accident": {
                    "links": {
                        "related": "/vehicule/1/accident",
                        "self": "/vehicule/1/relationships/accident"
                    }
                }
            },
            "type": "vehicule"
        },
        ...
         ],
    "jsonapi": {
        "version": "1.0"
    },
    "links": {
        "first": "http://api/v1/vehicule",
        "last": "http://api/v1/vehicule?page%5Bnumber%5D=3452",
        "next": "http://api/v1/vehicule?page%5Bnumber%5D=2",
        "self": "http://api/v1/vehicule"
    },
    "meta": {
        "count": 103546
    }
}

```

* #### `GET /vehicule/{id:int}`

This endpoint returns a vehicle by id.

##### Example with `GET /vehicule/1`

```
{
    "data": {
        "attributes": {
            "accident_id": 201700000001,
            "catv": 7,
            "choc": 3,
            "manv": 9,
            "num_veh": "B01",
            "obs": null,
            "obsm": 2,
            "occutc": null,
            "senc": null
        },
        "id": 1,
        "links": {
            "self": "/vehicule/1"
        },
        "relationships": {
            "accident": {
                "links": {
                    "related": "/vehicule/1/accident",
                    "self": "/vehicule/1/relationships/accident"
                }
            }
        },
        "type": "vehicule"
    },
    "jsonapi": {
        "version": "1.0"
    },
    "links": {
        "self": "/vehicule/1"
    }
}

```

* ####  `GET /lieu`

This endpoint returns a list of accident location description.

```
{
    "data": [
        {
            "attributes": {
                "accident_id": 201700000001,
                "catr": 3,
                "circ": 2,
                "infra": null,
                "nbv": 2,
                "plan": 1,
                "pr": null,
                "pr1": null,
                "prof": 1,
                "situ": 1,
                "surf": 1,
                "voie": 39,
                "vosp": 2
            },
            "id": 1,
            "links": {
                "self": "/lieu/1"
            },
            "relationships": {
                "accident": {
                    "links": {
                        "related": "/lieu/1/accident",
                        "self": "/lieu/1/relationships/accident"
                    }
                }
            },
            "type": "lieu"
        },
        ...
        ],
    "jsonapi": {
        "version": "1.0"
    },
    "links": {
        "first": "http://api/v1/lieu",
        "last": "http://api/v1/lieu?page%5Bnumber%5D=2024",
        "next": "http://api/v1/lieu?page%5Bnumber%5D=2",
        "self": "http://api/v1/lieu"
    },
    "meta": {
        "count": 60701
    }
}


```




* ####  `GET /lieu/{id:int}`

This endpoint returns a location by id.

##### Example with `GET /lieu/1`

```
{
    "data": {
        "attributes": {
            "accident_id": 201700000001,
            "catr": 3,
            "circ": 2,
            "infra": null,
            "nbv": 2,
            "plan": 1,
            "pr": null,
            "pr1": null,
            "prof": 1,
            "situ": 1,
            "surf": 1,
            "voie": 39,
            "vosp": 2
        },
        "id": 1,
        "links": {
            "self": "/lieu/1"
        },
        "relationships": {
            "accident": {
                "links": {
                    "related": "/lieu/1/accident",
                    "self": "/lieu/1/relationships/accident"
                }
            }
        },
        "type": "lieu"
    },
    "jsonapi": {
        "version": "1.0"
    },
    "links": {
        "self": "/lieu/1"
    }
}
```

## The full list of endpoints


> Note: The api supports only `GET` requests.

|Endpoint| Description |Parameter | Parameter type | Returned Resource  Type |
|--------|-------------|----------|----------------|-------------------------|
| /accident | Get list of accidents. | - | - | Accident         |
| /usager   | Get list of victims.   | - | - | Usager           |
| /lieu     | Get list of accident locations. | - | - | Lieu    |
| /departement | Get the list of France's departement | - | - | Departement |
| /vehicule | Get list of vehicles involved in accidents | - | - | Vehicule |
| /accident/{id:int} | GET the  accident by id. |id | int | Accident|
| /usager/{id:int}/accident | Get the accident in wich the person was involved.  |id| int| Accident|
| /lieu/{id:int}/accident          |  Get the accident that occured in the location. |id| int| Accident|
| /vehicule/{id:int}/accident          | Get the accident the vehicle was involved in.  |id | int | Accident |
| /lieu/{id:int}          | Get the location by id.  |id | int | Lieu|
| /accident/{id:int}/lieu          |   Get the location of the accident. |id | int | Lieu|
| /accident/{id:int}/usager        |   Get the victims of the accident. |id | int | Usager|
| /usager/{id:int}          |  Get the victim by id. |id | int | Usager|
| /accident/{id:int}/vehicule | Get the vehicles involved in the accident.| id | int | Vehicule|
| /vehicule/{id:int} | Get the vehicle by id.| id | int | Vehicule|
| /departement/{string:id} | Get the departement by id (see codes insee). | id | str | Departement |
| /accident/{int:id}/relationships/usager | Get the relationship between accident and usager.|id | int | AccidentRelationship |
| /accident/{int:id}/relationships/lieu | Get the relationship between accident and lieu.| id | int | AccidentRelationship |
| /accident/{int:id}/relationships/vehicule | Get the relationship between accident and vehicule.| id | int | AccidentRelationship |
| /lieu/{int:id}/relationships/accident | Get the relationship between lieu and accident.| id | int | LieuRelationship |
| /usager/{int:id}/relationships/accident | Get the relationship between usager and accident.| id | int | UsagerRelationship |
| /departement/{string:id}/relationships/accident | Get the relationship between the departement and the accident resources. | id | str | DepartementRelationship |
| /vehicule/{int:id}/relationships/accident | Get the relationship between vehicule and accident.| id | int | VehiculeRelationship |


## Querying and Filtering the data

In this section we will show you a couple of examples of querying and filtering the data. The examples are meant to provide an insight on the capabilities of the api. If you want to find out more about query structure take a look [here](https://flask-rest-jsonapi.readthedocs.io/en/latest/filtering.html) and on the JSON API [spec page](https://jsonapi.org/).

### Examples of queries

### All acidents where there is at least one person born in 1973
```
$ http GET localhost:5002/accident filter=='[
	{"name": "usager",
	 "op": "any",
	 "val": {
	 	"name":"an_nais",
		"op":"eq",
		"val":"1973"
		}
	}
	]' include=='usager'

```


### The persons born in 1973 involved in an accident with a heavy-duty-vehicle
```
$ http GET localhost:5002/usager filter=='[{"name": "an_nais", "op": "eq", "val": "1973"}, {"name": "accident", "op": "has", "val": {"name": "vehicule", "op": "any", "val": {"name": "catv", "op":"eq", "val": "14"}}}]' include=='accident.vehicule,accident'
```

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




### Usager

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



> **Note:** Some resource attributes are encoded as integers. To find the **meaning** of the values read the the [decode.json](decode.json) file.
