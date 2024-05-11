/*
/   Project Euler problem #9 Special pythagorean triplet
/
/   There exists exactly one pythagorean triplet for which a + b + c = 1000
/   Find the product of abc.
*/

import static java.lang.Math.sqrt;

public class Euler_9
{
    public static long findTriplet(int a, int b)
    {
        int c = (a * a) + (b * b);
        if (sqrt(c) + a + b == 1000) { 
            long triplet = (int) sqrt(c) * a * b;
            return triplet;
        }
        return 0;
    }

    public static void main(String[] args)
    {
        long start = System.nanoTime();
        long triplet = 0;
        long current = 0;
        for (int a = 1; a < 1000; a++) { 
            for (int b = 1; b < 1000; b++) {
                current = findTriplet(a, b);
                if (current > 0) {
                    triplet = current;
                    break;
                }
            }
            if (triplet != 0) {
                break;
            }
        }

        System.out.println("Answer: " + triplet);
        long stop = System.nanoTime();
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
}   