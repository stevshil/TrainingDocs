package com.tps;

public class Register {
    private TaxCalculator taxCalc;

    // Accept the dependency via constructor injection
    // Loose coupling: Register class is not responsible for creating the TaxCalculator instance
    public Register (TaxCalculator taxCalculator) {
        taxCalc = taxCalculator;
    }

    // Method that required the calculateTex() functionality from the injected dependency
    public double computeTotal(double beforeTax) {
        return beforeTax + taxCalc.calculateTax(beforeTax);
    }
}