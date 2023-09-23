#!/usr/bin/env ruby

require "timeout"

def is_prime(n)
  if n == 2
    return true
  end
  if n < 2
    return false
  end
  for i in (2..Math.sqrt(n).to_i)
    if n.modulo(i) == 0
      return false
    end
  end
  return true
end

def Euler_10
  answer = 0
  for i in (2..2000000)
    if is_prime(i)
      answer = answer + i
    end
  end
  puts "Answer #{answer}"
end


if __FILE__ == $0
  start = Time.now
  Euler_10()
  finish = Time.now - start
  puts "Time: #{finish}"
end
