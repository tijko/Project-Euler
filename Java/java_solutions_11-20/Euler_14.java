/*
/   Project Euler problem #14 Longest Collatz sequence
/
/   Which starting number, under one million, produces the longest chain?
/
*/


public class Euler_14
{
    public static int collatzSequence(long chain)
    {
        int sequenceCount = 0;

        while (chain > 1) {
            if (chain % 2 == 0)
                chain /= 2;
            else
                chain = (chain * 3) + 1;

            sequenceCount++;
        }

        return sequenceCount;
    }

    public static void main(String[] args)
    {
        int longestChain = 0;
        long high = 0;

        for (long curr = 0; curr < 1000000; curr++) {

            int chain = collatzSequence(curr);

            if (chain > longestChain) {
                longestChain = chain;
                high = curr;
            }
        }
            
        System.out.println("Answer: " + high);   
    }
}
