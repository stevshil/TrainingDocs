class App {
    public static void main(String[] args) {

        // Register a tax calculator with implementation of calculateTax() interface
        // Loosely coupled code as we can change the implementation of TaxCalculator in the main code
        TaxCalculator calc = new SalesTaxCalculator();
        
        // Inject the dependency of calculateTax() method into Register
        Register register = new Register(calc);

        double amount = 100.0;
        // calculateTax can be called as normal from SalesTaxCalculator
        double tax = calc.calculateTax(amount);
        System.out.println("Sales Tax on $" + amount + " is $" + tax);

        // To use computeTotal() method from Register it needs to know about calculateTax() which is injected
        double total = register.computeTotal(amount);
        System.out.println("Total amount including tax is $" + total);
    }
}