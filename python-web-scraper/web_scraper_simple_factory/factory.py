from scrapers import (
    QuoteScraper,
    BookScraper,
    OfflineQuoteScraper,
    OfflineBookScraper,
)


class ScraperFactory:
    """
    SIMPLE FACTORY

    One central class decides which concrete scraper object to create.
    """

    @staticmethod
    def create_scraper(mode, choice):

        if mode == "1" and choice == "1":
            return QuoteScraper()

        elif mode == "1" and choice == "2":
            return BookScraper()

        elif mode == "2" and choice == "1":
            return OfflineQuoteScraper()

        elif mode == "2" and choice == "2":
            return OfflineBookScraper()

        else:
            return None
