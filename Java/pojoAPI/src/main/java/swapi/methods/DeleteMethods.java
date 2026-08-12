package swapi.methods;

import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;

public class DeleteMethods {
    public void handleDelete(HttpExchange exchange) throws IOException {
        String response = "{\"message\":\"DELETE received\"}";
        exchange.sendResponseHeaders(200, response.length());
        exchange.getResponseBody().write(response.getBytes());
        exchange.getResponseBody().close();
    }
}
