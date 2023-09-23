#!/usr/bin/env ruby

require 'timeout'


def Euler_15
  forty_path = twenty_path = 1
  for i in (1..40)
    if i < 21
      twenty_path = twenty_path * i
    end
    forty_path = forty_path * i
  end
  answer = forty_path / (twenty_path * twenty_path) 
  puts "Answer: #{answer}"
end

if __FILE__ == $0
  start = Time.now()
  Euler_15()
  finish = Time.now() - start
  puts "Time: #{finish}"
end
