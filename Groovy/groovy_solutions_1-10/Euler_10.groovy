#!/usr/bin/env groovy

import groovy.time.TimeDuration
import groovy.time.TimeCategory


class Euler_10 {

    public static boolean is_prime(int n) {
        if (n == 2) {
            return true
        } else if (n < 2) {
            return false
        }

        def limit = (int) Math.sqrt(n) + 1
        for (int i=2; i < limit; i++) {
            if (n % i == 0) {
                return false
            }
        }

        return true
    }


    static void main(String[] args) {
        Date start = new Date()
        long answer = 0
        for (int i=0; i < 2000000; i++) {
            if (is_prime(i)) {
                answer += i
            }
        }
        Date end = new Date()
        println("Answer: ${answer}")
        TimeDuration time = TimeCategory.minus(end, start)
        println("Time: ${time}")
    }
}
