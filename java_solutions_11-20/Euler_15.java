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
        BigInteger factor;
        BigInteger twenty_side = new BigInteger("1");
        BigInteger forty_side = new BigInteger("1");
        for (int i = 1; i <= 40; i++) {
            factor = new BigInteger(String.valueOf(i));
            forty_side = forty_side.multiply(factor);
            if (i == 20) {
                twenty_side = forty_side;
            }
        }

        twenty_side = twenty_side.multiply(twenty_side);
        forty_side = forty_side.divide(twenty_side);

        System.out.printf("Answer: %s\n", forty_side.toString());
    }
}
