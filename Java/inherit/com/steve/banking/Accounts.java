package com.steve.banking;

import static java.lang.Math.*;

public class Accounts {
    private String name;
    protected double balance; // Variable protected as we use it in child class

//    private static double interestRate=0.2;
//    Alternate method
    private static double interestRate;
    static {
//        interestRate=0.2;
        interestRate = PI * random() *0.1;
    }

    private static int accountsTotal;
    static {
        accountsTotal = 0;
    }

    protected static void setAccountsTotal() {
        accountsTotal--;
    }

    public Accounts() {
        accountsTotal++;
    }

    public Accounts(String name) {
        this();
        this.name = name;
        this.balance = 0;
    }

    public Accounts(String name, double balance) {
        this();
        this.name = name;
        this.balance = balance;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double d) {
        balance = d;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void withdraw(double amount) {
        balance -= amount;
    }

    public void addInterest() {
        System.out.println("This is Account addInterest for "+this.name);
        balance += (balance * interestRate);
    }

    public static double getInterestRate() {
        System.out.println("Account Interest");
        return interestRate;
    }

    public static int getAccountsTotal() {
        return accountsTotal;
    }

    public String toString() {
        return "Account Name: " + name + "  -  Account Balance: " + balance;
    }
}