# Project Roadwatch

[![Build Status](https://travis-ci.com/daniel-sasu/project-roadwatch.svg?token=nNtzabkAyK14ViXe6y4n&branch=master)](https://travis-ci.com/daniel-sasu/project-roadwatch)

Every year the French Interior Ministry publishes an enourmous amound of data on the road accidents occured in the country.

The data contains the description of location, weather conditions, circumnstances
of the accidents and the resulted casualties. Details [here](https://www.data.gouv.fr/fr/datasets/base-de-donnees-accidents-corporels-de-la-circulation/)

The goal of this project is to create a resource in the form of an api/app which will allow to effectively query, manipulate and visualize the data.

## API Implementation

The api was implemented according to the [JSON:API 1.0](https://jsonapi.org/format/) specification. Using Flask and [flask-rest-jsonapi](https://github.com/miLibris/flask-rest-jsonapi).

For the api and resource documentation look [here](doc/api.md).


>**Note**:
> The app and data structure is not definitive, and it is susceptible to be heavily modified before
> the 1.0 version.

## Current State

The actual version of the api is **1.0-alpha**. Currently the api is not fully documented nor secured.

## Set Up

Review the set up guides to configure the app:

1. [setup-with-docker.md](setup-with-docker.md)
1. [setup-without-docker.md](setup-without-docker.md)
