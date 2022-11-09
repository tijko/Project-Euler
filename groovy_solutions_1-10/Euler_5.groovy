#!/usr/bin/env groovy

import groovy.time.TimeCategory
import groovy.time.TimeDuration


class Euler_5 {

    static boolean evenDivisor(int canidate) {

        for (int i=19; i > 2; i--) {
            if (canidate % i != 0) {
                return false
            }
        }

        return true
    }

    static void main(String[] args) {
        Date start = new Date()

        int answer = 20
        while (true) {
            if (evenDivisor(answer)) {
                break
            }

            answer += 20
        }

        println("Answer: ${answer}")
        Date end = new Date()
        TimeDuration time = TimeCategory.minus(end, start)
        println("Time: ${time}")
    }
}
