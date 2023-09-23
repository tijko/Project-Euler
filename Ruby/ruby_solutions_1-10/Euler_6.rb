#!/usr/bin/env ruby

require 'timeout'


def Euler_6
  squares_sum = (1..100).map{|i| i * i}.sum
  sum_square = (1..100).sum**2
  total = sum_square - squares_sum
  puts "Answer: #{total}"
end


if __FILE__ == $0
  start = Time.now
  Euler_6()
  finish = Time.now - start
  puts "Time: #{finish}"
end
