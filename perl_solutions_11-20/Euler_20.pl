use strict;
use warnings;
use Time::HiRes qw( clock );


my $start = clock();
my $answer = ;
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop -$start;
