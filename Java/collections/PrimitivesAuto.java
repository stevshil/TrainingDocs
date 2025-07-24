public class PrimitivesAuto {
    public static void main(String[] argv) {
        
        // Primitive types
        int i = 42;
        String name = "Steve";
        double money = 23.03;

        System.out.println("The number is " + i);
        System.out.println("Lowercase name " + name.toLowerCase());
        System.out.println("money is " + money);

       // Non-primitive types
        Integer i2 = 84;
        Integer i3 = 3;

        // Non-primitives start with a capital letter as they are classes.

        if ( i2.equals(i) )
            System.out.println("i2 and i are the same");
        else
            System.out.println("i2 is an Integer object, i is primitive");

    }
}