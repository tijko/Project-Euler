use strict;
use warnings;
use Time::HiRes qw( clock );


sub range_divisor
{
    my ($low, $high) = @_;
    my $start = $high;
    while (1) {
        foreach my $i ($low..$high) {
            if ($start % $i != 0) {
                $start += $high;
                last;
            }
            elsif ($i == $high) {
                return $start;
            }
        }
    }
}

my $start = clock();
my $answer = range_divisor(1, 20);
my $stop = clock();
print "Answer: ", $answer, "\n";
printf "Time: %.5f\n", $stop - $start;
