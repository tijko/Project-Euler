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
        long sumOfSq = 0;
        long sqOfSum = 0;

        for (int i = 0; i <= 100; i++) {
            sqOfSum += i;
            sumOfSq += i * i;
        }

        long answer = (sqOfSum * sqOfSum) - sumOfSq;

        System.out.println("Answer: " + answer);
    }
} 
