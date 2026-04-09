package com.tps.multidbcdlibrary.controller;

import com.tps.multidbcdlibrary.model.CompactDisc;
import com.tps.multidbcdlibrary.repository.CompactDiscRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/cds")
public class CompactDiscController {

    private final CompactDiscRepository repository;

    public CompactDiscController(CompactDiscRepository repository) {
        this.repository = repository;
    }

    @GetMapping
    public List<CompactDisc> getAllCds() {
        return repository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<CompactDisc> getCdById(@PathVariable Long id) {
        return repository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public CompactDisc createCd(@RequestBody CompactDisc compactDisc) {
        return repository.save(compactDisc);
    }
}
