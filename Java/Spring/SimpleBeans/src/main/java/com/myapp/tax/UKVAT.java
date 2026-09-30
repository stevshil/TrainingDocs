package com.myapp.tax;

/** UK standard VAT at 20%. */
public class UKVAT implements TaxClass {

    @Override
    public String name() {
        return "UKVAT";
    }

    @Override
    public double calculate(double amount) {
        return Math.round(amount * 20) / 100.0;
    }
}
