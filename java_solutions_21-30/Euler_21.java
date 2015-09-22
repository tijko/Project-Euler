/*
/   Project Euler problem #21 Amicable numbers
/
/   Evaluate the sum of all the amicable numbers under 10000.
/
*/

public class Euler_21
{
    public static int amicablePair(int amicableSum)
    {
        int amicablePairSum = 0;

        for (int i = 1; i < (amicableSum / 2) + 1; i++) {
            if (amicableSum % i == 0)
                amicablePairSum += i;
        }

        return amicablePairSum;
    }

    public static void main(String[] args)
    {
        int amicableLimit = 10000;
        int amicablePairSum = 0;

        for (int i = 4; i < amicableLimit; i++) {
            int amicableSum = 0;
            for (int j = 1; j < (i / 2) + 1; j++) {
                if (i % j == 0)
                    amicableSum += j;
            }    
     
            if (amicableSum != i) { 
                int canidate = amicablePair(amicableSum);
                if (canidate == i)
                    amicablePairSum += i;
            }
        }

        System.out.printf("Answer: %d\n", amicablePairSum);
    }
}
