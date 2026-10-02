package com.adp.secdemo;

import com.adp.secdemo.Config.DatabaseInitializer;
import com.adp.secdemo.entity.Users;
import com.adp.secdemo.repository.UsersRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest(properties = {
        "spring.datasource.url=jdbc:sqlite::memory:",
        "spring.datasource.hikari.maximum-pool-size=1",
        "spring.jpa.hibernate.ddl-auto=create-drop"
})
@Transactional
class SecdemoApplicationTests {

    @Autowired
    private UsersRepository usersRepository;

    @Autowired
    private DatabaseInitializer databaseInitializer;

    @Test
    void contextLoads() {
        assertEquals("admin", usersRepository.findById("admin").orElseThrow().getPassword());
    }

    @Test
    void createsAdminWhenMissing() {
        usersRepository.deleteAll();
        usersRepository.flush();

        databaseInitializer.run();
        usersRepository.flush();

        assertEquals("admin", usersRepository.findById("admin").orElseThrow().getPassword());
        assertEquals(1, usersRepository.count());
    }

    @Test
    void preservesExistingAdminOnRepeatedInitialization() {
        usersRepository.saveAndFlush(new Users("admin", "changed-password"));

        databaseInitializer.run();
        databaseInitializer.run();

        assertEquals("changed-password", usersRepository.findById("admin").orElseThrow().getPassword());
        assertEquals(1, usersRepository.count());
    }

}
