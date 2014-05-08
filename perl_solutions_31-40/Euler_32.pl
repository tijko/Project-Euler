use strict;
use warnings;
use Time::HiRes qw( clock );


sub base10_pandigital
{
    my %matches;
    my $total;
    my $base = '123456789';
    my $pandigital;
    for my $i (100..4999) {
        for my $j (2..99) {
            $pandigital = join("", ($i * $j, $i, $j));
            $pandigital = join("", sort {$a cmp $b} split(//, $pandigital));
            if ($base eq $pandigital) {
                $matches{$i * $j} = 1;
            }
        }
    }
    for my $i (keys %matches) {
        $total += $i
    }
    return $total;
}


my $start = clock();
my $answer = base10_pandigital();
my $stop = clock();

print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
