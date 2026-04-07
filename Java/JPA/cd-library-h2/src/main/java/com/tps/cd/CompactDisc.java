package com.tps.cd;

import jakarta.persistence.*;

@Entity
@Table(name = "compact_disc")
public class CompactDisc {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;

    private String artist;

    private Double price;

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
