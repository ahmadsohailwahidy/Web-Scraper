from creators import ScraperCreator

from scrapers import WebScraper

from offline_scrapers import OfflineQuoteScraper, OfflineBookScraper

class OfflineQuoteScraperCreator(ScraperCreator):

    def create_scraper(self) -> WebScraper:
        return OfflineQuoteScraper()

class OfflineBookScraperCreator(ScraperCreator):

    def create_scraper(self) -> WebScraper:
        return OfflineBookScraper()

        