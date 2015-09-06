/* 
/   Euler Problem #1 Multiples of 3 and 5
/
/   Find the sum of all the multiples of 3 or 5 below 1000
/
*/

public class 
Euler_1
{
    public static void
    main (String[] args)
    {
        int sum_of_multiples = 0;
        for (int i = 0; i < 1000; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                sum_of_multiples += i;
            }
        }

        System.out.printf("Answer: %d\n", sum_of_multiples);
    }
}    
