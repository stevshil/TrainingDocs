package swapi.controller;

import com.google.gson.Gson;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import swapi.methods.Errors;
import swapi.SwapiClient;
import swapi.methods.DeleteMethods;
import swapi.methods.GetMethods;
import swapi.methods.PostMethods;

import java.io.IOException;

public class FilmsHandler implements HttpHandler {

    private final SwapiClient client = new SwapiClient();
    private final Gson gson = new Gson();
    // Handle Get
    private final GetMethods getmethods = new GetMethods();
    private final PostMethods postmethods = new PostMethods();
    private final DeleteMethods deletemethods = new DeleteMethods();
    private final Errors errors = new Errors();

    @Override
    public void handle(HttpExchange exchange) throws IOException {
        try {
            String method = exchange.getRequestMethod();

            switch (method) {
                case "GET":
                    getmethods.handleGet(exchange);
                    break;

                case "POST":
                    postmethods.handlePost(exchange);
                    break;

                case "DELETE":
                    deletemethods.handleDelete(exchange);
                    break;

                default:
                    errors.sendError(exchange, "Failed to fetch films");
            }
        } catch (Exception e) {
            String error = "{\"error\":\"Failed to fetch films\"}";
            exchange.sendResponseHeaders(500, error.getBytes().length);
            exchange.getResponseBody().write(error.getBytes());
            exchange.getResponseBody().close();
        }
    }
}
