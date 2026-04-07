package com.tps.cd.model;

import jakarta.persistence.*;
import com.fasterxml.jackson.annotation.JsonBackReference;

@Entity
@Table(name = "track")
public class Track {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;
    private int trackNumber;

    @ManyToOne
    @JoinColumn(name = "compact_disc_id", nullable = false)
    @JsonBackReference // Prevents recursive nesting
    private CompactDisc compactDisc;

    public Track() {}

    public Track(String title, int trackNumber) {
        this.title = title;
        this.trackNumber = trackNumber;
    }

    public Long getId() { return id; }
    public String getTitle() { return title; }
    public int getTrackNumber() { return trackNumber; }
    public CompactDisc getCompactDisc() { return compactDisc; }

    public void setTitle(String title) { this.title = title; }
    public void setTrackNumber(int trackNumber) { this.trackNumber = trackNumber; }
    public void setCompactDisc(CompactDisc compactDisc) { this.compactDisc = compactDisc; }
}
