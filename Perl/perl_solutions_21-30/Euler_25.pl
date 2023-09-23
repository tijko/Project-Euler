use strict;
use warnings;
use Math::BigInt;
use Time::HiRes qw( clock );


sub milli_fib
{
    my($x, $y, $x0, $z);
    $x = Math::BigInt->new("1");
    $y = Math::BigInt->new("0");
    $z = 1;
    do {
        $x0 = $x->copy()->badd($y);
        $y = $x->copy();
        $x = $x0->copy();
        $z +=1; 
    } until (length($x) >= 1000); 
    return $z;
}

my $start = clock();
my $answer = milli_fib();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
