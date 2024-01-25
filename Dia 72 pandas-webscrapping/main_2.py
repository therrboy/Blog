from bs4 import BeautifulSoup
import requests
import pandas as pd

url_base = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/'
current_page = 1
contenidos_totales = []


# Itera a través de las filas (ignorando la primera fila de encabezados)
while True:
    url = f'{url_base}{current_page}'
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "lxml")

    tabla = soup.find('table')
    contenidos = []

    encabezados = [encabezado.text for encabezado in tabla.find_all('th')]  # Extraemos los encabezados de cada columna

    for row in tabla.find_all('tr')[1:]:
        fila_contenidos = []
        celdas = row.find_all('td')
        for celda in celdas:
            contenido = celda.text.strip().split(':')[-1].strip()
            fila_contenidos.append(contenido)
        contenidos.append(fila_contenidos)

    if not contenidos:  # Si no hay más contenidos en la página, rompe el bucle
        break

    contenidos_totales.extend(contenidos)  # Agrega los contenidos de esta página a la lista total
    current_page += 1  # Avanza a la siguiente página

df = pd.DataFrame(contenidos_totales, columns=encabezados)

ruta_completa = 'C:\\Users\\Rodrigo\\Desktop\\data\\datos_tabla.csv'
df.to_csv(ruta_completa, index=False, sep=';')  # Index=False para no incluir el índice en el archivo CSV
