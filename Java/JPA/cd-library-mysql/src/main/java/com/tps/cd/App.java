package com.tps.cd;

import jakarta.persistence.*;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Check MySQL, using user: root, password: root");

        // Start JPA
        EntityManagerFactory emf = Persistence.createEntityManagerFactory("cdPU");
        EntityManager em = emf.createEntityManager();

        // Insert sample data
        em.getTransaction().begin();
        em.persist(new CompactDisc("Dark Side of the Moon", "Pink Floyd", 12.99));
        CompactDisc product = new CompactDisc("Thriller", "Michael Jackson", 14.99);
        em.persist(product);
        em.getTransaction().commit();

        System.out.println("Sample data inserted.");

        // Query all the data in the table CompactDisc
        Query query = em.createQuery("from CompactDisc");
        java.util.List<CompactDisc> cds = query.getResultList();
        System.out.println("");
        System.out.println("CDs in the database:");
        for (CompactDisc disc : cds) {
            System.out.println("\tThe CD is " + disc.getTitle());
        }

        // Adhoc Query
        TypedQuery<CompactDisc> query2 = em.createQuery("SELECT title FROM CompactDisc",
CompactDisc.class);
        List<CompactDisc> results = query2.getResultList();
        System.out.println("RESULTS: "+results.toString());

        em.close();
        emf.close();
    }
}
