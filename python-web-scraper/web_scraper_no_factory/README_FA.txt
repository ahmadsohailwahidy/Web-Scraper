نسخه بدون Factory

در این نسخه هیچ Factory نداریم.

main.py خودش تصمیم می‌گیرد و خودش object را می‌سازد:

    if mode == "1" and choice == "1":
        scraper = QuoteScraper()

    elif mode == "1" and choice == "2":
        scraper = BookScraper()

یعنی مسئولیت انتخاب و ساخت Concrete Product مستقیماً در main.py است.

این نسخه برای مقایسه بسیار مهم است چون نشان می‌دهد Factory قرار است مسئولیت object creation را از Client جدا کند.

اجرا:
    python main.py

برای حالت آفلاین:
    Mode = 2
    سپس 1 برای Quotes یا 2 برای Books
