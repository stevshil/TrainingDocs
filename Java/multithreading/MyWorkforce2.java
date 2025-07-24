class MyWorkforce2 extends Thread {
    private static int threadCounter = 0;

    public void run() {
        // This is the function name that Thread looks for
        // Think of it like main() for your main program.
        if ( addOne() )
            System.out.println("Staff ID: " + threadId() + " has ThreadCounter " + threadCounter);
    }

    public static synchronized boolean addOne() {
        int oldThreadCounter = threadCounter;
        threadCounter++;
        if ( threadCounter > oldThreadCounter )
            return true;
        else
            return false;
    }
}