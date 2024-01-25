from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors'
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'lxml')

table = soup.find('table')

data = []
headers = [header.text for header in table.find_all('th')]

for row in table.find_all('tr'):
    row_data = [cell.text for cell in row.find_all('td')]
    if row_data:  # Ignorar filas vacías
        data.append(row_data)


df = pd.DataFrame(data, columns=headers)

# numeric_columns = ['Rank', 'Early Career Pay', 'Mid-Career Pay', '% High Meaning']
# df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

ruta_completa = 'C:\\Users\\Rodrigo\\Desktop\\data\\datos_tabla.csv'
df.to_csv(ruta_completa, index=False, sep=';')
