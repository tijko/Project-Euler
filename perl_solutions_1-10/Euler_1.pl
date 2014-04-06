use strict;
use warnings;
use Time::HiRes qw( clock );


sub three_five_factors 
{
    my ($low, $high) = @_;
    my $total = 0;
    for my $i ($low..$high) {
        if ($i % 3 == 0 || $i % 5 == 0) {
            $total += $i;
        }
    }
    return $total;
}

my $start = clock();
my $answer = three_five_factors(0, 999);
my $stop = clock();
print "Answer: ", $answer, "\n";
printf "Time: %.5f\n", $stop - $start;
