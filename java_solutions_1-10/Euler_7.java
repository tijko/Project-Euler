/*
/   Project Euler problem #7 10001 prime
/
/   What is the 10001 prime number?
/
*/

import static java.lang.Math.sqrt;


public class Euler_7
{
    public static boolean is_prime(int n)
    {
        if (n < 2) {
            return false;
        } else if (n == 2) {
            return true;
        }

        for (int i = 3; i < sqrt(n) + 1; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args)
    {
        int prime_count = 1;
        int i = 3;

        while (prime_count != 10001) {
            if (is_prime(i)) {
                prime_count++;
            }

            i += 2;
        }

        System.out.printf("Answer: %d\n", i - 2);
    }
}
