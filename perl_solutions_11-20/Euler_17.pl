use strict;
use warnings;
use Time::HiRes qw( clock );


sub letter_cnt
{
    return length(join('', ('one' x 191, 'two' x 190, 'three' x 190, 'four' x 190,
                            'five' x 190, 'six' x 190, 'seven' x 190, 'eight' x 190,
                            'nine' x 190, 'ten' x 10, 'eleven' x 10, 'twelve' x 10,
                            'thirteen' x 10, 'fourteen' x 10, 'fifteen' x 10, 
                            'sixteen' x 10, 'seventeen' x 10, 'eighteen' x 10, 
                            'nineteen' x 10, 'twenty' x 100, 'thirty' x 100, 
                            'forty' x 100, 'fifty' x 100, 'sixty' x 100, 
                            'seventy' x 100, 'eighty' x 100, 'ninety' x 100, 
                            'hundredand' x 891, 'hundred' x 9, 'thousand' x 1)));
}

my $start = clock();
my $answer = letter_cnt();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
