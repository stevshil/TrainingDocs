import java.util.ArrayList;
import java.util.List;

class ThreadWait {
    public static void main(String[] argv) {
        List<Thread> staff = new ArrayList<>();
        for (int x = 0; x < 10; x++) {
            MyWorkforce person = new MyWorkforce();
            staff.add(person);
            person.start();
        }

        for (int x = 0; x < 10; x++) {
            try {
                System.out.println( (staff.get(x)).threadId() );
                (staff.get(x)).join();
                System.out.println("Thread " + x + " completed");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        // This version does not check or wait for the threads.
    }
}

