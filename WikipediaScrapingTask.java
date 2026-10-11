public class WikipediaScrapingTask extends ScrapingTask {

    @Override 
    public WebScraper createScraper() {
        return new WikipediaScraper();
    }
    
}
