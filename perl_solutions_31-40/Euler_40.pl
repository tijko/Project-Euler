use strict;
use warnings;
use Time::HiRes qw( clock );


sub irrational_sum
{
    my $sum = 1;
    my $irrational = join("", (0..1000000));
    for my $i (0..5) {
        $sum *= substr($irrational, 10**$i, 1);
    }
    return $sum;
}


my $start = clock();
my $answer = irrational_sum();
my $stop = clock();

print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
