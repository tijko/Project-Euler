/*
/   Project Euler problem #3 Largest prime factor
/
/   Find the largest prime factor of the number 600851475143
/
*/

import static java.lang.Math.sqrt;


public class
Euler_3
{
    public static void
    main (String[] args)
    {
        long large_number = 600851475143L;
        long largest_prime_factor = 0;

        for (int i = 1; i < sqrt(large_number) + 1; i += 2) {
            if (large_number % i == 0 && is_prime(i) && 
                i > largest_prime_factor) {
                largest_prime_factor = i;
            }
        }

        System.out.printf("Answer: %d\n", largest_prime_factor);
    }

    private static boolean
    is_prime(int n)
    {
        if (n < 2) {
            return false;
        } else if (n == 2) {
            return true;
        }

        for (int i = 3; i < sqrt(n) + 1; i+=2) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }
}
