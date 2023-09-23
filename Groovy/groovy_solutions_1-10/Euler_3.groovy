#!/usr/bin/env groovy

import groovy.time.TimeCategory
import groovy.time.TimeDuration


class Euler_3 {

    public static boolean is_prime(long n) {
        if (n == 2) {
            return true
        } else if (n < 2) {
            return false
        }

        int limit = (int) Math.sqrt(n);
        for (int i=3; i < limit; i++) {
            if (n % i == 0) {
                return false
            }
        }

        return true
    }

    static void main(String[] args) {
        Date start = new Date()
        long limit = 600851475143 
        long answer = (long) Math.sqrt(limit)
        while (true) {
            if (is_prime(answer) && limit % answer == 0) {
                break
            }

            answer -= 1 
        }

        Date end = new Date()
        println("Answer: ${answer}") 
        TimeDuration time = TimeCategory.minus(end, start)
        println("Time: ${time}")
    }
}

