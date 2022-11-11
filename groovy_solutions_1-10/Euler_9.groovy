#!/usr/bin/env groovy

import groovy.time.TimeCategory
import groovy.time.TimeDuration


class Euler_9 {
    static void main(String[] args) {
        Date start = new Date()
        for (long x=1; x < 1000; x++) {
            for (long y=x+1; y < 1000; y++) {
                def side = Math.pow(x, 2) + Math.pow(y, 2)
                def z = Math.sqrt(side)
                def triangle = x + y + z
                if (triangle == 1000) {
                    long answer = x * y * z
                    Date end = new Date()
                    TimeDuration time = TimeCategory.minus(end, start)
                    println("Answer: ${answer}") 
                    println("Time: ${time}")
                    System.exit(0)
                }
            }
        }
    }
}
