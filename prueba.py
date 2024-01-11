# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

def parse_html(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')

    result = {}

    # Busca el primer elemento con un ID y extrae su ID
    first_element = soup.find(id=True)
    if first_element:
        element_id = first_element.get('id')

        # Busca todas las etiquetas de texto dentro del elemento
        cards = soup.select('#{} .card'.format(element_id))  # Modificado para adaptarse a la estructura de eventos
        tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'p'])  # Mantenido para adaptarse a la estructura de vestimenta

        # Lista para almacenar los datos de cada evento o tags de vestimenta
        data_list = []

        if cards:
            # Caso de estructura de eventos
            for card in cards:
                evento_data = {}
                card_title = card.select_one('.card-title')
                div_horario = card.select_one('.divhorario span')
                card_lugar = card.select_one('.card-lugar')
                card_text = card.select_one('.card-text')

                if card_title:
                    evento_data['tituloEvento'] = card_title.text.strip()
                if div_horario:
                    evento_data['horarioEvento'] = div_horario.text.strip()
                if card_lugar:
                    evento_data['lugarEvento'] = card_lugar.text.strip()
                if card_text:
                    evento_data['descripcionEvento'] = card_text.text.strip()

                data_list.append(evento_data)
        elif tags:
            # Caso de estructura de vestimenta
            tags_data = {}
            for tag in tags:
                if tag.text.strip():
                    if tag.get('class'):
                        # Utiliza la clase como clave y el contenido como valor
                        tags_data[tag['class'][0]] = tag.text.strip()
                    else:
                        # Si no hay clase, usa 'default' como clave
                        tags_data['default'] = tag.text.strip()

            # Crea el objeto "historia" en el formato deseado
            historia = {
                "tituloHistoria": tags_data.get('titulohashtag', ''),
                "textoHistoria": tags_data.get('hashtag', '')
            }

            if(element_id != 'eventos'):
                data_list = historia


        # Añade la lista de eventos o tags al diccionario resultante
        result[element_id] = data_list

    # Imprime el resultado en formato JSON
    print(json.dumps(result, indent=2, ensure_ascii=False))

# Ejemplo de uso con la estructura de eventos
html_string_eventos = '''
    <div id="regalos">
    <div class="container">
      <div class="row text-xs-center p-t-1 p-b-3">
        <div class="col-md-12 text-center">
          <br/>
          <h3 class="tituloregalo">Mesa de Regalo
          </h3>
          <br/>
          <div class="divtexto">
            <span class="textoregalo text-light">Tu presencia es nuestro mejor regalo, pero si quieres bendecirnos con algún bien material, aquí te dejamos una lista de regalos que nos gustaría recibir, o bien, también puedes colaborar con nuestra Luna de Miel.</span>
          </div>
          <br/>
          <div class="switcher mt-5 mb-5">
            <input type="radio" name="balance" value="yin" id="yin" checked class="switcher__input switcher__input--yin"/>
            <label for="yin" class="switcher__label yin">VER DATOS</label>
            <input type="radio" name="balance" value="yang" id="yang" class="switcher__input switcher__input--yang"/>
            <label for="yang" class="switcher__label yang">VER LISTA</label>
            <span class="switcher__toggle"></span>
          </div>
          <br/>
          <span class="datosbancarios pb-4">
            TITULAR: MATIAS NICOLAS SANCHEZ
            CBU: 1430001713011714940016
            ALIAS: TUERCA.TRUCO.MANIJA
            Nº DE CUENTA: 1301171494001
            CUIT: 23-36988681-9</span>
          <br/>
          <div id="i1kef">
            <div class="carousel-wrap re contenregalo pt-4" id="i7y25">
              <div class="owl-carousel regalos">
                <div class="card p-4">
                  <img src="https://eleve11.ar/wp-content/uploads/jet-engine-forms/1/2022/09/D_NQ_NP_885930-MLA47397157459_092021-O.webp" alt="Card image cap" class="card-img-top"/>
                  <div class="card-body">
                    <h5 class="card-title">LAMPARA COLGANTE
                    </h5>
                    <span class="card-text">Lampara Campana Colgante 40cm Nórdica Escandinaba Madera</span>
                    <h5 class="cardprecio mt-3">$36452
                    </h5>
                    <br/>
                    <a href="" class="botonhashtag">REGALAR</a>
                  </div>
                </div>
                <div class="card p-4">
                  <img src="https://eleve11.ar/wp-content/uploads/jet-engine-forms/1/2022/09/D_NQ_NP_885930-MLA47397157459_092021-O.webp" alt="Card image cap" class="card-img-top"/>
                  <div class="card-body">
                    <h5 class="card-title">LAMPARA COLGANTE
                    </h5>
                    <span class="card-text">Lampara Campana Colgante 40cm Nórdica Escandinaba Madera</span>
                    <h5 class="cardprecio mt-3">$36452
                    </h5>
                    <br/>
                    <a href="" class="botonhashtag">REGALAR</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
'''

parse_html(html_string_eventos)

# Ejemplo de uso con la estructura de vestimenta
html_string_vestimenta = '''
    <div id="historia">
        <div class="container">
            <div class="row text-xs-center p-t-1 p-b-4">
                <div class="col-md-12 text-center">
                    <br/><h3 class="titulohashtag text-light">Nuestra Historia</h3><br/>
                    <p class="hashtag">Tan sólo podemos decir que nuestra vida en estos momentos se encuentra completa y estamos listos para compartir el resto de nuestros días juntos.</p>
                </div>
            </div>
        </div>
    </div>
'''

parse_html(html_string_vestimenta)
