use strict;
use warnings;
use Time::HiRes qw( clock );


sub grid
{
    my ($step, @axis) = @_;
    my $total = $step;
    for my $i (@axis) {
        $step += $i;
        if ($step > $axis[$#axis - 1]) {
            last;
        }
        $total += $step;
    }
    return $total;
}

sub spiral_path
{
    my $diag = 3;
    my $total = 0;
    my @path = (10, 12, 14);
    for my $i (1..1001) {
        if ($i % 2 != 0) {
            $total += $i**2;
        }
    }
    for my $i (@path) {
        my @spiral;
        do {
            push(@spiral, $i);
            $i += 8;
        } until ($i >= 1002002);
        $total += grid($diag, @spiral);
        $diag += 2; 
    }
    return $total;
}


my $start = clock();
my $answer = spiral_path();
my $stop = clock();

print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
