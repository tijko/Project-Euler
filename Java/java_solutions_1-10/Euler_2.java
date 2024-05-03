/*
/   Project Euler problem #2 Even Fibonacci numbers
/
/   Find the sum of the even fibonacci terms <= 4 million
/
*/

public class Euler_2
{
    public static void main(String[] args)
    {
        long start = System.nanoTime();
        int sumFibonacci = 0;
        int prevTerm = 0;
        int tmp = 0;
        int currentTerm = 1;

        while (currentTerm <= 4000000) {

            if (currentTerm % 2 == 0) 
                sumFibonacci += currentTerm;

            tmp = currentTerm;
            currentTerm = currentTerm + prevTerm;
            prevTerm = tmp;
        }
        long stop = System.nanoTime();
        System.out.println("Answer: " + sumFibonacci);
        System.out.printf("Time: %.7\n", ((float) stop - start);
    }
}
            
