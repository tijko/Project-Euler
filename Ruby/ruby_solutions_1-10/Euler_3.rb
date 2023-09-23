#!/usr/bin/env ruby

require "timeout"

# Greatest prime factor of 600851475143?


def is_prime(n)
  if n.even?
    return true
  end
  high = Math.sqrt(n).ceil(0) + 1
  for i in (3..high).step(2)
    if n % i == 0
      return false
    end
  end
  true
end

def large_prime
  high = 1
  lim = 600851475143
  n = Math.sqrt(lim).ceil(0) + 1
  for i in (3..n)
    if lim % i == 0 and is_prime(i) 
      high = i
    end
  end
  puts "Answer: #{high}"
end

if __FILE__ == $0
  start = Time.now
  large_prime
  finish = Time.now - start
  puts "Time: #{finish}"
end
