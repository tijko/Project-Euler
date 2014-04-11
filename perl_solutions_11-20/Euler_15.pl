use strict;
use warnings;
use Time::HiRes qw( clock );
use Math::BigInt;


sub all_paths
{
    my $xstr = "20";
    my $xystr = "40";
    my $xy = Math::BigInt->new($xystr);
    my $x = Math::BigInt->new($xstr);
    $x->bfac();
    $xy->bfac();
    $x->bmul($x);
    return $xy->bdiv($x);
}

my $start = clock();
my $answer = all_paths();
my $stop = clock();
print "Answer: $answer\n";
printf "Time; %.5f\n", $stop - $start;
