use strict;
use warnings;
use Math::Complex;
use Time::HiRes qw( clock );


sub triangle_divisors
{
    my $divisors = 0;
    my $triangle = 1001;
    my $tri = 0;
    foreach my $i (0..1001) {
        $tri += $i;
    }   
    while ($divisors <= 500) {
        foreach my $i (2..int(sqrt($tri)) + 1) {
            if ($tri % $i == 0) {
                $divisors += 1;
            }
        }
        if ($divisors * 2 <= 500) {
            $triangle += 1;
            $tri += $triangle;
            $divisors = 0;
        }
    }
    return $tri;
}

my $start = clock();
my $answer = triangle_divisors();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
