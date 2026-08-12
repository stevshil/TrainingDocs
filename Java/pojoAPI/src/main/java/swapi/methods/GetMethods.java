package swapi.methods;

import com.google.gson.Gson;
import com.sun.net.httpserver.HttpExchange;
import swapi.entity.Film;
import swapi.SwapiClient;

import java.io.IOException;
import java.util.List;

public class GetMethods {
    private final SwapiClient client = new SwapiClient();
    private final Gson gson = new Gson();
    Errors errors = new Errors();

    public void handleGet(HttpExchange exchange) throws IOException {
        try {
            if (!exchange.getRequestMethod().equals("GET")) {
                exchange.sendResponseHeaders(405, -1);
                return;
            }

            String path = exchange.getRequestURI().getPath();
            String[] parts = path.split("/");

            if (parts.length == 3) {
                // /api/swfilms
                handleGetAll(exchange);
            } else if (parts.length == 4) {
                // /api/swfilms/{id}
                handleGetById(exchange, parts[3]);
            } else {
                errors.sendError(exchange, "Invalid path");
            }

        } catch (Exception e) {
            errors.sendError(exchange, "Failed to fetch films");
        }
    }

    protected void handleGetAll(HttpExchange exchange) throws IOException {
        try {
            List<Film> films = client.getFilms();
            String json = gson.toJson(films);

            exchange.getResponseHeaders().add("Content-Type", "application/json");
            exchange.sendResponseHeaders(200, json.getBytes().length);
            exchange.getResponseBody().write(json.getBytes());
            exchange.getResponseBody().close();

        } catch (Exception e) {
            errors.sendError(exchange, "Failed to fetch films");
        }
    }

    private void handleGetById(HttpExchange exchange, String idStr) throws IOException {
        try {
            int id = Integer.parseInt(idStr);

            Film film = client.getFilms()
                    .stream()
                    .filter(f -> f.getId() == id)
                    .findFirst()
                    .orElse(null);

            String json = gson.toJson(film);

            exchange.getResponseHeaders().add("Content-Type", "application/json");
            exchange.sendResponseHeaders(200, json.getBytes().length);
            exchange.getResponseBody().write(json.getBytes());
            exchange.getResponseBody().close();

        } catch (Exception e) {
            errors.sendError(exchange, "Invalid film ID");
        }
    }
}
