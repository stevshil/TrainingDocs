package swapi;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import swapi.entity.Film;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Type;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.List;

public class SwapiClient {

    public List<Film> getFilms() throws Exception {
        URL url = new URL("https://swapi.info/api/films");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");

        BufferedReader reader =
                new BufferedReader(new InputStreamReader(conn.getInputStream()));

        StringBuilder sb = new StringBuilder();
        String line;

        while ((line = reader.readLine()) != null) {
            sb.append(line);
        }

        reader.close();

        Gson gson = new Gson();
        // TypeToken to deserialise the list into a "generic" type List of Film objects
        Type listType = new TypeToken<List<Film>>() {}.getType();

        // Returns the downloaded data as a Java object, in this case a List<Film> object
        // sb contains the raw JSON
        // listType tells Gson what type to create, as defined above.
        return gson.fromJson(sb.toString(), listType);
    }
}
