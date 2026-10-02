package com.adp.secdemo.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
public class Users {

    @Id
    private String username;

    private String password;

//    @Column(nullable = true)
//    private boolean disable;

    protected Users() {
    }

    public Users(String username, String password) {
        this.username = username;
        this.password = password;
    }
}
