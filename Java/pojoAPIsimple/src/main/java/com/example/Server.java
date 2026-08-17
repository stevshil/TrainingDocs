package com.example;

import com.example.methods.GetMethods;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class Server {
    public static void main(String[] args) {

        try {
            HttpServer server = HttpServer.create(
                    new InetSocketAddress(8080), 0
            );

            server.createContext("/", new RootHandler());
            server.setExecutor(null);
            server.start();

            System.out.println("Server running on port 8080");

        } catch (IOException e) {
            System.err.println("Possible port issue, port 8080 might be in use");
            throw new RuntimeException(e);
        }
    }

    static class RootHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {

            // Is what was sent a GET, POST, PUT or DELETE?
            String method = exchange.getRequestMethod();
            // What is the endpoint requested, e.g. /users, or /users/1, or /products
            String path = exchange.getRequestURI().getPath();

            switch(method) {
                case "GET": // READ (SELECT)
                    /* Calling as an object
                    GetMethods gets = new GetMethods();
                    gets.handleGet(exchange, path);
                     */

                    // Calling as a class method
                    GetMethods.handleGet(exchange, path);
                case "POST": // CREATE (INSERT)
                case "PUT": // UPDATE
                case "DELETE": // DELETE
            }

//            String response = "<h1>Woohoo it's Friday!</h1>";
//            exchange.getResponseHeaders().add("Content-Type", "text/html");
//            String response = "{\"name\": \"Steve\", \"age\": 21}";
//            exchange.getResponseHeaders().add("Content-Type", "application/json");
//            exchange.sendResponseHeaders(200, response.length());
//
//            try {
//                OutputStream os = exchange.getResponseBody();
//                os.write(response.getBytes());
//            } catch (IOException e) {
//                System.err.println("Problem sending response");
//                throw new RuntimeException(e);
//            }
        }
    }
}
