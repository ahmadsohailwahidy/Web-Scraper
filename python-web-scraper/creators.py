from abc import ABC, abstractmethod
from scrapers import (WebScraper, QuoteScraper, BookScraper)

class ScraperCreator(ABC):

    @abstractmethod
    def create_scraper(self) -> WebScraper:
        pass


    def run_scraper(self, url):

        scraper = self.create_scraper()

        print(
            f"\nFactory created: "
            f"{scraper.__class__.__name__}"
        )

        return scraper.scrape(url)


class QuoteScraperCreator(ScraperCreator):

    def create_scraper(self) -> WebScraper:
        return QuoteScraper()


class BookScraperCreator(ScraperCreator):

    def create_scraper(self) -> WebScraper:
        return BookScraper()

    