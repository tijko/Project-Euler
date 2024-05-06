/*
/   Project Euler problem #3 Largest prime factor
/
/   Find the largest prime factor of the number 600851475143
/
*/

import java.util.stream.IntStream;
import static java.lang.Math.sqrt;
import static java.lang.Math.ceil;


public class Euler_3
{
    static long largeNumber = 600851475143L;

    public static void main (String[] args)
    {
        long start = System.nanoTime();
        long largestPrimeFactor = 0;

        for (int i = 1; i < sqrt(largeNumber) + 1; i += 2)
            if (largeNumber % i == 0 && isPrime(i) && 
                i > largestPrimeFactor)  
                largestPrimeFactor = i;

        long stop = System.nanoTime();
        System.out.println("Answer: " + largestPrimeFactor);
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }

    private static boolean isPrime(int n)
    {
        if (n < 2) return false;
        else if (n == 2) return true;

        int endRange = ((Double) ceil(sqrt(n))).intValue();
        IntStream range = IntStream.range(3, endRange);
        return range.allMatch(x -> n % x != 0);
    }
}
