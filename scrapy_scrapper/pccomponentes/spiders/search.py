import sys
import scrapy
import webbrowser
from playsound import playsound


class Search(scrapy.Spider):
    name = "brickset_spider"
    start_urls = [
        'https://www.pccomponentes.com/tarjetas-graficas/geforce-rtx-3080-series',
        # 'https://www.pccomponentes.com/tarjetas-graficas/geforce-rtx-3070-series',
        # 'https://www.pccomponentes.com/tablets'
    ]
    base_url = "https://www.pccomponentes.com"
    exceptions = ["zotac"]

    def parse(self, response):
        SET_SELECTOR = '.c-product-card__content'
        items = 0
        for brickset in response.css(SET_SELECTOR):
            items = items + 1
            if brickset.get().find("Sin fecha de entrada") <= 0:
                product_link = brickset.css(".c-product-card__title-link").attrib["href"]

                # Exceptions
                if [e for e in self.exceptions if (e not in product_link.lower())]:
                    playsound('media/found.mp3')
                    webbrowser.get(
                        "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(self.base_url + product_link)

        if items == 0:
            print("You may have been banned from pccomponentes\n\n\n\n\n\n")
