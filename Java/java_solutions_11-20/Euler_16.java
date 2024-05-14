/*
/   Project Euler problem #16 Power digit sum
/
/   What is the sum of the digits in 2 to the power of 1000?
/
*/

import java.math.BigInteger;


public class Euler_16
{
    public static void main(String[] args)
    {
        int exponentLimit = 1000;
        int base = 2;


        BigInteger powerOf = new BigInteger("1");
        BigInteger baseExp = new BigInteger("2");

        for (int i = 1; i <= exponentLimit; i++)
            powerOf = powerOf.multiply(baseExp);

        String baseExpStr = powerOf.toString();

        long expSum = 0;
        for (int i = 0; i < baseExpStr.length(); i++)
            expSum += Integer.parseInt(baseExpStr.substring(i, i + 1));

        System.out.println("Answer: " + expSum);
    }
}
