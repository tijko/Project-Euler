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
    for (my $i=3; $i < int(sqrt($n)) + 1; $i++) {
        if ($n % $i == 0) {
            return 0;
        }
    }
    return 1;
}

sub all_primes
{
    my ($limit) = @_;
    my $total = 0;
    for (my $i=2; $i < $limit; $i++) {
        if ((is_prime($i))) {
            $total += $i
        }
    }
    return $total;
}

my $start = clock();
my $answer = all_primes(2000000);
my $stop = clock();
print "Answer: ", $answer, "\n";
printf "Time: %.5f\n", $stop - $start;
