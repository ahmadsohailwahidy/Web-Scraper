from pathlib import Path

from requests.exceptions import RequestException

from factory import ScraperFactory


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
    print("=" * 60)
    print("   SIMPLE FACTORY - WEB SCRAPER DEMO")
    print("=" * 60)

    print("1. Online mode")
    print("2. Offline mode")
    mode = input("\nChoose mode 1 or 2: ").strip()

    print("\n1. Scrape quotes")
    print("2. Scrape books")
    choice = input("\nChoose 1 or 2: ").strip()

    # SIMPLE FACTORY:
    # main.py asks one central factory to create the correct object.
    scraper = ScraperFactory.create_scraper(mode, choice)

    if scraper is None:
        print("Invalid choice.")
        return

    if mode == "1" and choice == "1":
        source = QUOTES_URL
    elif mode == "1" and choice == "2":
        source = BOOKS_URL
    elif mode == "2" and choice == "1":
        source = QUOTES_FILE
    else:
        source = BOOKS_FILE

    try:
        print(f"\nFactory created: {scraper.__class__.__name__}")
        results = scraper.scrape(source)
        show_results(results)

    except RequestException as error:
        print("\nNetwork error:")
        print(error)

    except FileNotFoundError as error:
        print("\nOffline HTML file was not found:")
        print(error)

    except Exception as error:
        print("\nSomething went wrong:")
        print(error)


if __name__ == "__main__":
    main()
