import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class QuotesScraper implements WebScraper {

    @Override
    public void scrape(String source) throws Exception {
        System.out.println("[QuotesScraper] Downloading page...");

        String html = HtmlFetcher.fetch(source);

        Pattern quotePattern = Pattern.compile(
                "<span[^>]*class=[\"']text[\"'][^>]*>(.*?)</span>",
                Pattern.CASE_INSENSITIVE | Pattern.DOTALL
        );

        Pattern authorPattern = Pattern.compile(
                "<small[^>]*class=[\"']author[\"'][^>]*>(.*?)</small>",
                Pattern.CASE_INSENSITIVE | Pattern.DOTALL
        );

        Matcher quoteMatcher = quotePattern.matcher(html);
        Matcher authorMatcher = authorPattern.matcher(html);

        int count = 0;
        String firstQuote = "Not found";
        String firstAuthor = "Not found";

        while (quoteMatcher.find()) {
            count++;
            if (count == 1) {
                firstQuote = cleanText(quoteMatcher.group(1));
            }
        }

        if (authorMatcher.find()) {
            firstAuthor = cleanText(authorMatcher.group(1));
        }

        System.out.println("\n--- Quotes Result ---");
        System.out.println("Quotes found : " + count);
        System.out.println("First quote  : " + firstQuote);
        System.out.println("First author : " + firstAuthor);
    }

    private String cleanText(String text) {
        return text
                .replaceAll("<[^>]+>", " ")
                .replace("&amp;", "&")
                .replace("&quot;", "\"")
                .replace("&#39;", "'")
                .replace("&lt;", "<")
                .replace("&gt;", ">")
                .replace("&nbsp;", " ")
                .replaceAll("\\s+", " ")
                .trim();
    }
}
