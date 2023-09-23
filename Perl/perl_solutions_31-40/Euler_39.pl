use strict;
use warnings;
use Time::HiRes qw( clock );
use Math::Complex;


sub max_triangle
{
    my $max = 0;
    my $tri_max = 0;
    my %triangles;
    for my $a (1..999) {
        for my $b (3..1000) {
            my $triangle = sqrt($a**2 + $b**2);
            if ($triangle / 1 - (int($triangle / 1)) == 0 && ($a + $b + $triangle <= 1000)) {
                my $sum = $a + $b + $triangle;
                if ($triangles{$sum}) {
                    $triangles{$sum} += 1;
                } else {
                    $triangles{$sum} = 1;
                }
            }
        }
    }
    for my $tri (keys %triangles) {
        if ($triangles{$tri} > $max) {
            $max = $triangles{$tri};
            $tri_max = $tri;
        }
    }
    return $tri_max;
}


my $start = clock();
my $answer = max_triangle();
my $stop = clock();

print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
