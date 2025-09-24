class App {
    public static void main(String[] args) {

        // Create an object of SalesTaxCalculator
        SalesTaxCalculator taxCalculator = new SalesTaxCalculator();

        // cacluateTax is implemented in the SalesTaxCalculator class
        double amount = 100.0;
        double tax = taxCalculator.calculateTax(amount);
        System.out.println("Sales Tax on $" + amount + " is $" + tax);

        // Create an object of Register to perform the computeTotal operation
        Register register = new Register();
        double total = register.computeTotal(amount);
        System.out.println("Total amount including tax is $" + total);
    }
}