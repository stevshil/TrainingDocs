package com.myapp.tax;

/** A tax strategy that calculates tax for an amount. */
public interface TaxClass {

    String name();

    double calculate(double amount);
}
