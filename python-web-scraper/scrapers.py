from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests


class WebScraper(ABC):

    @abstractmethod
    def scrape(self, url):
        pass



class QuoteScraper(WebScraper):

    def scrape(self, url):

        response = requests.get(url, timeout=10, headers={'User-Agent': "FactoryMethodClassDemo/1.0"},)

        response.raise_for_status()

        #<html>.....</html>
        soup = BeautifulSoup(response.text, 'html.parser')

        results = []

        for quote_box in soup.select("div.quote"):

            quote = quote_box.select_one("span.text").get_text(strip=True)

            author = quote_box.select_one("small.author").get_text(strip=True)

            results.append({
                "quote": quote,
                "author": author,
            })

        return results



class BookScraper(WebScraper):

    def scrape(self, url):

        response = requests.get(url, timeout=10, headers={'User-Agent': "FactoryMethodClassDemo/1.0"},)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        results = []

        for book_box in soup.select("article.product_pod"):

            title = book_box.select_one("h3 a")["title"]

            price = book_box.select_one("p.price_color").get_text(strip=True)

            results.append({
                "title": title,
                "price": price,
            })

        return results
 
    