package com.tps;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;
import org.springframework.context.annotation.Configuration;

@Component
@Configuration
public class Register {
    @Value("${MYNAME}")
    private String thisName;


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

    public String getName() {
        return thisName;
    }

    public void setTaxRate(double amount) {
        taxCalc.setTaxRate(amount);
    }

}