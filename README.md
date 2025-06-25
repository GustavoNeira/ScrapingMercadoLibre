# 🛒 Scraper de Mercado Libre (Chile)

Este es un script en Python para realizar **web scraping** de productos desde [MercadoLibre.cl](https://www.mercadolibre.cl/), permitiendo obtener información básica como nombre, precio, enlace al producto e imagen.

Los datos recolectados se exportan automáticamente en formato **JSON**.

## 🚀 Características

- Permite buscar cualquier producto por nombre.
- Recorre múltiples páginas de resultados.
- Extrae título, precio, URL del producto y enlace a la imagen.
- Guarda los datos en `data/mercadolibre.json`.

## 🐍 Tecnologías utilizadas

- [Python 3.x](https://www.python.org/)
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)
- [json](https://docs.python.org/3/library/json.html)
- [os](https://docs.python.org/3/library/os.html)
