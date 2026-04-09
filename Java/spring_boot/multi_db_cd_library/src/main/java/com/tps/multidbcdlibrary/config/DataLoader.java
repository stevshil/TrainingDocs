package com.tps.multidbcdlibrary.config;

import com.tps.multidbcdlibrary.model.CompactDisc;
import com.tps.multidbcdlibrary.repository.CompactDiscRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class DataLoader implements CommandLineRunner {

    private final CompactDiscRepository repository;

    public DataLoader(CompactDiscRepository repository) {
        this.repository = repository;
    }

    @Override
    public void run(String... args) {
        repository.save(new CompactDisc("Greatest Hits", "Example Band", 12.50));
        repository.save(new CompactDisc("Acoustic Sessions", "Studio Artist", 9.99));
    }
}
