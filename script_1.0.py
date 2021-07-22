import requests, os, json
from requests.api import request
from requests.exceptions import HTTPError
from datetime import datetime

ahora = datetime.now()
formato_fecha = "%d-%m-%Y-%Hh-%Mm-%Ss"
texto_fecha = ahora.strftime(formato_fecha)


def crear_log():
    cant_revisar = int(input("Ingrese la cantidad de sellers a revisar: "))

    for x in range(cant_revisar):
        print()
        seller_id = input("Ingrese el Nro ID del seller (ej: 179571326 / 114457637): ")
        print()

        for url in [f'https://api.mercadolibre.com/sites/MLA/search?seller_id={seller_id}']:
            try:
                response = requests.get(url)
                response.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error: {http_err}')
            except Exception as err:
                print(f'Otro error sucedió: {err}')
            else:
                print('Conexión correta!')
                json_data = json.loads(response.text)
        print()

        ids = []
        titles = []
        category_ids = []
        domain_ids = []

        for i in range (len(json_data["results"])):
            ids.append(json_data["results"][i]["id"])
            titles.append(json_data["results"][i]["title"])
            category_ids.append(json_data["results"][i]["category_id"])
            domain_ids.append(json_data["results"][i]["domain_id"])

        print("Cantidad de IDs de productos: " + str(len(ids)))
        print("Cantidad de titulos de productos: " + str(len(titles)))
        print("Cantidad de categorías de IDs de productos: " + str(len(category_ids)))
        print("Cantidad de nombres de categorías de productos: " + str(len(domain_ids)))
        print()

        nombre_log = "log_seller_" + seller_id + "_" + texto_fecha

        log = open(nombre_log+".txt","w")
        for j in range (len(ids)):
            log.write("Artículo " + str(j+1) + ":\n" + "ID del ítem:\t\t\t" + str(ids[j])+"\n" + "Título del ítem:\t\t" +str(titles[j])+ "\n" + "ID de la catgoría del ítem:\t" + str(category_ids[j]+ "\n" + "Nombre de la categoría:\t\t" +str(domain_ids[j])+"\n\n"))
        log.close()
        print("Se ha creado el archivo " + nombre_log + ".txt")
        print()


if __name__ == "__main__":
    print("\nBIENVENIDO/A ESTE PROGRAMA GENERA UN LOG CON LAS PUBLICACIONES DE UN USUARIO DE MERCADO LIBRE DANDO EL ID DE DICHO USUARIO:\n")
    crear_log()