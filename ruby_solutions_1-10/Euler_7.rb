#!/usr/bin/env ruby


require 'timeout'


def is_prime(n)
  if n < 2 then return false end
  if n == 2 then return true end
  for i in (3..Math.sqrt(n).to_i + 1) 
    if n.modulo(i) == 0 then return false end
  end
  return true
end

def Euler_7
  prime = 3
  count = 2 
  until count == 10001
    prime = prime + 2 
    if is_prime(prime) 
      count += 1 
    end
  end
  puts "Answer: #{prime}"
end


if __FILE__ == $0
  start = Time.now
  Euler_7()
  finish = Time.now - start
  puts "Time: #{finish}"
end
