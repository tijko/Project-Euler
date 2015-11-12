/*
/   Project Euler problem #12 Highly divisible triangular number
/
/   What is the value of the first triangle number to have over five hundred
/   divisors?
/
*/

import static java.lang.Math.sqrt;


public class Euler_12
{
    public static void main(String[] args)
    {
        long triangleNum = 0;
        int triangleCount = 1;
        int divisors = 0; 
        while (divisors < 500) {
            divisors = 0; 
            triangleNum += triangleCount;
            triangleCount++;

            for (int i = 1; i < sqrt(triangleNum) + 1; i++) 
                if (triangleNum % i == 0) divisors += 2;
        }


        System.out.println("Answer: " + triangleNum); 
    }
}
