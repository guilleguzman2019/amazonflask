from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)  # Agrega CORS a la aplicación
app.config['CORS_HEADERS'] = 'Content-Type'

def obtener_nuevo_soup(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    return soup

def procesar_html(html_string):

    soup = BeautifulSoup(html_string, 'html.parser')

    first_element = soup.find(id=True)
    element_id = first_element.get('id')

    if first_element:
        element_id = first_element.get('id')

    for tag in first_element.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'span', 'p', 'button', 'label', 'a']):
        tag_content = tag.text.strip()
        print(tag)
        tag_classes = tag.get('class', [])[0]
        string = f"${{ jsondata && jsondata['{element_id}'] && jsondata['{element_id}'].{tag_classes} ? jsondata['{element_id}'].{tag_classes} : `{tag_content}` }}"
        tag.string = string

    elementos_hijos = first_element.find_all(recursive=False)

    print(elementos_hijos)

    nuevo_soup = obtener_nuevo_soup("".join(str(elem) for elem in elementos_hijos))

    return str(nuevo_soup)


    return str(soup)

@app.route('/jsonData', methods=['POST'])
@cross_origin()
def post_json_data():
    if 'html' not in request.json:
        return jsonify({'error': 'Missing HTML in the request body'}), 400

    html_input = request.json['html']
    html_modificado = procesar_html(html_input)
    return html_modificado

if __name__ == '__main__':
    app.run(debug=True)