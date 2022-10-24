#!/usr/bin/env ruby


require 'timeout'


def collatz(n)
  count = 0
  while n != 1
    if n.modulo(2) != 0
      n *= 3
      n += 1
      count += 1
    end 
    if n.modulo(2) == 0
      n = n >> 1
      count += 1
    end
  end
  count
end

def Euler_14
  answer = 0
  high = 0
  for i in (3..1000000).step(2)
    canidate = collatz(i)
    if canidate > high 
      answer = i 
      high = canidate
    end
  end
  puts "Answer: #{answer}"
end

if __FILE__ == $0
  start = Time.now()
  Euler_14()
  finish = Time.now() - start
  puts "Time: #{finish}"
end
