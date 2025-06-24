import requests
from bs4 import BeautifulSoup
import json
import os

class Scraper():

    def scraping(self):
        product_name = input("\nProducto: ")
        cleaned_name = product_name.replace(" ", "-").lower()
        base_url = 'https://listado.mercadolibre.cl/'
        urls = [base_url + cleaned_name]

        page_number = 50
        for i in range(0, 10000, 50):
            urls.append(f"{base_url}{cleaned_name}_Desde_{page_number + 1}_NoIndex_True")
            page_number += 50

        self.data = []
        c = 1

        for i, url in enumerate(urls, start=1):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            content = soup.find_all('li', class_='ui-search-layout__item')

            if not content:
                print("\nTermino el scraping.")
                break

            print(f"\nScrapeando pagina numero {i}. {url}")

            for post in content:
                title = post.find('h2').text
                price = post.find('span', class_='andes-money-amount__fraction').text
                post_link = post.find("a")["href"]

                img_tag = post.find("img")
                img_link = img_tag["data-src"] if img_tag and "data-src" in img_tag.attrs else None

                post_data = {
                    "title": title,
                    "price": price,
                    "post link": post_link,
                    "image link": img_link
                }
                self.data.append(post_data)
                c += 1

    def export_to_json(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        data_directory = os.path.join(script_directory, 'data')
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)

       
        

        with open(os.path.join(data_directory, "mercadolibre.json"), "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    s = Scraper()
    s.scraping()
    s.export_to_json()
    print("Datos guardados en 'data/mercadolibre.json'")
 