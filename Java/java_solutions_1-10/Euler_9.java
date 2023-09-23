/*
/   Project Euler problem #9 Special pythagorean triplet
/
/   There exists exactly one pythagorean triplet for which a + b + c = 1000
/   Find the product of abc.
*/

import static java.lang.Math.sqrt;

public class Euler_9
{
    static int triplet = 0;

    public static void checkTriplet(int a, int b)
    {
        int c = (a * a) + (b * b);
        if (sqrt(c) + a + b == 1000) 
            triplet = (int) sqrt(c) * a * b;
    }


    public static void main(String[] args)
    {
        for (int a = 1; a < 1000; a++) 
            for (int b = 1; b < 1000; b++) 
                checkTriplet(a, b);

        System.out.println("Answer: " + triplet);
    }
}   
