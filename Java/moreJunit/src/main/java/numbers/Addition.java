package numbers;

import java.util.Arrays;

public class Addition {
    public static int Add2Nums(int a, int b) {
        return(a+b);
    }

    public static double Add2Nums(double a, double b) {
        return(a+b);
    }

    public static int AddAllNums(int[] nums) {
        int total=0;
        total = Arrays.stream(nums).reduce(total, (a, b) -> a + b);
        return(total);
    }

    public static double AddAllNums(double[] nums) {
        double total=0.0;
        total = Arrays.stream(nums).reduce(total, (a, b) -> a + b);
        return(total);
    }
}
