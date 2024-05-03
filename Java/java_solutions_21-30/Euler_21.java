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
        int amicablePairSum = 0;

        for (int i = 1; i < (amicableSum / 2) + 1; i++) {
            if (amicableSum % i == 0)
                amicablePairSum += i;
        }

        return amicablePairSum;
    }

    public static List<Integer> getRange(int start, int end) {
        List<Integer> range = IntStream.range(start, end)
                                       .boxed()
                                       .collect(Collectors.toList());
        return range;
    }

    public static void main(String[] args)
    {
        int amicableLimit = 10000;
        int amicablePairSum = 0;
        List<Integer> amicableRange = getRange(4, amicableLimit);
        for (int i:amicableRange) {
            int amicableSum = 0;
            for (int j = 1; j < (i / 2) + 1; j++) {
                if (i % j == 0)
                    amicableSum += j;
            }    
     
            if (amicableSum != i) { 
                int candidate = amicablePair(amicableSum);
                if (candidate == i)
                    amicablePairSum += i;
            }
        }

        System.out.println("Answer: " + amicablePairSum);
    }
}
