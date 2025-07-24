import java.util.Set;
import java.util.TreeSet;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import java.util.function.Predicate;
import java.util.Iterator;

public class MyTreeSets {
    public static void main(String[] argv) {
        String[] names = {"Steve", "Nick", "Jack"};

        People myFolks = new People();
        
        for (String name : names) {
            int randomNum = ThreadLocalRandom.current().nextInt(21, 88 + 1);
            int randomPhone = ThreadLocalRandom.current().nextInt(1234, 9998 + 1);

            Person newperson = new Person(name, randomNum);
            newperson.setPhone("555-" + randomPhone);
            myFolks.addPeople(newperson);
        }

        for (Person p : myFolks ) {
            System.out.println(p.getName() + " " + myFolks.getNameBeginningWithN(p));
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

class People implements Iterable<Person> {
    private final Set<Person> persons = new TreeSet<Person>();

    public void addPeople(Person being) {
        persons.add(being);
    }

    public Iterator<Person> iterator() {
        return persons.iterator();
    }

    public boolean getNameBeginningWithN(Person person) {
        Predicate<Person> nameBeginsWithN = p -> p.getName().startsWith("N");

        if ( nameBeginsWithN.test(person) ) {
                return true;
        }
        return false;
    }
}