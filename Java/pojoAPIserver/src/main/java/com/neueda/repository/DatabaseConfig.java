package com.neueda.repository;

import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;

import javax.sql.DataSource;

public class DatabaseConfig {

    public static DataSource createDataSource() {
        String url = System.getenv().getOrDefault("DB_URL",
                "jdbc:mysql://localhost:3306/products_db");
        String user = System.getenv().getOrDefault("DB_USER", "root");
        String passwd = System.getenv("DB_PASS");

        HikariConfig config = new HikariConfig();
        config.setJdbcUrl(url);
        config.setUsername(user);
        config.setPassword(passwd);
        config.setMaximumPoolSize(10);

        return new HikariDataSource(config);
    }
}
