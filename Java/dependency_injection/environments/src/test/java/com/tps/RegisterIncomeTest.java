package com.tps;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit.jupiter.SpringJUnitConfig;

import static org.junit.jupiter.api.Assertions.*;

@SpringJUnitConfig(AppConfig.class)
@ActiveProfiles("income")
public class RegisterIncomeTest {

    @Autowired
    private Register register;

    @Test
    void testComputeTotal() {
        double input = 18.45;
        double expected = input + (input * 0.2); // assuming 20% tax
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
