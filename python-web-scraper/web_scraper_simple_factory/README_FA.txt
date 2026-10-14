نسخه Simple Factory

نکته اصلی:
main.py خودش QuoteScraper یا BookScraper را مستقیماً نمی‌سازد.
به جای آن می‌گوید:

    scraper = ScraperFactory.create_scraper(mode, choice)

سپس ScraperFactory با if/elif تصمیم می‌گیرد کدام object ساخته شود.

قلب Simple Factory:

    class ScraperFactory:
        @staticmethod
        def create_scraper(mode, choice):
            if ...:
                return QuoteScraper()
            elif ...:
                return BookScraper()

این یک Factory Method به سبک GoF نیست.
این یک Simple Factory است چون یک کلاس مرکزی با شرط‌ها نوع object را انتخاب می‌کند.

اجرا:
    python main.py

برای حالت آفلاین:
    Mode = 2
    سپس 1 برای Quotes یا 2 برای Books
