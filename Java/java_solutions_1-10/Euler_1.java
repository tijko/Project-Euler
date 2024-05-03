/* 
/   Project Euler problem #1 Multiples of 3 and 5
/
/   Find the sum of all the multiples of 3 or 5 below 1000
/
*/
import java.util.stream.*;
import java.util.List;

public class Euler_1
{
    public static int factors(int limit)
    {
        int sum = 0;
        // IntStream 'boxed' method to convert from primitive [int] type
        List<Integer> range = IntStream.range(1, limit)
                                       .boxed()
                                       .collect(Collectors.toList());
        for (int i:range) {
            if (i % 5 == 0 || i % 3 == 0)
                sum += i;
        }

        return sum;
    }           

    public static void main(String[] args)
    {
        long start = System.nanoTime();

        int factor_sum = factors(1000);

        long stop = System.nanoTime();
        System.out.println("Answer: " + factor_sum); 
        System.out.printf("Time: %.7f\n", ((float) stop - (float) start) / 10000000);
    }
}    
