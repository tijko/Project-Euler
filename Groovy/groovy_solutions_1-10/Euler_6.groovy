#!/usr/bin/env groovy

import groovy.time.TimeCategory
import groovy.time.TimeDuration


class Euler_6 {

    static void main(String[] args) {
        Date start = new Date()

        long sq_sum = 0
        def sum_sq = 0

        for (int i=1; i < 101; i++) {
            sq_sum += i
            sum_sq += (i * i)
        }

        sq_sum = Math.pow(sq_sum, 2)
        def answer = sq_sum - sum_sq
        println("Answer: ${answer}")
        Date end = new Date()
        TimeDuration time = TimeCategory.minus(end, start)
        println("Time: ${time}")
    }
}
