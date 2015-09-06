/*
/   Project Euler problem #6 Sum of squares v. square of sums
/
/   Find the difference between the sum of the squares of the first 100 natural
/   numbers and the square of the sum.
/
*/

import static java.lang.Math.pow;


public class Euler_6
{
    public static void main(String[] args)
    {
        long sum_of_square = 0;
        long square_of_sum = 0;

        for (int i = 0; i <= 100; i++) {
            square_of_sum += i;
            sum_of_square += pow(i, 2);
        }

        double float_answer = pow(square_of_sum, 2) - sum_of_square;
        int answer = (int) float_answer;
        System.out.printf("Answer: %d\n", answer);
    }
} 
