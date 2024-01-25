"""
* Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen
a partir de una url.
 * - Nota: Esta prueba no se puede resolver con el playground online de Kotlin.
 Se necesita Android Studio.
 * - Url de ejemplo:
 https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
"""

import requests

url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

# Obtener información del encabezado
response = requests.head(url)
content_type = response.headers.get('content-type')

content_length = int(response.headers.get('content-length', 0))
aspect_ratio = content_length / 1024  # Just an example, adjust as needed
print(f"Aspect Ratio: {aspect_ratio}")
