/*
/   Project Euler problem #6 Sum of squares v. square of sums
/
/   Find the difference between the sum of the squares of the first 100 natural
/   numbers and the square of the sum.
/
*/


public class Euler_6
{
    public static void main(String[] args)
    {
        long sum_of_square = 0;
        long square_of_sum = 0;

        for (int i = 0; i <= 100; i++) {
            square_of_sum += i;
            sum_of_square += i * i;
        }

        long answer = (square_of_sum * square_of_sum) - sum_of_square;

        System.out.println("Answer: " + answer);
    }
} 
