package swapi.methods;

import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;

public class Errors {
    public void sendError(HttpExchange exchange, String msg) throws IOException {
        String json = "{\"error\":\"" + msg + "\"}";
        exchange.sendResponseHeaders(500, json.length());
        exchange.getResponseBody().write(json.getBytes());
        exchange.getResponseBody().close();
    }
}
