use strict;
use warnings;
use Time::HiRes qw( clock );


sub collatz
{
    my ($cnt, $high, $nhigh) = (0, 0, 0);
    foreach my $i (map(($_ * 2) + 1, (1..500000))) {
        my $cur = $i;
        while ($i != 1) {
            if ($i % 2 != 0) {
                $i *= 3;
                $i += 1;
                $cnt += 1;
            }
            if ($i % 2 == 0) {
                $i /= 2;
                $cnt += 1;
            }
        }
        if ($cnt > $high) {
            $high = $cnt;
            $nhigh = $cur;
        }
        $cnt = 0;
    }
    return $nhigh;
}

my $start = clock();
my $answer = collatz();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
