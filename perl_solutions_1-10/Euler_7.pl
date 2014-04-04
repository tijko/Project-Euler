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
    foreach my $i (3..int(sqrt($n)) + 1)
    {
        if ($n % $i == 0)
        {
            return 0;
        }
    }
    return 1;
}

sub find_prime
{
    my $prime_num;
    ($prime_num) = @_;

    my $num_prime = 0;
    my $prime = 1;
    while ($num_prime < $prime_num)
    {
        $prime++;
        if (is_prime($prime))
        {
            $num_prime++;
        }
    }
    return $prime;
}

my $answer = find_prime(10001);
print "Answer: ", $answer, "\n";
