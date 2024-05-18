/*
 * Find the largest sequence of repeating numbers n < 1000 of 1/d
 */

import java.util.stream.IntStream;
import java.util.List;
import java.util.stream.Collectors;


public class Euler_26 {

    public static boolean is_prime(int n) {
        if (n == 2) {
            return true;
        } else if (n % 2 == 0 || n < 2) {
            return false;
        }
        return IntStream.range(3, (int) Math.sqrt(n) + 1)
                        .allMatch(x -> n % x != 0);
    }

    public static void main(String[] args) {
        long start = System.nanoTime();
        List<Integer> primes = IntStream.range(1, 1001)
                                        .filter(x -> is_prime(x))
                                        .boxed()
                                        .collect(Collectors.toList());
        int answer = primes.get(primes.size() - 3);
        System.out.println("Answer: " + answer);
        long stop = System.nanoTime();
        System.out.printf("Time: %.4f\n", ((float) stop - start) / 1_000_000_000);
    }
}

