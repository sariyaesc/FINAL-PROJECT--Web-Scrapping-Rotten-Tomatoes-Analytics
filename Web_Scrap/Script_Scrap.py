import requests
from bs4 import BeautifulSoup
import datetime
from datetime import datetime

def obtener_contenido_pagina(url):
    respone=requests.get(url)
    return respone.text

def analizar_contenido_html(html):
    return BeautifulSoup(html,'html.parser')

data=[]
def procesar_pagina(soup):
    titulos=[]
    tomatoers=[] 
    audience_scores=[]
    estrenos=[]

    #titulos
    titulo_items=soup.find_all('span',{'data-qa': 'discovery-media-list-item-title'})
    
    for item in titulo_items:
        titulo=item.text.strip()
        titulos.append(titulo)

    #tomatoers
    tomatoers_items=soup.find_all('score-pairs')
    
    for item in tomatoers_items:
        valor_critic=item['criticsscore']
        tomatoers.append(valor_critic)

    tomatoers= [None if item == "" else item for item in tomatoers]
    
    #audience
    audience_score=soup.find_all('score-pairs')

    for item in audience_score:
        valor_audience=item['audiencescore']
        audience_scores.append(valor_audience)
    
    audience_scores= [None if item == "" else item for item in audience_scores]

    #estrenos
    estrenos_items=soup.find_all('span',{'data-qa':'discovery-media-list-item-start-date'})

    for item in estrenos_items:
        estreno=item.text.strip()
        estrenos.append(estreno)

    estrenos=[item.replace('Opened ', '') for item in estrenos]
    estrenos=[item.replace('Opens ', '') for item in estrenos]
    
    min_length = min(len(titulos), len(tomatoers), len(audience_scores), len(estrenos))

    for i in range(min_length):
        data.append({
            "Titles": titulos[i] if i < len(titulos) else None,
            "Critics Score": tomatoers[i]  if i < len(tomatoers) else None,
            "Audience Score": audience_scores[i]  if i < len(audience_scores) else None,
            "Premiere": estrenos[i] if i < len(estrenos) else None,
        })


url= "https://www.rottentomatoes.com/browse/movies_in_theaters/?page=4"
contenido_pagina = obtener_contenido_pagina(url)
soup = analizar_contenido_html(contenido_pagina)
procesar_pagina(soup)

import pandas as pd

df = pd.DataFrame(data)

import datetime
import os
fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
csv_folder = os.path.join("Web_Scrap\dataset")
csv_filename = f"On-Theaters-Rotten-Tomatoes-{fecha_actual}.csv"
csv_path = os.path.join(csv_folder, csv_filename)
df.to_csv(csv_path, index=False)

