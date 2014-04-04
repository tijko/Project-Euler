use strict;
use warnings;


sub fibonacci
{
    my ($t, $n, $ln, $limit);
    ($t, $n, $ln, $limit) = @_;

    if ($n >= $limit)
    {
        return $t;
    }
    elsif ($n % 2 == 0)
    {
        return fibonacci($t + $n, $n + $ln, $n, $limit);
    }
    return fibonacci($t, $n + $ln, $n, $limit);
}

my $answer = fibonacci(0, 2, 1, 4000000);
print "Answer: ", $answer, "\n";
