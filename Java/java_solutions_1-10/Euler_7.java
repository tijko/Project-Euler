/*
/   Project Euler problem #7 10001 prime
/
/   What is the 10001 prime number?
/
*/

import java.util.stream.IntStream;
import java.lang.Math;


public class Euler_7
{
    public static boolean isPrime(int n)
    {
        if (n < 2) return false;
        else if (n == 2) return true;
        int limit = (int) Math.sqrt(n);
        return IntStream.range(3, limit + 1)
                        .allMatch(x -> n % x != 0);
    }

    public static void main(String[] args)
    {
        long start = System.nanoTime();
        int i = 3;
        for (int primeCount=1; primeCount < 10001; i+=2)
            if (isPrime(i)) primeCount++;

        System.out.println("Answer: " + (i - 2));
        long stop = System.nanoTime();
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
}
