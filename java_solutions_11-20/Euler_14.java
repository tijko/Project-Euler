/*
/   Project Euler problem #14 Longest Collatz sequence
/
/   Which starting number, under one million, produces the longest chain?
/
*/


public class Euler_14
{
    public static void main(String[] args)
    {
        int longest_chain = 0;
        int high = 0;

        for (int current_number = 0; current_number < 1000000; current_number++) {

            int chain = 1;
            long chain_number = current_number;

            while (chain_number > 1) {

                if (chain_number % 2 == 0) {
                    chain_number = chain_number / 2;
                } else {
                    chain_number = (chain_number * 3) + 1;
                }

                chain = chain + 1;
            }

            if (chain > longest_chain) {
                longest_chain = chain;
                high = current_number;
            }
        }
            
        System.out.printf("Answer: %d\n", high);   
    }
}
