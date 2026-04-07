package com.tps.cd.dao;

import com.tps.cd.model.Track;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface TrackRepository extends JpaRepository<Track, Long> {
    List<Track> findByCompactDiscId(Long compactDiscId);
}
