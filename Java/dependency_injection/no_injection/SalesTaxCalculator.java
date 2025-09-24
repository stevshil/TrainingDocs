public class SalesTaxCalculator implements TaxCalculator {

    // Implementation of the calculateTax method from the TaxCalculator interface
    private double taxRate = 0.05; // default rate
    public double calculateTax(double amount) {
        return amount * taxRate;
    }
}