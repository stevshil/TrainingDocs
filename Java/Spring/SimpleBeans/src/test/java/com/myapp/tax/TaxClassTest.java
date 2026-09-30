package com.myapp.tax;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.util.Map;
import org.junit.jupiter.api.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.beans.factory.BeanCreationException;
import org.springframework.core.env.MapPropertySource;

class TaxClassTest {

    @Test
    void calculatesTaxInEachImplementation() {
        assertEquals(200.00, new UKVAT().calculate(1000));
        assertEquals(50.00, new EUGST().calculate(1000));
    }

    @Test
    void defaultsToUKVAT() {
        try (var context = TaxApplication.createContext(new String[0])) {
            assertEquals("UKVAT", context.getBean(TaxClass.class).name());
        }
    }

    @Test
    void commandLineArgumentSelectsTaxClass() {
        try (var context = TaxApplication.createContext(new String[] {"1000", "EUGST"})) {
            assertEquals("EUGST", context.getBean(TaxClass.class).name());
        }
    }

    @Test
    void taxTypePropertySelectsTaxClass() {
        try (var context = new AnnotationConfigApplicationContext()) {
            context.getEnvironment().getPropertySources().addFirst(
                    new MapPropertySource("test", Map.of("tax.type", "eu")));
            context.register(TaxConfig.class);
            context.refresh();
            assertEquals("EUGST", context.getBean(TaxClass.class).name());
        }
    }

    @Test
    void rejectsUnknownTaxType() {
        try (var context = new AnnotationConfigApplicationContext()) {
            context.getEnvironment().getPropertySources().addFirst(
                    new MapPropertySource("test", Map.of("tax.type", "nope")));
            context.register(TaxConfig.class);
            assertThrows(BeanCreationException.class, context::refresh);
        }
    }
}
