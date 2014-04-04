use strict;
use warnings;

sub diff_sum_sq
{
    my ($low, $high);
    ($low, $high) = @_;

    my $sum_sq;
    my $sq_sum;
    foreach my $i ($low..$high)
    {
        $sum_sq += $i**2;
        $sq_sum += $i;
    }
    $sq_sum **= 2;
    return $sq_sum - $sum_sq;
}

my $answer = diff_sum_sq(1, 100);
print "Answer: ", $answer, "\n";
