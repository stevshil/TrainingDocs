package com.myapp.tax;

import java.util.Locale;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.core.env.Environment;

@Configuration
@PropertySource("classpath:application.properties")
public class TaxConfig {

    @Bean
//    TaxClass taxClass(Environment environment) {
//        String type = environment.getProperty("tax.type", "ukvat").toLowerCase(Locale.ROOT);
    TaxClass taxClass(
        @Value("${tax.type}") String type
    ) {
        return switch (type) {
            case "uk", "ukvat" -> new UKVAT();
            case "eu", "eugst" -> new EUGST();
            default -> throw new IllegalArgumentException("Unknown tax type: " + type);
        };
    }
}
