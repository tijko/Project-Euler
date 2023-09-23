use strict;
use warnings;
use Time::HiRes qw( clock );


sub abundant_sums
{
    my @abundants;
    my $sum = 0;
    for my $i (12..28123) {
        my $total = 0;
        for my $j (1..($i / 2) + 1) {
            if ($i % $j == 0) {
                $total += $j;
            }
        }
        if ($total > $i) {
            push(@abundants, $i);
        }
    }
    my %abunsums;
    for my $i (@abundants) {
        for my $j (@abundants) {
            my $s = $i + $j;
            $abunsums{$s} = $s;
        }
    }
    my @sums = keys %abunsums;
    @sums = sort {$a <=> $b} @sums;
    SUMS: for my $i (1..28123) {
        for my $j (@sums) {
            if ($i == $j) {
                next SUMS;
            }
            if ($j > $i) {
                last;
            }
        }
        $sum += $i;
    }
    return $sum;
}


my $start = clock();
my $answer = abundant_sums();
my $stop = clock();

print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
