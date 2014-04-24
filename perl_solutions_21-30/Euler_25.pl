use strict;
use warnings;
use Math::BigInt;
use Time::HiRes qw( clock );


sub milli_fib
{
    my $x = Math::BigInt->new("1");
    my $y = Math::BigInt->new("0");
    my $x0 = $x->copy();
    my $y0 = $y->copy();
    my $x1 = $x->copy();
    my $z = 0;
    do {
        my $x0 = $x1->bmuladd(2, $y);
        my $y0 = $y->badd($x);
        $x = $x0->copy();
        $y = $y0->copy();
        $x1 = $x->copy();
        $z +=2; 
    } until (length($x) >= 1000); 
    return $z;
}

my $start = clock();
my $answer = milli_fib();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
