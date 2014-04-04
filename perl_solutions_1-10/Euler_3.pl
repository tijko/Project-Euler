use strict;
use warnings;
use Math::Complex;

sub primes
{
    my ($n);
    ($n) = @_;
    if ($n == 2)
    {
        return 1;
    }
    if ($n % 2 == 0 || $n == 1)
    {
        return 0;
    }
    foreach my $i (3..int(sqrt($n)) + 1)
    {
        if ($n % $i == 0)
        {
            return 0;
        }
    }
    return 1;
}

sub largest_factor
{
    my $factor;
    ($factor) = @_;
    my $high = 0;
    foreach my $i (1..int(sqrt($factor)))
    {
        if ($factor % $i == 0 && (primes($i)))
        {
            $high = $i;
        }
    }
    return $high;
}

my $answer = largest_factor(600851475143);
print "Answer: ", $answer, "\n";
