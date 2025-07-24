import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class MyListsGeneric {
    public static void main(String[] argv) {
        String[] names = {"Steve", "Nick", "Jack"};

        // Specifically store only Person objects
        List<Person> persons = new ArrayList<>();
        
        for (String name : names) {
            int randomNum = ThreadLocalRandom.current().nextInt(21, 88 + 1);
            int randomPhone = ThreadLocalRandom.current().nextInt(1234, 9998 + 1);

            if ( name.equals("Steve")) {
                Alien newperson = new Alien(name, randomNum);
                newperson.setSpecies("Grey");
                newperson.setPhone("555-" + randomPhone);
                persons.add(newperson);
            }
            else {
                Person newperson = new Person(name, randomNum);
                newperson.setPhone("555-" + randomPhone);
                persons.add(newperson);
            }
        }

        for (Person person : persons) {
            if ( person instanceof Alien) {
                Alien alien = (Alien) person;
                System.out.println(alien.getName() + " is " + alien.getAge() + " and is a " + alien.getSpecies());
            }
            else
                System.out.println(person.getName() + " is " + person.getAge());
        }

    }
}

class Person {
    private String name;
    private int age;
    private String phone;

    public Person() {
        // Default constructor
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    
}

class Alien extends Person {
    private String species;

    public Alien(String name, int age) {
        super(name,age);
    }

    public void setSpecies(String species) {
        this.species = species;
    }

    public String getSpecies() {
        return this.species;
    }
}