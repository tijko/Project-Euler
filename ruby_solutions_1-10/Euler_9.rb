#!/usr/bin/env ruby

require "timeout"


def Euler_9
  for x in (1..1000)
    for y in (x+1..1000)
      z = (x**2 + y**2)**0.5
      if x + y + z == 1000
        puts "Answer #{x * y * z}"
      end
    end
  end
end

if __FILE__ == $0
  start = Time.now
  Euler_9()
  finish = Time.now - start
  puts "Time: #{finish}"
end
