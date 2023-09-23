#!/usr/bin/env ruby

require 'timeout'


def Euler_5
  dividend = 20
  while true do
    for i in (3..19)
      if dividend.modulo(i) != 0 then
        break
      end
    end
    if i == 19 && dividend.modulo(19) == 0 then
      break
    else
      dividend += 20
    end
  end
  puts "Answer: #{dividend}"
end


if __FILE__ == $0
  start = Time.now
  Euler_5()
  finish = Time.now - start
  puts "Time: #{finish}"
end

