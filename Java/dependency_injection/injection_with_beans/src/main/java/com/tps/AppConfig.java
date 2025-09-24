package com.tps;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {

    @Bean
    public TaxCalculator taxCalculator() {
        return new SalesTaxCalculator();
    }

    @Bean
    public Register register(TaxCalculator calc) {
        return new Register(calc);
    }
}