/*
/   Project Euler problem #4 Largest palindrome product
/
/   Find the largest palindrome made from the product of two 3-digit numbers.
/
*/

public class Euler_4
{
    static int largest_palindrome = 0;

    public static void largest_palindrome(int m1, int m2)
    {
        Integer three_digit_product = m1 * m2;
        if (three_digit_product < largest_palindrome) return;

        String product_str = three_digit_product.toString();

        int product_str_len = product_str.length();
        int j = product_str_len - 1;

        for (int i = 0; i < product_str_len; i++) {
            if (product_str.charAt(i) != product_str.charAt(j)) 
                return;
            j--;
        }

        largest_palindrome = three_digit_product;
    }

    public static void main(String[] args)
    {
        Integer three_digit_product;
        String product_str;

        for (int i = 100; i < 1000; i++) 
            for (int j = 100; j < 1000; j++) 
                largest_palindrome(i, j);

        System.out.println("Answer: " + largest_palindrome);
    }
}
