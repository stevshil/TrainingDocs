package com.myapp.tax;

import java.util.Map;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.MapPropertySource;

/**
 * Entry point.
 *
 * Usage: gradlew run --args="1000 EUGST"
 * Or set TAX_TYPE=EUGST in the environment.
 */
@Configuration
public class TaxApplication {

    public static void main(String[] args) {
        try (var context = createContext(args)) {
            TaxClass taxClass = context.getBean(TaxClass.class);

            double amount = args.length > 0 ? Double.parseDouble(args[0]) : 1000;

            System.out.printf("Tax on %.2f (%s) = %.2f%n",
                    amount, taxClass.name(), taxClass.calculate(amount));
        }
    }

    static AnnotationConfigApplicationContext createContext(String[] args) {
        var context = new AnnotationConfigApplicationContext();
        if (args.length > 1) {
            context.getEnvironment().getPropertySources().addFirst(
                    new MapPropertySource("commandLine", Map.of("tax.type", args[1])));
        }
        context.register(TaxApplication.class, TaxConfig.class);
        context.refresh();
        return context;
    }
}
