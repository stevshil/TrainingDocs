public class Register {
    private TaxCalculator taxCalc;

    // Constructor that creates an object directly from SalesTaxCalculator class
    // No ability to dynamically change, requires code change to use a different implementation
    public Register() {
        this.taxCalc = new SalesTaxCalculator();
    }

    // Implementation of computeTotal method that requires a class that has calculateTax method
    // calculateTax method is tightly coupled to SalesTaxCalculator class
    public double computeTotal(double beforeTax) {
        return beforeTax + taxCalc.calculateTax(beforeTax);
    }
}