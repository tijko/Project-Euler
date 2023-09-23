use strict;
use warnings;
use Time::HiRes qw( clock );
use Math::BigInt;


sub sum_exp
{
    my $base = "2";
    my $total = 0;
    my $x = Math::BigInt->new($base);
    $x->bpow(1000);
    foreach my $i (split(//, "$x")) {
        $total += $i;
    }
    return $total;
}


my $start = clock();
my $answer = sum_exp();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
