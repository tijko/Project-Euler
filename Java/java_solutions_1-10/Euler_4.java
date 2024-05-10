/*
/   Project Euler problem #4 Largest palindrome product
/
/   Find the largest palindrome made from the product of two 3-digit numbers.
/
*/

public class Euler_4
{
    public static boolean isPalindrome(String candidate) {
        return new StringBuilder(candidate).reverse()
                                           .toString()
                                           .equals(candidate);
    }

    public static void main(String[] args)
    {
        long start = System.nanoTime();
        int largestPalindrome = 0;

        for (int i = 100; i < 1000; i++) { 
            for (int j = 100; j < i; j++) {
                int current = i * j;
                if (current > largestPalindrome && 
                    isPalindrome(String.valueOf(current))) { 
                    largestPalindrome = current;
                }
            }
        }
        long stop = System.nanoTime();
        System.out.println("Answer: " + largestPalindrome);
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
}
