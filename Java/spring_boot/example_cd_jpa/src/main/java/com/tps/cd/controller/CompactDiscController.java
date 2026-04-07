package com.tps.cd.controller;

import com.tps.cd.model.CompactDisc;
import com.tps.cd.model.Track;
import com.tps.cd.service.CompactDiscService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/cds")
public class CompactDiscController {

    private final CompactDiscService service;

    public CompactDiscController(CompactDiscService service) {
        this.service = service;
    }

    @GetMapping
    public List<CompactDisc> getAllCds() {
        return service.findAll();
    }

    @GetMapping("/{id}")
    public CompactDisc getCd(@PathVariable Long id) {
        return service.findById(id);
    }

    @PostMapping
    public CompactDisc createCd(@RequestBody CompactDisc cd) {
        return service.create(cd);
    }

    @GetMapping("/{id}/tracks")
    public List<Track> getTracks(@PathVariable Long id) {
        return service.findTracksForDisc(id);
    }

    @PostMapping("/{id}/tracks")
    public Track addTrack(@PathVariable Long id, @RequestBody Track track) {
        return service.addTrackToDisc(id, track);
    }
}
