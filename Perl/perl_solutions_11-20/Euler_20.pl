use strict;
use warnings;
use Time::HiRes qw( clock );
use Math::BigInt;


sub hundredfac_sum
{
    my $total = 0;
    my $hundredstr = "100";
    my $hundred = Math::BigInt->new($hundredstr);
    $hundred->bfac();
    foreach my $i (split(//, "$hundred")) {
        $total += $i;
    }
    return $total;
}

my $start = clock();
my $answer = hundredfac_sum();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop -$start;
