/*
/   Project Euler problem #3 Largest prime factor
/
/   Find the largest prime factor of the number 600851475143
/
*/

import static java.lang.Math.sqrt;


public class Euler_3
{
    static long largeNumber = 600851475143L;

    public static void main (String[] args)
    {
        long largestPrimeFactor = 0;

        for (int i = 1; i < sqrt(largeNumber) + 1; i += 2)
            if (largeNumber % i == 0 && isPrime(i) && 
                i > largestPrimeFactor)  
                largestPrimeFactor = i;

        System.out.println("Answer: " + largestPrimeFactor);
    }

    private static boolean isPrime(int n)
    {
        if (n < 2) return false;
        else if (n == 2) return true;

        for (int i = 3; i < sqrt(n) + 1; i+=2) 
            if (n % i == 0) 
                return false;
        return true;
    }
}
