package com.adp.secdemo.Config;

import com.adp.secdemo.entity.Users;
import com.adp.secdemo.repository.UsersRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

@Component
public class DatabaseInitializer implements CommandLineRunner {

    private final UsersRepository usersRepository;

    public DatabaseInitializer(UsersRepository usersRepository) {
        this.usersRepository = usersRepository;
    }

    @Override
    @Transactional
    public void run(String... args) {
        if (!usersRepository.existsById("admin")) {
            usersRepository.save(new Users("admin", "admin"));
        }
    }
}
