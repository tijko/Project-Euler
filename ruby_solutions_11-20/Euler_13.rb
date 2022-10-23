#!/usr/bin/env ruby

require 'timeout'


def Euler_13
  fh = File.open('large-digit.txt')
  answer = fh.readlines().map{|i| i.strip}.map{|i| i.to_i}
  puts "Answer: #{answer.sum.to_s[..9]}"
end

if __FILE__ == $0
  start = Time.now()
  Euler_13()
  finish = Time.now() - start
  puts "Time: #{finish}"
end
