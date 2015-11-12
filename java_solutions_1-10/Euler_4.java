/*
/   Project Euler problem #4 Largest palindrome product
/
/   Find the largest palindrome made from the product of two 3-digit numbers.
/
*/

public class Euler_4
{
    static int largestPalindrome = 0;

    public static void findLargestPalindrome(int m1, int m2)
    {
        Integer threeDigitProduct = m1 * m2;
        if (threeDigitProduct < largestPalindrome) return;

        String productStr = threeDigitProduct.toString();

        int productStrLen = productStr.length();
        int j = productStrLen - 1;

        for (int i = 0; i < productStrLen; i++) {
            if (productStr.charAt(i) != productStr.charAt(j)) 
                return;
            j--;
        }

        largestPalindrome = threeDigitProduct;
    }

    public static void main(String[] args)
    {
        Integer threeDigitProduct;
        String productStr;

        for (int i = 100; i < 1000; i++) 
            for (int j = 100; j < 1000; j++) 
                findLargestPalindrome(i, j);

        System.out.println("Answer: " + largestPalindrome);
    }
}
