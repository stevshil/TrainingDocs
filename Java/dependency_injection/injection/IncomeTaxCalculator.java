public class IncomeTaxCalculator implements TaxCalculator {

    // Method that performs the tax calculation
    private double taxRate = 0.2; // default rate
    public double calculateTax(double amount) {
        return amount * taxRate;
    }
}