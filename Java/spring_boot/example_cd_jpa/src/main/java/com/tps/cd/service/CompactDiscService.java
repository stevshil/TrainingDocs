package com.tps.cd.service;

import com.tps.cd.dao.CompactDiscRepository;
import com.tps.cd.dao.TrackRepository;
import com.tps.cd.model.CompactDisc;
import com.tps.cd.model.Track;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CompactDiscService {

    private final CompactDiscRepository cdRepo;
    private final TrackRepository trackRepo;

    public CompactDiscService(CompactDiscRepository cdRepo, TrackRepository trackRepo) {
        this.cdRepo = cdRepo;
        this.trackRepo = trackRepo;
    }

    public List<CompactDisc> findAll() {
        return cdRepo.findAll();
    }

    public CompactDisc findById(Long id) {
        return cdRepo.findById(id).orElseThrow(() -> new RuntimeException("CD not found: " + id));
    }

    public CompactDisc create(CompactDisc cd) {
        // cascade will save tracks if they’re attached
        return cdRepo.save(cd);
    }

    public List<Track> findTracksForDisc(Long cdId) {
        return trackRepo.findByCompactDiscId(cdId);
    }

    public Track addTrackToDisc(Long cdId, Track track) {
        CompactDisc cd = findById(cdId);
        cd.addTrack(track);
        cdRepo.save(cd);
        return track;
    }
}
