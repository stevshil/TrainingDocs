package com.tps.cd;

import jakarta.persistence.*;

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
    private CompactDisc compactDisc;

    public Track() {}

    public Track(String title, int trackNumber, CompactDisc compactDisc) {
        this.title = title;
        this.trackNumber = trackNumber;
        this.compactDisc = compactDisc;
    }

    public Long getId() { return id; }
    public String getTitle() { return title; }
    public int getTrackNumber() { return trackNumber; }
    public CompactDisc getCompactDisc() { return compactDisc; }
}
