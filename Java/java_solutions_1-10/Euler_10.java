/*
/   Project Euler problem #10 Primes below two million.
/
/   Find the sum of all the primes below two million.
/
*/

import static java.lang.Math.sqrt;


public class Euler_10
{
    public static boolean isPrime(int n)
    {
        if (n < 2) return false;
        else if (n == 2) return true;

        for (int i = 2; i < sqrt(n) + 1; i++) 
            if (n % i == 0) return false;

        return true;
    }

    public static void main(String[] args)
    {
        long start = System.nanoTime();
        long primeSum = 0;
        for (int i = 1; i < 2000000; i++) {
            if (!isPrime(i)) continue;
            primeSum += i;
        }

        System.out.println("Answer: " + primeSum);
        long stop = System.nanoTime();
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
}
