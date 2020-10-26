import scrapy
import webbrowser
from playsound import playsound


class Search(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://www.pccomponentes.com/tarjetas-graficas/geforce-rtx-3080-series']
    base_url = "https://www.pccomponentes.com"

    def parse(self, response):
        SET_SELECTOR = '.c-product-card__content'
        for brickset in response.css(SET_SELECTOR):
            if brickset.get().find("Sin fecha de entrada") == 0:
                playsound('media/found.mp3')
                product_link = brickset.css(".c-product-card__title-link").attrib["href"]
                webbrowser.get(
                    "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(self.base_url + product_link)
