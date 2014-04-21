use strict;
use warnings;
use Time::HiRes qw( clock );


sub permute
{
    my @arr = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
    for my $perm (1..999999) {
        my $len = scalar(@arr);
        my $i = $len - 2;
        my ($l1, $l2);
        my $f = "";
        for (; $i >= 0; $i--) {
            if ($arr[$i] lt $arr[$i + 1]) {
                $l1 = $i;
                $f = $arr[$i];
                last;
            }
        }   
        my $low = "";      
        for (; $i <= $len - 1; $i++) {
            if ($arr[$i] gt $f) {
                if ($low eq "") {
                    $l2 = $i;
                    $low = $arr[$i];
                } elsif ($low gt $arr[$i]) {
                    $l2 = $i;
                    $low = $arr[$i];
                }
            }
        }
        my $temp = $arr[$l2];
        $arr[$l2] = $arr[$l1];
        $arr[$l1] = $temp;
        if (!($l1 >= $len - 1)) {
            @arr = (@arr[0..$l1], sort(@arr[$l1 + 1..$len - 1]));
        }
    }
    return join("", @arr);
}

my $start = clock();
my $answer = permute();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
