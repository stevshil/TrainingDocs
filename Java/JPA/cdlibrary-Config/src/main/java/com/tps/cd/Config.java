package com.tps.cd;

import jakarta.persistence.EntityManagerFactory;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistry;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public final class Config {
    private Config() {}

    public static EntityManagerFactory createEntityManagerFactory() {
        Properties properties = loadProperties();
        Properties hibernateSettings = new Properties();
        hibernateSettings.setProperty("hibernate.connection.driver_class",
                required(properties, "spring.datasource.driver-class-name"));
        hibernateSettings.setProperty("hibernate.connection.url",
                required(properties, "spring.datasource.url"));
        hibernateSettings.setProperty("hibernate.connection.username",
                required(properties, "spring.datasource.username"));
        hibernateSettings.setProperty("hibernate.connection.password",
                required(properties, "spring.datasource.password"));
        hibernateSettings.setProperty("hibernate.dialect",
                required(properties, "spring.jpa.database-platform"));
        hibernateSettings.setProperty("hibernate.hbm2ddl.auto",
                required(properties, "spring.jpa.hibernate.ddl-auto"));
        hibernateSettings.setProperty("hibernate.show_sql",
                required(properties, "spring.jpa.show-sql"));
        hibernateSettings.setProperty("hibernate.format_sql",
                required(properties, "spring.jpa.properties.hibernate.format_sql"));

        StandardServiceRegistry registry = new StandardServiceRegistryBuilder()
                .applySettings(hibernateSettings)
                .build();
        try {
            return new MetadataSources(registry)
                    .addAnnotatedClass(CompactDisc.class)
                    .buildMetadata()
                    .buildSessionFactory();
        } catch (RuntimeException exception) {
            StandardServiceRegistryBuilder.destroy(registry);
            throw exception;
        }
    }

    private static Properties loadProperties() {
        Properties properties = new Properties();
        try (InputStream input = Config.class.getResourceAsStream("/application.properties")) {
            if (input == null) {
                throw new IllegalStateException("application.properties was not found on the classpath");
            }
            properties.load(input);
        } catch (IOException exception) {
            throw new IllegalStateException("Could not load application.properties", exception);
        }
        return properties;
    }

    private static String required(Properties properties, String key) {
        String value = properties.getProperty(key);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException("Missing required property: " + key);
        }
        return value;
    }
}
