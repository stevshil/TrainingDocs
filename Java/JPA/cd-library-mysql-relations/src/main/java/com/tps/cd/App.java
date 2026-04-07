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
        CompactDisc cd1 = new CompactDisc("Dark Side of the Moon", "Pink Floyd", 12.99);
        CompactDisc cd2 = new CompactDisc("Thriller", "Michael Jackson", 14.99);
        em.persist(cd1);
        em.persist(cd2);

        // Add tracks for Dark Side of the Moon
        cd1.addTrack(new Track("Speak to Me", 1, cd1));
        cd1.addTrack(new Track("Breathe", 2, cd1));
        cd1.addTrack(new Track("Time", 3, cd1));

        // Add tracks for Thriller
        cd2.addTrack(new Track("Wanna Be Startin' Somethin'", 1, cd2));
        cd2.addTrack(new Track("Thriller", 2, cd2));
        cd2.addTrack(new Track("Beat It", 3, cd2));

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
        TypedQuery<CompactDisc> query2 = em.createQuery("SELECT title FROM CompactDisc", CompactDisc.class);
        List<CompactDisc> results = query2.getResultList();
        System.out.println("RESULTS: "+results.toString());

        TypedQuery<CompactDisc> q =
        em.createQuery("SELECT c FROM CompactDisc c JOIN FETCH c.tracks", CompactDisc.class);

        List<CompactDisc> cds2 = q.getResultList();

        for (CompactDisc cd : cds2) {
            System.out.println(cd.getTitle());
            for (Track t : cd.getTracks()) {
                System.out.println("   " + t.getTrackNumber() + ". " + t.getTitle());
            }
        }

        em.close();
        emf.close();
    }
}
