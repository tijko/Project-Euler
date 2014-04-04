use strict;
use warnings;

sub three_five_factors {

    my ($low, $high);
    ($low, $high) = @_;

    my $total = 0;
    my $i;

    for $i ($low..$high)
    {
        if ($i % 3 == 0 || $i % 5 == 0)
        {
            $total += $i;
        }
    }
    return $total;
}

my $answer = three_five_factors(0, 999);
print "Answer: ", $answer, "\n";
