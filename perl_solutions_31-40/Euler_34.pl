use strict;
use warnings;
use Math::BigInt;
use Time::HiRes qw( clock );


sub fac_sums
{
    my $sums = 0;
    my $limit = Math::BigInt->new("9");
    $limit->bfac();
    FAC: for my $i (3..$limit) {
        my $fac = 0;
        for my $d (split(//, $i)) {
            if ($d eq "9") {
                next FAC;
            }
            my $f = Math::BigInt->new($d);
            $f->bfac();
            $fac += $f;
            if ($fac > $i) {
                next FAC;
            }
        }
        if ($fac eq $i) {
            $sums += $i;
        }
    }
    return $sums;
}


my $start = clock();
my $answer = fac_sums();
my $stop = clock();

print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
