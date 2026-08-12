package swapi.entity;

import com.google.gson.annotations.SerializedName;

public class Film {

    @SerializedName(value = "id", alternate = {"episode_id"})
    private int id;

    private String title;
    private String release_date;

    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getReleaseYear() {
        // release_date format: "1977-05-25"
        return release_date.split("-")[0];
    }
}
