#!/usr/bin/env ruby

require 'timeout'

def Euler_16
  two_power_to_thousand = 2**1000
  two_power_to_thousand_sum = two_power_to_thousand.to_s.chars.map(&:to_i).sum
  return two_power_to_thousand_sum
end

if __FILE__ == $0
  start = Time.now()
  answer = Euler_16()
  puts "Answer: #{answer}"
  finish = Time.now() - start
  puts "Time: #{finish}"
end
