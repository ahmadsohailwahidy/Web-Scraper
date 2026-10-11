public class QuotesScrapingTask extends ScrapingTask {

    @Override 
    public WebScraper createScraper() {
        return new QuotesScraper();
    }
    
}
