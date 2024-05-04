/*
/   Project Euler problem #2 Even Fibonacci numbers
/
/   Find the sum of the even fibonacci terms <= 4 million
/
*/
import java.util.stream.IntStream;
import java.util.OptionalInt;

public class Euler_2
{
    public static long fibonacci(long fnum, long idx, int limit, long total) {
        if (fnum >= limit) {
            return total;
        }

        if (fnum % 2 == 0) {
            total += fnum;
        }

        return fibonacci(fnum + idx, fnum, limit, total);
    }

    public static void main(String[] args)
    {
        long start = System.nanoTime();
        long sumFibonacci = fibonacci(3, 2, 4000000, 0);
        long stop = System.nanoTime();
        System.out.println("Answer: " + sumFibonacci);
        System.out.printf("Time: %.7f\n", ((float) stop - start));
    }
}
            
