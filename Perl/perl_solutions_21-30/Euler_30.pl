use strict;
use warnings;
use Time::HiRes qw( clock );


sub sum_fifthpow
{
    my $total = 0;
    for my $i (2..1000000) {
        my $sum = 0;
        for my $j (split(//, $i)) {
            $sum += $j**5;
        }
        if ($sum eq $i) {
            $total += $i;
        }
    }
    return $total;
}


my $start = clock();
my $answer = sum_fifthpow();
my $stop = clock();

print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
