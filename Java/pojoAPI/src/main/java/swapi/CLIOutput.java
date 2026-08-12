package swapi;

import swapi.entity.Film;

import java.util.List;

public class CLIOutput {
    public static void ShowFilms() throws Exception {
        SwapiClient client = new SwapiClient();
        List<Film> films = client.getFilms();

        for (Film f : films) {
            System.out.println(f.getTitle() + " (" + f.getReleaseYear() + ")");
        }
    }
}
