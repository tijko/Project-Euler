use strict;
use warnings;
use Math::Complex;


sub pythag_trip
{
    my ($low, $high);
    ($low, $high) = @_;
    my ($b, $c);
    for my $a ($low..$high)
    {
        $b = $a + 1;
        while ($b < $high)
        {
            if ($a + $b + sqrt($a**2 + $b**2) == 1000)
            {
                return $a * $b * int(sqrt($a * $b * sqrt($a**2 + $b**2)));
            }
            elsif ($a + $b + sqrt($a**2 + $b**2) > 1000)
            {
                last;
            }
            $b++;
        }
    }
}

my $answer = pythag_trip(1, 2999);
print "Answer: ", $answer, "\n";
