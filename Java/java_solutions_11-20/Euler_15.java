/*
/   Project Euler problem #15 Lattice paths
/
/   How many routes are there through a 20 x 20 grid?
/
*/

import java.math.BigInteger;


public class Euler_15
{
    public static void main(String[] args)
    {
        long start = System.nanoTime();
        BigInteger factor;
        BigInteger twentySide = new BigInteger("1");
        BigInteger fortySide = new BigInteger("1");
        for (int i = 1; i <= 40; i++) {
            factor = new BigInteger(String.valueOf(i));
            fortySide = fortySide.multiply(factor);
            if (i == 20)
                twentySide = fortySide;
        }

        twentySide = twentySide.multiply(twentySide);
        fortySide = fortySide.divide(twentySide);
        long stop = System.nanoTime();
        System.out.println("Answer: " + fortySide.toString());
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
}
