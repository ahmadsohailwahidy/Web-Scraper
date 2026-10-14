from pathlib import Path

from requests.exceptions import RequestException

from creators import (QuoteScraperCreator, BookScraperCreator)

from offline_creators import OfflineQuoteScraperCreator, OfflineBookScraperCreator


QUOTES_URL = "https://quotes.toscrape.com/"
BOOKS_URL = "https://books.toscrape.com/"


BASE_DIR = Path(__file__).resolve().parent
QUOTES_FILE = BASE_DIR / "pages" / "quotes.html"
BOOKS_FILE = BASE_DIR / "pages" / "books.html"

def show_results(results):

    print(f"\nItems found: {len(results)}")

    print("Showing the first 5 items:\n")

    for number, item in enumerate(results[:5], start=1):

        print(f"{number}. {item}")


def main():

    print("=" * 55)
    print("    FACTORY METHOD - WEB SCRAPER DEMO")
    print("=" * 55)

    print("1. Online mode")
    print("2. Offline mode")

    mode = input("\nChoose 1 or 2: ").strip()


    print("1. Scrape quotes")
    print("2. Scrape books")

    choice = input("\nChoose 1 or 2: ").strip()

    if mode == "1":
        if choice == "1":
            creator = QuoteScraperCreator()
            source = QUOTES_URL
        elif choice == "2":
            creator = BookScraperCreator()
            source = BOOKS_URL
        else:
            print("Invalid choice. Exiting.")
            return
    elif mode == "2":
        if choice == "1":
            creator = OfflineQuoteScraperCreator()
            source = QUOTES_FILE
        elif choice == "2":
            creator = OfflineBookScraperCreator()
            source = BOOKS_FILE
        else:
            print("Invalid scraper choice")
            return
    else:
        print("Invalid mode choice")
        return

    try:
        results = creator.run_scraper(source)
        show_results(results)
    except RequestException as error:
        print("\nNetwork error:")
        print(error)

        #useful when an offline HTML file is missing
    except FileNotFoundError as error:
        print("\nOffline HTML file was not found:")
        print(error)

    except Exception as error:
        print("\nSomething went wrong:")
        print(error)

if __name__ == "__main__":
    main()