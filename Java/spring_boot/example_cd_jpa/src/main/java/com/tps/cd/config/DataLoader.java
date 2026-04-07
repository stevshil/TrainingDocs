package com.tps.cd.config;

import com.tps.cd.dao.CompactDiscRepository;
import com.tps.cd.model.CompactDisc;
import com.tps.cd.model.Track;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DataLoader {

    @Bean
    CommandLineRunner init(CompactDiscRepository repo) {
        return args -> {
            if (repo.count() == 0) {
                CompactDisc cd1 = new CompactDisc("Dark Side of the Moon", "Pink Floyd", 12.99);
                cd1.addTrack(new Track("Speak to Me", 1));
                cd1.addTrack(new Track("Breathe", 2));
                cd1.addTrack(new Track("Time", 3));

                CompactDisc cd2 = new CompactDisc("Thriller", "Michael Jackson", 14.99);
                cd2.addTrack(new Track("Wanna Be Startin' Somethin'", 1));
                cd2.addTrack(new Track("Thriller", 2));
                cd2.addTrack(new Track("Beat It", 3));

                repo.save(cd1);
                repo.save(cd2);
            }
        };
    }
}
