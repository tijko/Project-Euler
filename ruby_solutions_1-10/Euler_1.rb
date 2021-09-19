=begin

  Project Euler Ruby Solutions!!

  ok time to begin....Getting used to the basics
  of Ruby for the first ten Euler problems...
  basic builtins, flow-control, conditionals,
  modules...

=end

# Find the sum of all the multiples of 3 & 5 below 1000

#/usr/bin/env ruby

require 'timeout'


def find_multiples(multiple_one, multiple_two)
  my_multiples = []
  for multiple in (1...1000)
    if ((multiple % multiple_one == 0) || 
        (multiple % multiple_two == 0))
      my_multiples << multiple
    end
  end
  return my_multiples
end  

def sum_multiples(limit)
  total = find_multiples(3, 5).reduce(:+)
  puts "Answer: #{total}"
end


if __FILE__ == $0
  start = Time.now
  sum_multiples(1000)
  finish = Time.now - start
  puts "Time:   #{finish}"
end
