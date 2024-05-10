/*
/   Project Euler problem #6 Sum of squares v. square of sums
/
/   Find the difference between the sum of the squares of the first 100 natural
/   numbers and the square of the sum.
/
*/

import java.util.stream.IntStream;


public class Euler_6
{
    public static void main(String[] args)
    {
        long start = System.nanoTime();
        long sumOfSq = IntStream.range(1, 100)
                                .map(x -> x * x)
                                .sum();
        long sqOfSum = IntStream.range(1, 100)
                                .sum();
        long answer = (sqOfSum * sqOfSum) - sumOfSq;
        long stop = System.nanoTime();
        System.out.println("Answer: " + answer);
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
} 
