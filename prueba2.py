from bs4 import BeautifulSoup
import json

def parse_html(html_string):

    soup = BeautifulSoup(html_string, 'html.parser')

    result = {}

    first_element = soup.find(id=True)
    if first_element:
        element_id = first_element.get('id')

        tags_data = {}

        regalos_list = []

        card_tags_data = {}

        # Itera sobre todas las etiquetas dentro del elemento principal
        for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'p', 'button', 'a', 'label']):
            tag_name = tag.name
            if(tag_name == 'a'):
                a_data = {}
                a_data['href'] = 'google.com.ar'
                a_data['target'] = '_blank'
                a_data['content'] = tag.text.strip()

                tag_classes = tag.get('class', [])

                tags_data[tag_classes[0]] = a_data

            else:
                # Extrae las clases de la etiqueta
                tag_classes = tag.get('class', [])

                if tag_classes:
                    if (tag.text.strip() != '' and 'card' not in tag_classes[0].lower()):
                        tags_data[tag_classes[0]] = tag.text.strip()


        is_regalos = bool(soup.select('#{} .card'.format(element_id)))

        if is_regalos:

            # Caso de estructura de regalos
            for card in soup.select('#{} .card'.format(element_id)):
                card_tags = card.find_all(['h5', 'span', 'btn', 'a'])

                for tag in card_tags:
                    tag_class = tag.get('class', [])[0] if tag.get('class') else 'default'
                    if tag.text.strip():
                        card_tags_data[tag_class] = tag.text.strip()

                regalos_list.append(card_tags_data)

            tags_data['listado'] = regalos_list

        result[element_id] = tags_data

    # Imprime el resultado en formato JSON
    print(json.dumps(result, indent=2, ensure_ascii=False))

# Ejemplo de uso con HTML que contiene ambas estructuras
html_string_mixto = '''
  <div id="portada">
    <h1 class="titulo-portada">
      Juan y Carla
    </h1>
    <a  href="google.com.ar" class="enlaceHashtag">Nos Casamos !</a>
  </div>
'''

parse_html(html_string_mixto)
