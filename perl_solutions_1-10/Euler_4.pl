use strict;
use warnings;
use Time::HiRes qw( clock );


sub palindrome
{
    my $high = 0;
    my $product;
    foreach my $i (100..999) {
        foreach my $j (100..999) {
            $product = $i * $j;
            if ($product eq reverse($product) && $product > $high) {
                $high = $product;
            }
        }
    }
    return $high;
}

my $start = clock();
my $answer = palindrome();
my $stop = clock();
print "Answer: ", $answer, "\n";
printf "Time: %.5f\n", $stop - $start;
