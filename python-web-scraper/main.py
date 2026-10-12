from creators import (QuoteScraperCreator, BookScraperCreator)

QUOTES_URL = "https://quotes.toscrape.com/"
BOOKS_URL = "https://books.toscrape.com/"


def show_results(results):

    print(f"\nItems found: {len(results)}")

    print("Showing the first 5 items:\n")

    for number, item in enumerate(results[:5], start=1):

        print(f"{number}. {item}")


def main():

    print("1. Scrape quotes")
    print("2. Scrape books")

    choice = input("\nChoose 1 or 2: ").strip()

    if choice == "1":
        creator = QuoteScraperCreator()
        url = QUOTES_URL
    elif choice == "2":
        creator = BookScraperCreator()
        url = BOOKS_URL

    results = creator.run_scraper(url)