#!/usr/bin/env groovy

import groovy.time.TimeCategory
import groovy.time.TimeDuration


class Euler_2 {

    static void main(String[] args) {

        Date start = new Date()
        int answer = 0
        int limit = 4000000

        int cur = 1
        int lst = 1

        while (cur < limit) {
            int tmp = cur
            cur = cur + lst
            lst = tmp

            if (cur % 2 == 0) {
                answer += cur
            }
        }

        Date end = new Date()
        println("Answer: ${answer}")
        TimeDuration time = TimeCategory.minus(end, start)
        println("Time: ${time}")
    }
}
