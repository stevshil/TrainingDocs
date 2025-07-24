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