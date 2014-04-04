use strict;
use warnings;


sub palindrome
{
    my $high = 0;
    my $product;
    foreach my $i (100..999)
    {
        foreach my $j (100..999) {
            $product = $i * $j;
            if ($product eq reverse($product) && $product > $high)
            {
                $high = $product;
            }
        }
    }
    return $high;
}

my $answer = palindrome();
print "Answer: ", $answer, "\n";
