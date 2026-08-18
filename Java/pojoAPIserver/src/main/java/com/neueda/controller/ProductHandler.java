package com.neueda.controller;

import com.google.gson.Gson;
import com.neueda.model.Product;
import com.neueda.service.ProductService;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.IOException;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;
import java.util.Optional;

public class ProductHandler implements HttpHandler {

    private final ProductService service;
    private final Gson gson = new Gson();

    public ProductHandler(ProductService service) {
        this.service = service;
    }

    @Override
    public void handle(HttpExchange exchange) throws IOException {
        String method = exchange.getRequestMethod();
        String path   = exchange.getRequestURI().getPath();

        if (method.equals("GET") && path.equals("/api/products")) {
            handleGetAll(exchange);
            return;
        }

        if (method.equals("GET") && path.matches("/api/products/\\d+")) {
            handleGetOne(exchange, extractId(path));
            return;
        }

        if (method.equals("POST") && path.equals("/api/products")) {
            handleCreate(exchange);
            return;
        }

        if (method.equals("PUT") && path.matches("/api/products/\\d+")) {
            handleUpdate(exchange, extractId(path));
            return;
        }

        if (method.equals("DELETE") && path.matches("/api/products/\\d+")) {
            handleDelete(exchange, extractId(path));
            return;
        }

        sendResponse(exchange, 404, "{\"error\":\"Not found\"}");
    }

    private void handleGetAll(HttpExchange exchange) throws IOException {
        try {
            var products = service.getAllProducts();
            sendResponse(exchange, 200, gson.toJson(products));
        } catch (Exception e) {
            sendResponse(exchange, 500, "{\"error\":\"Server error\"}");
        }
    }

    private void handleGetOne(HttpExchange exchange, int id) throws IOException {
        try {
            Optional<Product> product = service.getProductById(id);
            if (product.isPresent()) {
                sendResponse(exchange, 200, gson.toJson(product.get()));
            } else {
                sendResponse(exchange, 404, "{\"error\":\"Product not found\"}");
            }
        } catch (Exception e) {
            sendResponse(exchange, 500, "{\"error\":\"Server error\"}");
        }
    }

    private void handleCreate(HttpExchange exchange) throws IOException {
        try {
            String body = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
            Product product = gson.fromJson(body, Product.class);

            Product created = service.createProduct(product);
            sendResponse(exchange, 201, gson.toJson(created));

        } catch (Exception e) {
            sendResponse(exchange, 400, "{\"error\":\"Invalid request\"}");
        }
    }

    private void handleUpdate(HttpExchange exchange, int id) throws IOException {
        try {
            Optional<Product> existing = service.getProductById(id);
            if (existing.isEmpty()) {
                sendResponse(exchange, 404, "{\"error\":\"Product not found\"}");
                return;
            }

            String body = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
            Product updated = gson.fromJson(body, Product.class);
            updated.setId(id);

            Product saved = service.updateProduct(updated);
            sendResponse(exchange, 200, gson.toJson(saved));

        } catch (Exception e) {
            sendResponse(exchange, 400, "{\"error\":\"Invalid request\"}");
        }
    }

    private void handleDelete(HttpExchange exchange, int id) throws IOException {
        try {
            boolean deleted = service.deleteProduct(id);
            if (deleted) {
                sendResponse(exchange, 204, "");
            } else {
                sendResponse(exchange, 404, "{\"error\":\"Product not found\"}");
            }
        } catch (Exception e) {
            sendResponse(exchange, 500, "{\"error\":\"Server error\"}");
        }
    }

    private int extractId(String path) {
        String[] parts = path.split("/");
        return Integer.parseInt(parts[3]); // /api/products/5 → ["", "api", "products", "5"]
    }

    private void sendResponse(HttpExchange exchange, int status, String body)
            throws IOException {

        byte[] bytes = body.getBytes(StandardCharsets.UTF_8);
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
