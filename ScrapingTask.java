public abstract class ScrapingTask {

    public abstract WebScraper createScraper();

    public void run(String source) throws Exception {

        WebScraper scraper = createScraper();
        
        System.out.println(
            "Factory method created. Scraper class: " + scraper.getClass().getSimpleName()
        );
        
        scraper.scrape(source);
    }
}
