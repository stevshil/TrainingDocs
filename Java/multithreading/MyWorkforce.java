class MyWorkforce extends Thread {
    public void run() {
        // This is the function name that Thread looks for
        // Think of it like main() for your main program.
        System.out.println("Staff " + threadId());
    }
}