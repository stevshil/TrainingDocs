package com.adp.secdemo.controller;

import java.util.Map;

import com.adp.secdemo.repository.UsersRepository;
import com.adp.secdemo.service.JwtService;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

@RestController
public class OpenAccess {
    private final UsersRepository usersRepository;
    private final JwtService jwtService;

    public OpenAccess(UsersRepository usersRepository, JwtService jwtService) {
        this.usersRepository = usersRepository;
        this.jwtService = jwtService;
    }

    @GetMapping("/")
    public ResponseEntity<Map<String, String>> openAccess() {
        return ResponseEntity.ok(Map.of("message", "This requires no security", "status", "ok"));
    }

    @PostMapping(value = "/login", consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Map<String, Object>> login(@RequestBody LoginRequest request) {
        if (request.username() == null || request.username().isBlank()
                || request.password() == null || request.password().isBlank()) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Username and password are required");
        }

        usersRepository.findById(request.username())
                .filter(user -> request.password().equals(user.getPassword()))
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Invalid credentials"));

        return ResponseEntity.ok(jwtService.createLoginResponse(request.username()));
    }

    public record LoginRequest(String username, String password) {
    }

}
