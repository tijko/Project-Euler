use strict;
use warnings;
use Math::Complex;
use Time::HiRes qw( clock );


sub pythag_trip
{
    my ($low, $high) = @_;
    my ($b, $c);
    foreach my $a ($low..$high) {
        $b = $a + 1;
        for (my $b1 = $b; $b1 < $high; $b1++) {
            if (($a + $b1 + sqrt($a**2 + $b1**2)) == 1000) {
                return $a * $b1 * int(sqrt($a**2 + $b1**2));
            }
            elsif (($a + $b1 + sqrt($a**2 + $b1**2)) > 1000) {
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
