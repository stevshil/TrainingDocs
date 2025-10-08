package com.tps.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ApiController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello, world!";
    }

    @GetMapping("/secured")
    public String secured() {
        return "This is a secured endpoint.";
    }

    @GetMapping("/admin")
    public String admin() {
        return "Welcome, admin!";
    }

    @GetMapping("/user")
    public String user() {
        return "Welcome, user!";
    }
}