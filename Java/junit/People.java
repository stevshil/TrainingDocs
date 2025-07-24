import java.util.Iterator;
import java.util.Set;
import java.util.TreeSet;
import java.util.function.Predicate;

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