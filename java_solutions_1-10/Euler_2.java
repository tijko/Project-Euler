/*
/   Project Euler problem #2 Even Fibonacci numbers
/
/   Find the sum of the even fibonacci terms <= 4 million
/
*/

public class
Euler_2
{
    public static void
    main (String[] args)
    {
        int sum_of_fibonacci = 0;
        int last_term = 0;
        int last_current_term = 0;
        int current_term = 1;
        while (current_term <= 4000000) {
            if (current_term % 2 == 0) {
                sum_of_fibonacci += current_term;
            }
            last_current_term = current_term;
            current_term = current_term + last_term;
            last_term = last_current_term;
        }

        System.out.printf("Answer: %d\n", sum_of_fibonacci);
    }
}
            
