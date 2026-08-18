package com.neueda.controller;

import com.google.gson.Gson;
import com.neueda.model.Product;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.IOException;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

public class ProductHandler implements HttpHandler {

    // The object to import or export JSON strings
    private final Gson gson = new Gson();
    // An empty collection of products, which we hard code in this program, normally from a database
    private final Map<Integer, Product> store = new ConcurrentHashMap<>();
    // Create a new ID, something the database would normally do
    private final AtomicInteger nextId = new AtomicInteger(1);

    // This constructor is creating dummy data as we are not using a database yet
    public ProductHandler() {
        // 2 entries into our store collection
        store.put(1, new Product(1, "Laptop", 999.99));
        store.put(2, new Product(2, "Mouse", 29.99));
        nextId.set(3);
    }

    @Override
    // The method that needs to be implemented from HttpHandler
    // This will allow us to identify the method and path provided by the client request
    public void handle(HttpExchange exchange) throws IOException {
        // Gets the method past, either GET, POST, PUT, DELETE, etc
        String method = exchange.getRequestMethod();
        // Gets the URI of the requested resource, e.g. /api/products
        String path   = exchange.getRequestURI().getPath();

        // TODO: route to the correct handler method based on method and path
        // Hint: use path.matches("/api/products/\\d+") to detect ID-based routes
        if ( method.equals("GET") && path.equals("/api/products") ) {
            handleGetAll(exchange);
        } else if ( method.equals("GET") && path.matches("/api/products/\\d+") ) {
            handleGetOne(exchange, extractId(path));
        }
    }

    private void handleGetAll(HttpExchange exchange) throws IOException {
        // TODO: serialise all products and send a 200 response
        List<Product> products = new ArrayList<>(store.values());
        sendResponse(exchange, 200, gson.toJson(products));
    }

    private void handleGetOne(HttpExchange exchange, int id) throws IOException {
        // TODO: look up by id; send 200 with product JSON, or 404 if not found
    }

    private void handleCreate(HttpExchange exchange) throws IOException {
        // TODO: read body, deserialise, assign next ID, store and send 201
    }

    private void handleUpdate(HttpExchange exchange, int id) throws IOException {
        // TODO: return 404 if id missing; otherwise deserialise body,
        //       set id, replace in store, and send 200
    }

    private void handleDelete(HttpExchange exchange, int id) throws IOException {
        // TODO: remove from store; send 204 if removed, 404 if not found
    }

    private int extractId(String path) {
        // TODO: split path on "/" and parse the last segment as an int
        String[] parts = path.split("/");
        if ( parts.length > 3 ) {
            int id = Integer.parseInt(parts[3]);
            return id;
        }
        return 0;
    }

    private void sendResponse(HttpExchange exchange, int status, String body)
            throws IOException {
        byte[] bytes = body.getBytes();
        exchange.getResponseHeaders().set("Content-Type", "application/json");
        exchange.sendResponseHeaders(status, bytes.length == 0 ? -1 : bytes.length);
        if (bytes.length > 0) {
            try (OutputStream os = exchange.getResponseBody()) {
                os.write(bytes);
            }
        } else {
            exchange.getResponseBody().close();
        }
    }
}
