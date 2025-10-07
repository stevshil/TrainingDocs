package com.tps.myapp.controllers;

import org.springframework.beans.factory.annotation.Autowired;
// Important imports for REST APIs to help generate responses and receive requests
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.tps.myapp.services.testServices;

// Annotations that help define the class as a rest controller
@RestController
public class SimpleEndPoint {

    @Autowired
    private testServices testService;

    // No auth
    @GetMapping("/hello")
    public String hello() {
        return "Hello World";
    }

    // Below requires auth

    // Annotation defines the URI endpoint
    @GetMapping("/api/test")
    public ResponseEntity<String> returnJSON(){
        return new ResponseEntity<>(testService.getSimple(), HttpStatus.OK);
        // return new ResponseEntity<>("{\"output\": \"This is a test endpoint\"}", HttpStatus.OK);
    }

    @GetMapping("/api/test/{username}")
    public ResponseEntity<String> returnHello(@PathVariable("username") String username){
        return new ResponseEntity<>(testService.getUsername(username), HttpStatus.OK);
        // return new ResponseEntity<>("{\"output\": \"This is a test endpoint "+ username +"\"}", HttpStatus.OK);

    }
}
