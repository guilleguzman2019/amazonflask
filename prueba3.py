from bs4 import BeautifulSoup
import json

def parse_html(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')

    result = {}

    # Busca el primer elemento con un ID y extrae su ID
    first_element = soup.find(id=True)
    if first_element:
        element_id = first_element.get('id')

        # Lista para almacenar los datos de cada etiqueta
        tags_data = {}

        # Itera sobre todas las etiquetas dentro del elemento principal
        for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'p', 'button', 'a', 'label']):
            tag_name = tag.name

            # Extrae las clases de la etiqueta
            tag_classes = tag.get('class', [])

            if tag_classes:
                if(tag.text.strip() != ''):
                    tags_data[tag_classes[0]] = tag.text.strip()


        # Agrega el resultado al diccionario final
        result[element_id] = tags_data

    # Imprime el resultado en formato JSON
    print(json.dumps(result, indent=2, ensure_ascii=False))

# Ejemplo de uso con HTML de historia
html_string_historia = '''
  <div id="mensaje">
      <div class="container">
        <div class="row">
          <div class="col-12 text-center pt-5">
            <div class="divdedicatoria">
              <h4 class="textodedicatoria">Vayan poniendose sus mejores trajes que estos novios se casan
              </h4>
            </div>
          </div>
        </div>
      </div>
    </div>
'''

# Llama a la función con el HTML de historia
parse_html(html_string_historia)
