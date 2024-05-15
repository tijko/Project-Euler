/*
/   Project Euler #17 Number letter counts
/
/   If all the numbers from 1 to 1000 (one thousand) inclusive were written out
/   in words, how many letters would be used?
/
*/

public class Euler_17
{
    public static void main(String[] args)
    {
        long start = System.nanoTime();
        String[][] numWords = {{"", "one", "two", "three", "four",
                                "five", "six", "seven", "eight", "nine"},
                               {"ten", "eleven", "twelve", "thirteen",
                                "fourteen", "fifteen", "sixteen",
                                "seventeen", "eighteen", "nineteen"},
                               {"twenty", "thirty", "forty", "fifty",
                                "sixty", "seventy", "eighty", "ninety"},
                               {"hundred", "hundredand"},
                               {"thousand"}};

        int letterCount = 0;
        int curNumber = 0;

        for (int number = 1; number <= 1000; number++) {

            curNumber = number;

            if (curNumber / 1000 > 0) {
                letterCount += (numWords[0][curNumber / 1000].length() +
                                numWords[4][0].length());
            }

            curNumber %= 1000;

            if (curNumber / 100 > 0 && curNumber % 100 == 0) {
                letterCount += (numWords[0][curNumber / 100].length() +
                                numWords[3][0].length());
                continue;
            }

            if (curNumber / 100 > 0) {
                letterCount += (numWords[0][curNumber / 100].length() +
                                numWords[3][1].length());
            }

            curNumber %= 100;

            if (curNumber / 10 == 1) {
                letterCount += numWords[1][curNumber % 10].length();
                continue;
            }

            if (curNumber / 10 > 0) {
                letterCount += numWords[2][(curNumber / 10) - 2].length();
            }

            curNumber %= 10;

            letterCount += numWords[0][curNumber % 10].length();
        }

        long stop = System.nanoTime();
        System.out.println("Answer: " + letterCount);
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
}
