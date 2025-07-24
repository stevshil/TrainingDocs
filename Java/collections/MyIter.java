import java.util.Set;
import java.util.TreeSet;
import java.util.Iterator;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class MyIter {
    public static void main(String[] argv) {
        String[] names = {"Steve", "Nick", "Jack"};

        // Specifically store only Person objects
        Set<Person> persons = new TreeSet<Person>();
        
        for (String name : names) {
            int randomNum = ThreadLocalRandom.current().nextInt(21, 88 + 1);
            int randomPhone = ThreadLocalRandom.current().nextInt(1234, 9998 + 1);

            Person newperson = new Person(name, randomNum);
            newperson.setPhone("555-" + randomPhone);
            persons.add(newperson);
        }

        // NOTE: You have to create to iterator after you have populated your List.
        Iterator<Person> pIter = persons.iterator();

        while ( pIter.hasNext() ) {
            Person person = pIter.next();
            System.out.println(person.getName() + " is " + person.getAge());
        }

    }
}

class Person implements Comparable<Person> {
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

    public int compareTo(Person b) {
        if ( age > b.age ) {
            return 1;
        } else if ( age < b.age ) {
            return -1;
        } else {
            return 0;
        }
    }
    
}