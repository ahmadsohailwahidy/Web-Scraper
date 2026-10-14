from bs4 import BeautifulSoup

from scrapers import WebScraper

class OfflineQuoteScraper(WebScraper):
    def scrape(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
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

class OfflineBookScraper(WebScraper):
    def scrape(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
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