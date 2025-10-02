package com.tps;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.annotation.DirtiesContext;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit.jupiter.SpringJUnitConfig;

import static org.junit.jupiter.api.Assertions.*;

@SpringJUnitConfig(AppConfig.class)
@ActiveProfiles("sales")
public class RegisterSalesTest {

    @Autowired
    private Register register;

    @Test
    @DirtiesContext
    void testAltTaxComputeTotal() {
        double input = 18.45;
        register.setTaxRate(5.00);
        double expected = input + (input * 5.00); // assuming 20% tax
        // double expected = input;
        double actual = register.computeTotal(input);

        assertEquals(expected, actual);
    }

    @Test
    void testComputeTotal() {
        double input = 18.45;
        double expected = input + (input * 0.05); // assuming 20% tax
        // double expected = input;
        double actual = register.computeTotal(input);

        assertEquals(expected, actual);
    }

    @Test
    void testGetName() {
        String name = register.getName();
        assertNotNull(name, "Name should not be null");
        assertFalse(name.isEmpty(), "Name should not be empty");
    }
}
