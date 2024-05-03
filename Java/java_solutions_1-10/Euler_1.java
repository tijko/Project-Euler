/*
/   Project Euler problem #1 Multiples of 3 and 5
/
/   Find the sum of all the multiples of 3 or 5 below 1000
/
*/
import java.util.OptionalInt;
import java.util.stream.IntStream;

public class Euler_1
{
    public static int factors(int limit)
    {
        // Use OptionalInt over IntStream with a map-reduce like
        OptionalInt sum = IntStream.range(1, limit)
                                   .filter(x -> x % 3 == 0 ||
                                                x % 5 == 0)
                                   .reduce(Integer::sum);
        return sum.getAsInt();
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
