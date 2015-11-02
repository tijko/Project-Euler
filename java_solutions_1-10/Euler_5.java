/*
/   Project Euler problem #5 Divide Evenly
/
/   What is the smallest number that can be dividely evenly by all the numbers
/   from 1-20?
/
*/

public class Euler_5
{
    public static boolean all_divisible(int dividend)
    {
        for (int i = 20; i > 1; i--)
            if (dividend % i != 0) return false;
        return true;
    }

    public static void main(String[] args)
    {
        int dividend = 20;
        while (!all_divisible(dividend)) dividend += 20;
        System.out.println("Answer: " + dividend);
    }
}
