/*
/   Project Euler problem #5 Divide Evenly
/
/   What is the smallest number that can be dividely evenly by all the numbers
/   from 1-20?
/
*/

import java.util.stream.IntStream;


public class Euler_5
{
    public static boolean allDivisible(int dividend)
    {
        return IntStream.range(1, 20)
                        .allMatch(x -> dividend % x == 0);
    }

    public static void main(String[] args)
    {
        long start = System.nanoTime();
        int dividend = 20;
        while (!allDivisible(dividend)) dividend += 20;
        System.out.println("Answer: " + dividend);
        long stop = System.nanoTime();
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
}
