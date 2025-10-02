class Conditional {
    public static void main(String[] args) {

        // Register a tax calculator with implementation of calculateTax() interface
        // Loosely coupled code as we can change the implementation of TaxCalculator in the main code
        // Different tax calculator can be used here
        TaxCalculator calc;

        if ( args.length > 0 ) {
            calc = new SalesTaxCalculator();
        } else {
            calc = new IncomeTaxCalculator();
        }
        
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