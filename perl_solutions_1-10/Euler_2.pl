use strict;
use warnings;
use Time::HiRes qw( clock );


sub fibonacci
{
    my ($t, $n, $ln, $limit) = @_;
    if ($n >= $limit) {
        return $t;
    }
    elsif ($n % 2 == 0) {
        return fibonacci($t + $n, $n + $ln, $n, $limit);
    }
    return fibonacci($t, $n + $ln, $n, $limit);
}

my $start = clock();
my $answer = fibonacci(0, 2, 1, 4000000);
my $stop = clock();
print "Answer: ", $answer, "\n";
printf "Time: %.5f\n", $stop - $start;
