package com.neueda.controller;

import com.google.gson.Gson;
import com.neueda.model.Product;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import javax.sql.DataSource;
import java.io.IOException;
import java.io.OutputStream;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

public class ProdHandler implements HttpHandler {

    // The object to import or export JSON strings
    private final Gson gson = new Gson();
    private final DataSource dataSource;

    // This constructor is creating dummy data as we are not using a database yet
    public ProdHandler(DataSource dataSource) {
        this.dataSource = dataSource;
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
        String sql = "SELECT * FROM products";
        List<Product> products = new ArrayList<>();

        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                products.add(mapRow(rs));
            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        sendResponse(exchange, 200, gson.toJson(products));
    }

    // Added as we need a mapper of values for product
    private Product mapRow(ResultSet rs) throws SQLException {
        return new Product(
                rs.getInt("id"),
                rs.getString("name"),
                rs.getDouble("price")
        );
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
