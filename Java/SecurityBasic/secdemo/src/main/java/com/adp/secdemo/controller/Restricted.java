package com.adp.secdemo.controller;

import java.util.List;
import java.util.Map;

import com.adp.secdemo.repository.UsersRepository;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Restricted {
    private final UsersRepository usersRepository;

    public Restricted(UsersRepository usersRepository) {
        this.usersRepository = usersRepository;
    }

    @GetMapping("/users")
    public ResponseEntity<Map<String, Object>> getUsers() {
        List<Map<String, String>> users = usersRepository.findAll().stream()
                .map(user -> Map.of("username", user.getUsername()))
                .toList();
        if (users.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND)
                    .body(Map.of("code", 404, "message", "No users found"));
        }
        return ResponseEntity.ok(Map.of("code", 200, "users", users));
    }
}
