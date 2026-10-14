from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup


# Product
class WebScraper(ABC):
    @abstractmethod
    def scrape(self, source):
        pass


# Concrete Product 1 - Online Quotes
class QuoteScraper(WebScraper):
    def scrape(self, source):
        response = requests.get(
            source,
            timeout=10,
            headers={"User-Agent": "FactoryClassDemo/1.0"},
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        results = []

        for quote_box in soup.select("div.quote"):
            quote = quote_box.select_one("span.text").get_text(strip=True)
            author = quote_box.select_one("small.author").get_text(strip=True)

            results.append({
                "quote": quote,
                "author": author,
            })

        return results


# Concrete Product 2 - Online Books
class BookScraper(WebScraper):
    def scrape(self, source):
        response = requests.get(
            source,
            timeout=10,
            headers={"User-Agent": "FactoryClassDemo/1.0"},
        )
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


# Concrete Product 3 - Offline Quotes
class OfflineQuoteScraper(WebScraper):
    def scrape(self, source):
        with open(source, "r", encoding="utf-8") as file:
            html = file.read()

        soup = BeautifulSoup(html, "html.parser")
        results = []

        for quote_box in soup.select("div.quote"):
            quote = quote_box.select_one("span.text").get_text(strip=True)
            author = quote_box.select_one("small.author").get_text(strip=True)

            results.append({
                "quote": quote,
                "author": author,
            })

        return results


# Concrete Product 4 - Offline Books
class OfflineBookScraper(WebScraper):
    def scrape(self, source):
        with open(source, "r", encoding="utf-8") as file:
            html = file.read()

        soup = BeautifulSoup(html, "html.parser")
        results = []

        for book_box in soup.select("article.product_pod"):
            title = book_box.select_one("h3 a")["title"]
            price = book_box.select_one("p.price_color").get_text(strip=True)

            results.append({
                "title": title,
                "price": price,
            })

        return results
