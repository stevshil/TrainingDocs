package com.tps.cd;

import jakarta.persistence.*;
import org.h2.tools.Server;

public class App {
    public static void main(String[] args) throws Exception {
        // Start H2 Web Console
        Server webConsole = Server.createWebServer(
                "-web", 
                "-webAllowOthers", 
                "-webPort", "8082"
        ).start();

        System.out.println("H2 Console started at: http://localhost:8082");
        System.out.println("JDBC URL: jdbc:h2:mem:cdDB");
        System.out.println("User: sa");
        System.out.println("Password: (empty)");

        // Start JPA
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("cdPU");
        EntityManager em = emf.createEntityManager();

        // Insert sample data
        em.getTransaction().begin();
        em.persist(new CompactDisc("Dark Side of the Moon", "Pink Floyd", 12.99));
        em.persist(new CompactDisc("Thriller", "Michael Jackson", 14.99));
        em.getTransaction().commit();

        System.out.println("Sample data inserted.");

        // Keep application alive
        System.out.println("Application running. Press Ctrl+C to exit.");
        Thread.currentThread().join(); // Keeps JVM alive

        em.close();
        emf.close();
    }
}
