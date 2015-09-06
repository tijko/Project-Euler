/*
/   Project Euler problem #5 Divide Evenly
/
/   What is the smallest number that can be dividely evenly by all the numbers
/   from 1-20?
/
*/

public class Euler_5
{
    public static void main(String[] args)
    {
        int dividend = 20;
        boolean solution_found = false;
        while (!solution_found) {
            for (int i = 20; i > 1; i--) {
                if (dividend % i != 0) {
                    dividend += 20;
                    break;
                } else if (i == 2) {
                    solution_found = true;
                }
            }
        }

        System.out.printf("Answer: %d\n", dividend);
    }
}
