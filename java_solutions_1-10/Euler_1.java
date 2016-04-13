/* 
/   Project Euler problem #1 Multiples of 3 and 5
/
/   Find the sum of all the multiples of 3 or 5 below 1000
/
*/


public class Euler_1
{
    public static int factors(int limit, int ... factorsOf)
    {
        int sum = 0;
        int numFactors = factorsOf.length;

        for (int j, i = 0; i < limit; i++) {
            for (j = 0; j < numFactors; j++)
                if (i % factorsOf[j] == 0) break;
            sum += j == numFactors ? 0 : i;
        }

        return sum;
    }           

    public static void main(String[] args)
    {
        long start = System.nanoTime();

        int factor_sum = factors(1000, 3, 5);

        long stop = System.nanoTime();
        System.out.println("Answer: " + factor_sum); 
        System.out.printf("Time: %.7f\n", ((float) stop - (float) start) / 10000000);

    }
}    
