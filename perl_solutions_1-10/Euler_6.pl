use strict;
use warnings;
use Time::HiRes qw( clock );


sub diff_sum_sq
{
    my ($low, $high) = @_;

    my $sum_sq;
    my $sq_sum;
    foreach my $i ($low..$high) {
        $sum_sq += $i**2;
        $sq_sum += $i;
    }
    $sq_sum **= 2;
    return $sq_sum - $sum_sq;
}

my $start = clock();
my $answer = diff_sum_sq(1, 100);
my $stop = clock();
print "Answer: ", $answer, "\n";
printf "Time: %.5f\n", $stop - $start;
