#!/usr/bin/env groovy

import groovy.time.TimeCategory
import groovy.time.TimeDuration


class Euler_4 {

    static void main(String[] args) {
        Date start = new Date()

        def answer = 0
        for (int x=100; x < 1000; x++) {
            for (int y=x+1; y < 1000; y++) {
                Integer product = x * y
                String current = product.toString()
                int length = current.length() - 1
                if (current == current[length..0] && product > answer) {
                    answer = product
                }
            } 
        }

        Date end = new Date()
        println("Answer: ${answer}")
        TimeDuration time = TimeCategory.minus(end, start)
        println("Time: ${time}")
    }
}
