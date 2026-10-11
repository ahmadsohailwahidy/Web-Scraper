import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class WikipediaScraper implements WebScraper {

    @Override
    public void scrape(String source) throws Exception {
        System.out.println("[WikipediaScraper] Downloading page...");

        String html = HtmlFetcher.fetch(source);

        String title = findFirst(
                html,
                "<title>(.*?)</title>"
        );

        String firstParagraph = findFirstUsefulParagraph(html);
        int linkCount = countMatches(html, "<a\\s+[^>]*href=");

        System.out.println("\n--- Wikipedia Result ---");
        System.out.println("Title      : " + cleanText(title));
        System.out.println("Paragraph  : " + cleanText(firstParagraph));
        System.out.println("Link count : " + linkCount);
    }

    private String findFirst(String text, String regex) {
        Pattern pattern = Pattern.compile(
                regex,
                Pattern.CASE_INSENSITIVE | Pattern.DOTALL
        );
        Matcher matcher = pattern.matcher(text);

        if (matcher.find()) {
            return matcher.group(1);
        }
        return "Not found";
    }

    private String findFirstUsefulParagraph(String html) {
        Pattern pattern = Pattern.compile(
                "<p(?:\\s[^>]*)?>(.*?)</p>",
                Pattern.CASE_INSENSITIVE | Pattern.DOTALL
        );
        Matcher matcher = pattern.matcher(html);

        while (matcher.find()) {
            String paragraph = cleanText(matcher.group(1));
            if (paragraph.length() > 40) {
                return paragraph;
            }
        }
        return "No useful paragraph found";
    }

    private int countMatches(String text, String regex) {
        Pattern pattern = Pattern.compile(regex, Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(text);

        int count = 0;
        while (matcher.find()) {
            count++;
        }
        return count;
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
