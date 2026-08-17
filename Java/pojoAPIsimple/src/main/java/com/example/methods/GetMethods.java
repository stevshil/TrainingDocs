package com.example.methods;

import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;

public class GetMethods {
    public static void handleGet(HttpExchange exchange, String path) throws IOException {
        try {
            if (!exchange.getRequestMethod().equals("GET")) {
                exchange.sendResponseHeaders(405, -1);
                return;
            }
        } catch (IOException e) {
            String jsonerror = "{ \"error\": \"Failed in GET method\" }";
            exchange.sendResponseHeaders(500, jsonerror.length());
            exchange.getResponseBody().write(jsonerror.getBytes());
            exchange.getResponseBody().close();
        }

        // Check which endpoint (or uri) is being requested
        if ( path.equals("/users")) {
            // Then return all users
            String response = "{ \"output\": \"All users returned\" }";
            exchange.getResponseHeaders().add("Content-Type", "application/json");
            exchange.sendResponseHeaders(200, response.length());

            try {
                OutputStream os = exchange.getResponseBody();
                os.write(response.getBytes());
            } catch (IOException e) {
                System.err.println("Problem sending response");
                throw new RuntimeException(e);
            }
            return;
        } else if ( path.matches("/users/\\d+")) {
            // The return the data for the user matching value supplied
            // Example /users/1,  \d+ matches 1
            String[] parts = path.split("/");
            String response = "{ \"output\": \"Data for user " + parts[2] + "\" }";
            exchange.getResponseHeaders().add("Content-Type", "application/json");
            exchange.sendResponseHeaders(200, response.length());

            try {
                OutputStream os = exchange.getResponseBody();
                os.write(response.getBytes());
            } catch (IOException e) {
                System.err.println("Problem sending response");
                throw new RuntimeException(e);
            }
            return;
        } else if ( path.matches( "/users/\\s+")) {
            // Searches for users by name
            String response = "{\"output\": \"Some user by name\" }";
            exchange.getResponseHeaders().add("Content-Type", "application/json");
            exchange.sendResponseHeaders(200, response.length());

            try {
                OutputStream os = exchange.getResponseBody();
                os.write(response.getBytes());
            } catch (IOException e) {
                System.err.println("Problem sending response");
                throw new RuntimeException(e);
            }
            return;
        }
    }
}
