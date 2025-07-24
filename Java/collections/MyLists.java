import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class MyLists {
    public static void main(String[] argv) {
        String[] names = {"Steve", "Nick", "Jack"};

        // Specifically store only Person objects
        List<Person> persons = new ArrayList<Person>();
        
        for (String name : names) {
            int randomNum = ThreadLocalRandom.current().nextInt(21, 88 + 1);
            int randomPhone = ThreadLocalRandom.current().nextInt(1234, 9998 + 1);

            Person newperson = new Person(name, randomNum);
            newperson.setPhone("555-" + randomPhone);
            persons.add(newperson);
        }

        for (Person person : persons) {
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