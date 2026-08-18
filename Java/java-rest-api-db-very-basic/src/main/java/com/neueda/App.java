package com.neueda;

import com.neueda.config.DatabaseConfig;
import com.neueda.controller.CustomerHandler;
//import com.neueda.controller.ProdHandler;
import com.neueda.controller.ProductHandler;
import com.neueda.controller.ProductsHandler;
import com.sun.net.httpserver.HttpServer;

import javax.sql.DataSource;
import java.io.IOException;
import java.net.InetSocketAddress;

public class App {
    public static void main(String[] args) throws IOException {
        // Add database
        DataSource dataSource = DatabaseConfig.createDataSource();

        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        // The old in memory service
        // server.createContext("/api/products", new ProductHandler());
        server.createContext("/api/products", new ProductsHandler(dataSource));
        server.createContext("/api/customers", new CustomerHandler());
        server.setExecutor(null);
        server.start();

        System.out.println("Server running on port 8080");
    }
}
