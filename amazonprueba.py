import requests
from pprint import pprint
import json


# Structure payload.
payload = {
    'source': 'amazon_search',
    'domain': 'com',
    'query': data.get('query', ''),
    'start_page': 1,
    'pages': 10,
    'parse': True,
}


# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('guillermo2020', 'Guillermo2020'),
    json=payload,
)

data = response.json()

if 'results' in data:
    results_array = []
    # Recorrer la lista 'results'
    for result in data['results']:
        # Verificar si la clave 'content' está presente en cada resultado
        if 'content' in result:

            if 'paid' in result['content']['results']:

                for paid_result in result['content']['results']['paid']:

                    json = {}
                    # Obtener las propiedades deseadas
                    url = paid_result.get('url', '')
                    asin = paid_result.get('asin', '')
                    price = paid_result.get('price', '')
                    title = paid_result.get('title', '')
                    url_image = paid_result.get('url_image', '')

                    result_dict = {
                        'url': url,
                        'asin': asin,
                        'price': price,
                        'title': title,
                        'url_image': url_image,
                    }

                    # Agregar el diccionario al array general
                    results_array.append(result_dict)

                    # Imprimir o utilizar las propiedades como sea necesario
                    #print(f"URL: {url}, ASIN: {asin}, Price: {price}, Title: {title}, URL Image: {url_image}")

            if 'organic' in result['content']['results']:

                for paid_result in result['content']['results']['organic']:
                    # Obtener las propiedades deseadas
                    url = paid_result.get('url', '')
                    asin = paid_result.get('asin', '')
                    price = paid_result.get('price', '')
                    title = paid_result.get('title', '')
                    url_image = paid_result.get('url_image', '')

                    result_dict = {
                        'url': url,
                        'asin': asin,
                        'price': price,
                        'title': title,
                        'url_image': url_image,
                    }

                    # Agregar el diccionario al array general
                    results_array.append(result_dict)

            if 'suggested' in result['content']['results']:

                for paid_result in result['content']['results']['suggested']:
                    # Obtener las propiedades deseadas
                    url = paid_result.get('url', '')
                    asin = paid_result.get('asin', '')
                    price = paid_result.get('price', '')
                    title = paid_result.get('title', '')
                    url_image = paid_result.get('url_image', '')

                    result_dict = {
                        'url': url,
                        'asin': asin,
                        'price': price,
                        'title': title,
                        'url_image': url_image,
                    }

                    # Agregar el diccionario al array general
                    results_array.append(result_dict)

                    # Imprimir o utilizar las propiedades como sea necesario
                    #print(f"URL: {url}, ASIN: {asin}, Price: {price}, Title: {title}, URL Image: {url_image}")
else:
    print("La clave 'results' no está presente en la respuesta.")



print(results_array)

