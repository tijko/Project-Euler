#!/usr/bin/env ruby

require 'timeout'

def find_fibonacci_sum(n)
  total = 0
  last = 0
  current = 1
  while current < n 
    current, last = current + last, current
    if current.even? 
      total += current
    end
  end
  puts "Answer: #{total}"
end

if __FILE__ == $0
  start = Time.now
  find_fibonacci_sum(4000000)
  finish = Time.now - start
  puts "Time: #{finish}"
end
