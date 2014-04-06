use strict;
use warnings;
use Math::Complex;
use Time::HiRes qw( clock );


sub pythag_trip
{
    my ($low, $high) = @_;
    for my $a ($low..$high) {
        for my $b ($a + 1..$high) {
            if (($a + $b + sqrt($a**2 + $b**2)) == 1000) {
                return $a * $b * int(sqrt($a**2 + $b**2));
            }
            elsif (($a + $b + sqrt($a**2 + $b**2)) > 1000) {
                last;
            }
        }
    }
}

my $start = clock();
my $answer = pythag_trip(1, 3000);
my $stop = clock();
print "Answer: ", $answer, "\n";
printf "Time: %.5f\n", $stop - $start;
