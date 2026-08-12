package swapi;

import com.sun.net.httpserver.HttpServer;
import swapi.controller.FilmsHandler;

import java.io.IOException;
import java.net.InetSocketAddress;

public class APIOutput {

    public void RunServer() throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        server.createContext("/api/swfilms", new FilmsHandler());
        server.setExecutor(null);
        server.start();
        System.out.println("Server running on port8080");
    }
}
