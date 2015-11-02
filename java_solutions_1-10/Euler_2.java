/*
/   Project Euler problem #2 Even Fibonacci numbers
/
/   Find the sum of the even fibonacci terms <= 4 million
/
*/

public class Euler_2
{
    public static void main (String[] args)
    {
        int sum_of_fibonacci = 0;

        int prev_term = 0;
        int tmp = 0;
        int current_term = 1;

        while (current_term <= 4000000) {

            if (current_term % 2 == 0) 
                sum_of_fibonacci += current_term;

            tmp = current_term;
            current_term = current_term + prev_term;
            prev_term = tmp;
        }

        System.out.println("Answer: " + sum_of_fibonacci);
    }
}
            
