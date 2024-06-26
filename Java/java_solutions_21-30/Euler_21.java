/*
/   Project Euler problem #21 Amicable numbers
/
/   Evaluate the sum of all the amicable numbers under 10000.
/
*/
import java.util.List;
import java.util.stream.IntStream;
import java.util.function.Supplier;
import java.util.stream.Collectors;


public class Euler_21
{
    public static int amicablePair(int amicableSum)
    {
        return IntStream.range(1, (amicableSum / 2) + 1)
                        .filter(x -> amicableSum % x == 0)
                        .sum();
    }

    public static List<Integer> getRange(int start, int end) {
        List<Integer> range = IntStream.range(start, end)
                                       .boxed()
                                       .collect(Collectors.toList());
        return range;
    }

    public static void main(String[] args)
    {
        long start = System.nanoTime();
        int amicableLimit = 10000;
        int amicablePairSum = 0;
        List<Integer> amicableRange = getRange(4, amicableLimit);
        for (int i:amicableRange) {
            int amicableSum = IntStream.range(1, (i / 2) + 1)
                                       .filter(x -> i % x == 0)
                                       .sum();
            if (amicableSum != i) { 
                int candidate = amicablePair(amicableSum);
                if (candidate == i) {
                    amicablePairSum += i;
                }
            }
        }

        long stop = System.nanoTime();
        System.out.println("Answer: " + amicablePairSum);
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
}
