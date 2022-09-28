#!/usr/bin/env ruby

require 'timeout'


def Euler_4
  is_palindrome = ->(int) { return int.to_s.reverse == int.to_s }
  high = 0
  for pair in (100..1000).to_a.repeated_combination(2) do
    current_product = pair.reduce(:*)
    if current_product > high and is_palindrome.call(current_product) 
      high = current_product
    end
  end
  puts "Answer: #{high}"
end

if __FILE__ == $0
  start = Time.now
  Euler_4()
  finish = Time.now - start
  puts "Time: #{finish}"
end
