package com.tps;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;
import org.springframework.context.annotation.PropertySource;


@Configuration
@PropertySource("classpath:application.properties")
public class AppConfig {    
    @Bean
    @Profile("sales")
    public TaxCalculator salesTaxCalculator() {
        return new SalesTaxCalculator();
    }

    @Bean
    @Profile("income")
    public TaxCalculator incomeTaxCalculator() {
        return new IncomeTaxCalculator();
    }

    @Bean
    public Register register(TaxCalculator calc) {
        return new Register(calc);
    }
}