#!/usr/bin/env groovy

import groovy.time.TimeCategory
import groovy.time.TimeDuration


class Euler_1 {

    static void main(String[] args) {

        Date start = new Date()
        int answer = 0;
        int limit = 1000;
        for (int i=0; i < limit; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                answer += i
            }
        }

        Date end = new Date()
        println("Answer: " + answer)
        TimeDuration time = TimeCategory.minus(end, start)
        println("Time: " + time)
    }
}
