package com.example;

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
            String response = "Woohoo it's Friday!";
            exchange.getResponseHeaders().add("Content-Type", "text/plain");
            exchange.sendResponseHeaders(200, response.length());

            try {
                OutputStream os = exchange.getResponseBody();
                os.write(response.getBytes());
            } catch (IOException e) {
                System.err.println("Problem sending response");
                throw new RuntimeException(e);
            }
        }
    }
}
