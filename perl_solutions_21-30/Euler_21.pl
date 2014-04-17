use strict;
use warnings;
use Time::HiRes qw( clock );


sub amicable_pairs
{
    my $total = 0;
    for my $d1 (1..9999) {
        my $p1 = 0;
        my $p2 = 0;
        for my $d2 (1..($d1 / 2) + 1) {
            if ($d1 % $d2 == 0) {
                $p1 += $d2;
            }
        }
        for my $d2 (1..($p1 / 2) + 1) {
            if ($p1 % $d2 == 0) {
                $p2 += $d2;
            }
        } 
        if ($p2 == $d1 && $d1 != $p1) {
            $total += $d1;
        }
    }
    return $total;
}

my $start = clock();
my $answer = amicable_pairs();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", ($stop - $start);
