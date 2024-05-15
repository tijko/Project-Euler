/*
/   Project Euler problem #12 Highly divisible triangular number
/
/   What is the value of the first triangle number to have over five hundred
/   divisors?
/
*/

import static java.lang.Math.sqrt;
import java.util.stream.IntStream;


public class Euler_12
{
    public static long findTriangleDivisors(long triangleNumber) {
        int divisors = 0;
        int triangleLimit = (int) sqrt(triangleNumber);
        IntStream triangleRange = IntStream.range(1, triangleLimit)
                                           .filter(x -> triangleNumber % x == 0);
        return triangleRange.count() * 2;
    }

    public static long findHighlyDivisibleTriangle(int limit, long count, long triangleNumber) {
        if (findTriangleDivisors(triangleNumber) > limit) {
            return triangleNumber;
        }

        return findHighlyDivisibleTriangle(limit, count + 1, triangleNumber + count);
    }

    public static void main(String[] args)
    {
        long start = System.nanoTime();
        long answer = findHighlyDivisibleTriangle(500, 1, 0);
        long stop = System.nanoTime();
        System.out.println("Answer: " + answer);
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
}
