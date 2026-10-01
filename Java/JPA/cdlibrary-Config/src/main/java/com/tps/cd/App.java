package com.tps.cd;

import jakarta.persistence.*;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {
        EntityManagerFactory emf = Config.createEntityManagerFactory();
        EntityManager em = emf.createEntityManager();

        // Insert sample data
        em.getTransaction().begin();
        em.persist(new CompactDisc("Dark Side of the Moon", "Pink Floyd", 12.99));
        CompactDisc product = new CompactDisc("Thriller", "Michael Jackson", 14.99);
        em.persist(product);
        em.getTransaction().commit();

        System.out.println("Sample data inserted.");

        // Query all the data in the table CompactDisc
        TypedQuery<CompactDisc> query = em.createQuery("from CompactDisc", CompactDisc.class);
        List<CompactDisc> cds = query.getResultList();
        System.out.println("");
        System.out.println("CDs in the database:");
        for (CompactDisc disc : cds) {
            System.out.println("\tThe CD is " + disc.getTitle());
        }

        // Adhoc Query
        TypedQuery<String> query2 = em.createQuery("SELECT cd.title FROM CompactDisc cd",
                String.class);
        List<String> results = query2.getResultList();
        System.out.println("RESULTS: " + results);

        em.close();
        emf.close();
    }
}
