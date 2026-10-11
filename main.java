
import java.nio.file.Path;
import java.util.Scanner;

class Main{

    private static final boolean OFFLINE_MODE = false;

    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

    System.out.println("====================================");
        System.out.println(" FACTORY METHOD - WEB SCRAPER DEMO ");
        System.out.println("====================================");
        System.out.println("1. Scrape Factory Method page on Wikipedia");
        System.out.println("2. Scrape Quotes to Scrape");
        System.out.print("Choose an option: ");

        int choice = scanner.nextInt();

        ScrapingTask task;
        String source;

        if (choice == 1) {
            task = new WikipediaScrapingTask();
            source = OFFLINE_MODE
                    ? Path.of("demo-data/wikipedia.html").toUri().toString()
                    : "https://en.wikipedia.org/wiki/Factory_method_pattern";
        } else if (choice == 2 ) {
            task = new QuotesScrapingTask();
            source = OFFLINE_MODE
                    ? Path.of("demo-data/quotes.html").toUri().toString()
                    : "https://quotes.toscrape.com/";
        } else {
            System.out.println("Invalid choice. Exiting.");
            scanner.close();
            return;
        }

        try {
            task.run(source);
        } catch (Exception e) {
              System.out.println("\nCould not scrape the source.");
            System.out.println("Reason: " + e.getMessage());
            System.out.println("Tip: If classroom internet is unavailable, set OFFLINE_MODE to true.");
        }

        scanner.close();
    }
}

