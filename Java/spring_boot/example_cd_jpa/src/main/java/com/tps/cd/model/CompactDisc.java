package com.tps.cd.model;

import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonManagedReference;

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
    @JsonManagedReference
    private List<Track> tracks = new ArrayList<>();


    public CompactDisc() {}

    public CompactDisc(String title, String artist, Double price) {
        this.title = title;
        this.artist = artist;
        this.price = price;
    }

    public Long getId() { return id; }
    public String getTitle() { return title; }
    public String getArtist() { return artist; }
    public Double getPrice() { return price; }
    public List<Track> getTracks() { return tracks; }

    public void setTitle(String title) { this.title = title; }
    public void setArtist(String artist) { this.artist = artist; }
    public void setPrice(Double price) { this.price = price; }

    public void addTrack(Track track) {
        tracks.add(track);
        track.setCompactDisc(this);
    }

    public void removeTrack(Track track) {
        tracks.remove(track);
        track.setCompactDisc(null);
    }
}
