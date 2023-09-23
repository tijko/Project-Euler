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
    if ($n == 1 || $n % 2 == 0) {
        return 0;
    }
    for my $i (3..int(sqrt($n)) + 1) {
        if ($n % $i == 0) {
            return 0;
        }
    }
    return 1;
}

sub quadratic_primes
{
    my $max = 0;
    my $co_prod = 0;
    for my $i (-999..999) {
        for my $j (-999..999) {
            my $primes = 0;
            my $q = $primes**2 + ($primes * $j) + $i;
            while (is_prime(abs($q))) {
                $primes++;
                $q = $primes**2 + ($primes * $j) + $i;
            }
            if ($primes > $max) {
                $max = $primes;
                $co_prod = $i * $j;
            }
        }
    }
    return $co_prod;
}
    

my $start = clock();
my $answer = quadratic_primes();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
