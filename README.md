# Ejercicio - Investigación / Script
Ejercicio de script para el Test Gestión Operativa - Básico

## Table of contents
* [General info](#general-info)
* [How it works](#how-it-works)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
The script allows you to generate a file with the publications of a Mercado Libre Argentina seller knowing their selled_id, if you do not know it, the following script can be used to obtain it https://github.com/GCE140/obtener_id_usuario_MELI.

## How it works
The program works by consulting the Mercado Libre API according to what is specified in https://developers.mercadolibre.com.ar/es_ar/items-y-busquedas#Buscar-items-por-vendor, this method is limited by listing only 50 items.

The response obtained from the API is in JSON format, so to work with it, the json and requests modules are necessary in order to be able to send the GET to the API url.

The results are saved in a text file in the same location where the script is found, having the following format:
* Artículo x: 
* ID del ítem: MLAXXXXXXXXX 
* Título del ítem: XXXXXXXXXXXXXXXXXX 
* ID de la catgoría del ítem: MLAXXXXXX 
* Nombre de la categoría: MLA-XXXXXXXXXXXX

## Technologies
Project is created with:
* Python 3.9
* requests 2.26.0
	
## Setup
To run this project, install locally:
* pip install requests
