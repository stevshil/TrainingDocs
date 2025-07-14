package com.steve.banking;

public class OffShoreAccounts extends Accounts implements AccountClose {
    private String nation;
    private String taxCode;

    private static double taxFiddle = 1.3;

    public OffShoreAccounts() {
    }

    public OffShoreAccounts(String name, double balance) {
        super(name, balance);
    }

    public OffShoreAccounts(String name, String nation, String taxCode) {
        super(name);
        this.nation = nation;
        this.taxCode = taxCode;
    }

    public OffShoreAccounts(String name, double balance, String nation, String taxCode) {
        super(name, balance);
        this.nation = nation;
        this.taxCode = taxCode;
    }

    public String getNation() {
        return nation;
    }

    public void setNation(String nation) {
        this.nation = nation;
    }

    public String getTaxCode() {
        return taxCode;
    }

    public void setTaxCode(String taxCode) {
        this.taxCode = taxCode;
    }

    @Override
    public void addInterest() {
        super.addInterest();
        System.out.println("This is OffShore addInterest for "+this.getName());
        balance *= taxFiddle;
    }

    @Override
    public double getBalance() {
        System.out.println("Offshore Balance: "+this.balance);
        return this.balance;
    }

    @Override
    public double close() {
        // Remove tax fiddle payment
        this.balance /= taxFiddle;
        setAccountsTotal();
        return this.balance;
    }
}
