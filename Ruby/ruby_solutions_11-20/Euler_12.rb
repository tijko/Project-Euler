#!/usr/bin/env ruby

require 'timeout'


def get_divisors(n)
  range = (n / 2) + 1
  divisors = 1
  for i in (2..range)
    if n.modulo(i) == 0
      divisors += 1
    end
  end
  divisors
end

def Euler_12
  triangle = (1..10000).sum 
  count = 10000
  divisors = 0
  while divisors < 500
    # only even numbers
    count += 1
    triangle += count 
    if triangle.modulo(2) == 0
      divisors = get_divisors(triangle)
    end
  end 
  puts "Answer: #{triangle}"
end

if __FILE__ == $0
  start = Time.now()
  Euler_12()
  finish = Time.now() - start
  puts "Time: #{finish}"
end
