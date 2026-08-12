package swapi.methods;

import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;

public class PostMethods {
    public void handlePost(HttpExchange exchange) throws IOException {
        String response = "{\"message\":\"POST received\"}";
        exchange.sendResponseHeaders(200, response.length());
        exchange.getResponseBody().write(response.getBytes());
        exchange.getResponseBody().close();
    }
}
