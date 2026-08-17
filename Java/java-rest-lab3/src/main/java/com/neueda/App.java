package com.neueda;

import com.neueda.controller.CustomerHandler;
import com.neueda.controller.ProductHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;

public class App {
    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        server.createContext("/api/products", new ProductHandler());
        server.createContext("/api/customers", new CustomerHandler());
        server.setExecutor(null);
        server.start();

        System.out.println("Server running on port 8080");
    }
}
