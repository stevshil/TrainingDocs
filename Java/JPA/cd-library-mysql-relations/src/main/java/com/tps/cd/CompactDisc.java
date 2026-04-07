package com.tps.cd;

import jakarta.persistence.*;
import java.util.List;
import java.util.ArrayList;

@Entity
@Table(name = "compact_disc")
public class CompactDisc {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;

    private String artist;

    private Double price;

    @OneToMany(mappedBy = "compactDisc", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Track> tracks = new ArrayList<>();

    public List<Track> getTracks() {
        return tracks;
    }

    public void addTrack(Track track) {
        tracks.add(track);
    }

    public CompactDisc() {}

    public CompactDisc(String title, String artist, Double price) {
        this.title = title;
        this.artist = artist;
        this.price = price;
    }

    // Getters and setters
    public Long getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getArtist() {
        return artist;
    }

    public Double getPrice() {
        return price;
    }
}
