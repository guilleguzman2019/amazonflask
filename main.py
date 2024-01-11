from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Agrega CORS a la aplicación

@app.route('/parseHtml', methods=['POST'])
def parse_html():
    try:
        data = request.json
        html_string = data.get('html_string', '')
        soup = BeautifulSoup(html_string, 'html.parser')

        result = {}

        first_element = soup.find(id=True)
        if first_element:
            element_id = first_element.get('id')

            tags_data = {}

            regalos_list = []

            card_tags_data = {}

            # Itera sobre todas las etiquetas dentro del elemento principal
            for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'p', 'button', 'a', 'label', 'img']):

                tag_name = tag.name

                if tag.name == 'img':
                    src = tag.get('src')
                    tag_class = tag.get('class', [])[0] if tag.get('class') else 'default'
                    tags_data[tag_class] = src


                # Extrae las clases de la etiqueta
                tag_classes = tag.get('class', [])

                if tag_classes:
                    if (tag.text.strip() != '' and 'card' and 'countdown-cont' not in tag_classes[0].lower()):
                        tags_data[tag_classes[0]] = tag.text.strip()

            is_regalos = bool(soup.select('#{} .card, #{} .card-testigo, #{} .item'.format(element_id, element_id, element_id)))

            src = ''

            if is_regalos:

                # Caso de estructura de regalos
                for card in soup.select('#{} .card, #{} .card-testigo , #{} .item'.format(element_id, element_id, element_id)):
                    card_tags_data = {}

                    card_tags = card.find_all(['h5', 'span', 'btn', 'a' , 'img'])

                    for tag in card_tags:
                        if tag.name == 'img':
                            src = tag.get('src')
                            tag_class = tag.get('class', [])[0] if tag.get('class') else 'default'
                            card_tags_data[tag_class] = src

                        tag_class = tag.get('class', [])[0] if tag.get('class') else 'default'
                        if tag.text.strip():
                            card_tags_data[tag_class] = tag.text.strip()

                    regalos_list.append(card_tags_data)

                tags_data['listado'] = regalos_list

            result[element_id] = tags_data

        else:
            return jsonify({'error': 'No se encontró un elemento con ID'}), 400

        # Imprime el resultado en formato JSON
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)