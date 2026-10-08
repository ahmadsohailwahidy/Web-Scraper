import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Path;

public class HtmlFetcher {

    private static final HttpClient CLIENT = HttpClient.newBuilder()
            .followRedirects(HttpClient.Redirect.NORMAL)
            .build();

    public static String fetch(String source) throws IOException, InterruptedException {
        if (source.startsWith("file:")) {
            return Files.readString(Path.of(URI.create(source)));
        }

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(source))
                .header("User-Agent", "FactoryMethodClassDemo/1.0")
                .GET()
                .build();

        HttpResponse<String> response = CLIENT.send(
                request,
                HttpResponse.BodyHandlers.ofString()
        );

        if (response.statusCode() >= 400) {
            throw new IOException("Website returned HTTP " + response.statusCode());
        }

        return response.body();
    }
}
