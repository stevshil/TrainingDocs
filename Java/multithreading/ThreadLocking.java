import java.util.ArrayList;
import java.util.List;

public class ThreadLocking {

    public static void main(String[] argv) {
        List<Thread> staff = new ArrayList<>();
        for (int x = 0; x < 10; x++) {
            MyWorkforce2 person = new MyWorkforce2();
            staff.add(person);
            person.start();
        }
    }
}
