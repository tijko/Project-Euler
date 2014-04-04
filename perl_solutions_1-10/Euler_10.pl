use strict;
use warnings;
use Math::Complex;


sub is_prime
{
    my $n;
    ($n) = @_;

    if ($n == 2)
    {
        return 1;
    }
    if ($n % 2 == 0 || $n == 1)
    {
        return 0;
    }
    for (my $i=3; $i < int(sqrt($n)) + 1; $i++)
    {
        if ($n % $i == 0)
        {
            return 0;
        }
    }
    return 1;
}

sub all_primes
{
    my $limit;
    ($limit) = @_;

    my $total = 0;
    for (my $i=2; $i < $limit; $i++)
    {
        if ((is_prime($i)))
        {
            $total += $i
        }
    }
    return $total;
}

my $answer = all_primes(2000000);
print "Answer: ", $answer, "\n";
