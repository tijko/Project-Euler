/*
/   Project Euler problem #4 Largest palindrome product
/
/   Find the largest palindrome made from the product of two 3-digit numbers.
/
*/

class Euler_4
{
    public static boolean is_palindrome(String product_str)
    {
        int product_str_len = product_str.length();
        int j = product_str_len - 1;
        for (int i = 0; i < product_str_len; i++) {
            if (product_str.charAt(i) != product_str.charAt(j)) {
                return false;
            }
            j--;
        }

        return true;
    }

    public static void main(String[] args)
    {
        int largest_palindrome = 0;
        Integer three_digit_product;
        String product_str;
        for (int i = 100; i < 1000; i++) {
            for (int j = 100; j < 1000; j++) {
                if (i * j > largest_palindrome) {
                    three_digit_product = new Integer(i * j);
                    product_str = three_digit_product.toString();
                    if (is_palindrome(product_str)) {
                        largest_palindrome = three_digit_product;
                    }
                }
            }
        }

        System.out.printf("Answer: %d\n", largest_palindrome);
    }
}
