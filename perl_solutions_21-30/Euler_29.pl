use strict;
use warnings;
use Math::BigInt;
use Time::HiRes qw( clock );


sub pow_combos
{
    my %power_set;
    for my $i (2..100) {
        my $base = Math::BigInt->new("$i");
        my $cpy = $base->copy();
        for my $j (2..100) {
            $power_set{$base->bpow($j)} = 0;
            $base = $cpy;
            $cpy = $base->copy();
        }        
    }
    return scalar(keys %power_set);
}

my $start = clock();
my $answer = pow_combos();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;

