use strict;
use warnings;
use Time::HiRes qw( clock );


sub change_combos
{
    my $ways = 0;
    for my $i (0..1) {
        $i *= 200;
        for my $j (0..2) {
            $j *= 100;
            FIFTY: for my $l (0..4) {
                $l *= 50;
                if ($l + $j + $i > 200) {
                    next;
                }
                TWENTY: for my $v (0..10) {
                    $v *= 20;
                    if ($v + $l + $j + $i > 200) {
                        next FIFTY;
                    }
                    TEN: for my $k (0..20) {
                        $k *= 10;
                        if ($k + $v + $l + $j + $i > 200) {
                            next TWENTY;
                        }
                        FIVE: for my $m (0..40) {
                            $m *= 5;
                            if ($m + $k + $v + $l + $j + $i > 200) {
                                next TEN;
                            }
                            TWO: for my $e (0..100) {
                                $e *= 2;
                                if ($e + $m + $k + $v + $l + $j + $i > 200) {
                                    next FIVE;
                                }
                                for my $x (0..200) {
                                    my $combo = $i + $j + $l + $v + $k + $m + $e + $x;
                                    if ($combo > 200) {
                                        next TWO;
                                    } elsif ($combo == 200) {
                                        $ways++;
                                        next TWO;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return $ways;
}


my $start = clock();
my $answer = change_combos();
my $stop = clock();

print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
