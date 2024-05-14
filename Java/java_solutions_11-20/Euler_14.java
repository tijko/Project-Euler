/*
/   Project Euler problem #14 Longest Collatz sequence
/
/   Which starting number, under one million, produces the longest chain?
/
*/


public class Euler_14
{
    public static long collatzSequence(long chain)
    {
        long sequenceCount = 0;
        while (chain > 1) {
            if (chain % 2 == 0) {
                chain /= 2;
            } else {
                chain = (chain * 3) + 1;
            }
            sequenceCount++;
        }
        return sequenceCount;
    }

    public static long findLongestChain(long limit, 
                                       long candidate, 
                                       long longestChain, 
                                       long longestChainStart) {
        if (candidate > limit) {
            return longestChainStart; 
        }

        long currentChain = collatzSequence(candidate);
        if (currentChain > longestChain) {
            longestChain = currentChain;
            longestChainStart = candidate;
        }

        return findLongestChain(limit, candidate + 1, longestChain, 
                                                      longestChainStart);
    }

    public static void main(String[] args)
    {
        long start = System.nanoTime();
        long answer = findLongestChain(1000000, 0, 0, 0);
        long stop = System.nanoTime();
        System.out.println("Answer: " + answer); 
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);            
    }
}
