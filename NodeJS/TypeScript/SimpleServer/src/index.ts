import { callApi } from "./callapi";
import { Film } from "../Types/Film";

const fetchFilms = async (): Promise<void> => {
  try {
    const films = await callApi<Film[]>("films");
    console.log("Star Wars Films:");
    films.forEach((film) => {
      console.log(
        `Episode ${film.episode_id}: ${film.title} (Directed by ${film.director}, Released: ${film.release_date})`
      );
    });
  } catch (error) {
    console.error("Failed to fetch films:", error);
  }
};

fetchFilms();
