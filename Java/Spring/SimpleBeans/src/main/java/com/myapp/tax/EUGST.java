package com.myapp.tax;

/** EU GST at the configured 5% rate. */
public class EUGST implements TaxClass {

    @Override
    public String name() {
        return "EUGST";
    }

    @Override
    public double calculate(double amount) {
        return Math.round(amount * 5) / 100.0;
    }
}
