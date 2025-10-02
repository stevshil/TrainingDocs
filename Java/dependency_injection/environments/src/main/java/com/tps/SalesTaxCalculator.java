package com.tps;

public class SalesTaxCalculator implements TaxCalculator {

    // Method that performs the tax calculation
    private double taxRate = 0.05; // default rate
    public double calculateTax(double amount) {
        System.out.println("Tax Rate: " + taxRate);
        return amount * taxRate;
    }

    public void setTaxRate(double amount) {
        this.taxRate = amount;
    }
}