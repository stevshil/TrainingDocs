package com.tps.myapp.services;

import org.springframework.stereotype.Service;

@Service
public class testServices {

    public String getSimple() {
        return "{\"output\": \"This is a test endpoint\"}";
    }
    
    public String getUsername(String username) {
        return "{\"output\": \"This is a test endpoint "+ username +"\"}";
    }
}
