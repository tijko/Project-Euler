/*
/   Project Euler problem #24 Lexicographic permutations
/
/   What is the millionth lexicographic permutation of the digits 
/   0, 1, 2, 3, 4, 5, 6, 7, 8, and 9?
/
*/

public class Euler_24
{
    public static String permutationSort(char[] permutationArray, int idx)
    {
        for (int i = idx; i < permutationArray.length; i++) {

            char cur = permutationArray[i];
            int j = i - 1;

            while (j >= idx && cur < permutationArray[j]) 
                permutationArray[j + 1] = permutationArray[j--];

            permutationArray[j + 1] = cur;
        }

        return new String(permutationArray);
    }

    public static String permute(String permutationString)
    {
        char[] permutationArray = permutationString.toCharArray();

        int idx1, idx2;

        for (idx1 = permutationArray.length - 1; idx1 > 0; idx1--) {
            if (permutationArray[idx1] > permutationArray[idx1 - 1]) {
                idx1--;
                break;
            }
        }

        for (idx2 = permutationArray.length - 1; idx2 > idx1; idx2--) {
            if (permutationArray[idx1] < permutationArray[idx2]) {
                char tmp = permutationArray[idx1];
                permutationArray[idx1] = permutationArray[idx2];
                permutationArray[idx2] = tmp;
                return permutationSort(permutationArray, idx1 + 1);
            }
        }

        char tmp = permutationArray[idx1];
        permutationArray[idx1] = permutationArray[idx2];
        permutationArray[idx2] = tmp;
        return permutationSort(permutationArray, idx1 + 1);
    }

    public static void main(String[] args)
    {
        String permutationString = "0123456789";
        for (int i = 1; i < 1000000; i++)
            permutationString = permute(permutationString);

        System.out.println("Answer: " + permutationString);
    }
}
