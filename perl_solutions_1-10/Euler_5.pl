use strict;
use warnings;

sub range_divisor
{
    my ($low, $high);
    ($low, $high) = @_;

    my $start = $high;
    while (1)
    {
        foreach my $i ($low..$high)
        {
            if ($start % $i != 0)
            {
                $start += $high;
                last;
            }
            elsif ($i == $high)
            {
                return $start;
            }
        }
    }
}

my $answer = range_divisor(1, 20);
print "Answer: ", $answer, "\n";
