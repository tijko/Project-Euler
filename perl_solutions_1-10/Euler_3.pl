use strict;
use warnings;
use Math::Complex;
use Time::HiRes qw( clock );


sub is_prime
{
    my ($n) = @_;
    if ($n == 2) {
        return 1;
    }
    if ($n % 2 == 0 || $n == 1) {
        return 0;
    }
    for my $i (3..int(sqrt($n)) + 1) {
        if ($n % $i == 0) {
            return 0;
        }
    }
    return 1;
}

sub largest_factor
{
    my ($factor) = @_;
    my $high = 0;
    for my $i (1..int(sqrt($factor)) + 1) {
        if ($factor % $i == 0 && (is_prime($i))) {
            $high = $i;
        }
    }
    return $high;
}

my $start = clock();
my $answer = largest_factor(600851475143);
my $stop = clock();
print "Answer: ", $answer, "\n";
printf "Time: %.5f\n", $stop - $start;
