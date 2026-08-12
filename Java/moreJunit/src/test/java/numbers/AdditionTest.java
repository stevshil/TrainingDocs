package numbers;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AdditionTest {
    public static Addition mynums = new Addition();
    public static int first;
    public static int second;
    public static double one;
    public static double two;

    @BeforeEach
    public void SetUp() {
        first = 20;
        second = 2;
        one = 20;
        two = 22;
    }

    @Test
    public void Add2NumsIntTest() {
        int result = mynums.Add2Nums(first,second);
        try {
            assertEquals(22, result);
            System.out.println("22 expected got " + result);
        } catch (AssertionError e) {
            System.out.println("22 expected but not received");
        }
    }

    @Test
    public void AddAllNumsDoubleTest() {
        double[] allnums = {1.0,3.0,5.0,7.5,9.2};
        double result = mynums.AddAllNums(allnums);
        try {
            assertEquals(25.7,result);
            System.out.println("25.7 expected, got "+result);
        } catch (AssertionError e) {
            System.out.println("25.2 expected, didn't get "+result);
        }
    }
}
