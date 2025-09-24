package com.tps;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class App {
    public static void main(String[] args) {
        ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);

        Register register = context.getBean(Register.class);

        double total = register.computeTotal(18.45);

        System.out.println("Total with tax: " + total);
    }
}