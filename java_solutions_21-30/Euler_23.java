/*
/   Project Euler problem #23 Non-abundant sums
/
/   Find the sum of all positive integers which cannot be written as the sum
/   of two abundant numbers.
/
*/

public class Euler_23
{
    public static int totalFactors(int n)
    {
        int factorSum = 0;

        for (int i = 1; i < (n / 2) + 1; i++) {
            if (n % i == 0)
                factorSum += i;
        }

        return factorSum;
    }

    public static void main(String[] args)
    {
        int abundantLimit = 28124;
        int abundantNumbers = 0;
        int[] abundantArray = new int[abundantLimit];

        long nonAbundantable = 0;

        for (int i = 1; i < abundantLimit; i++) {
            int factorSum = totalFactors(i);
            if (factorSum > i)
                abundantArray[abundantNumbers++] = i;
        }

        int[] abundantSums = new int[abundantNumbers * abundantNumbers];

        for (int i = 0; i < abundantSums.length; i++)
            abundantSums[i] = 0;

        for (int i = 0; i < abundantNumbers; i++) { 
            for (int j = 0; j < abundantNumbers; j++) {
                abundantSums[abundantArray[i] + abundantArray[j]] = 
                             abundantArray[i] + abundantArray[j];
            }
        }

        for (int i = 0; i < abundantLimit + 1; i++) {
            if (abundantSums[i] == 0)
                nonAbundantable += i;
        }

        System.out.printf("Answer: %d\n", nonAbundantable);
    }
}
