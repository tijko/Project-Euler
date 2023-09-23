use strict;
use warnings;
use Time::HiRes qw( clock );


sub tri_path
{
    my @triangle;
    my $path = "/home/tijko/Project_Euler/euler_txt/triangle1.txt";
    open (my $tri, $path);
    while (my $i = <$tri>) {
        chomp($i);
        my @row = split(" ", $i);
        @triangle = (@triangle, \@row);
    }
    close $tri;
    my $total = $triangle[0][0] + 10;
    my $col = 0;
    my $row = 1;
    while ($row < scalar(@triangle)) {
        if ($triangle[$row][$col] < $triangle[$row][$col + 1]) {
            $total += $triangle[$row][$col + 1];
            $col += 1;
            $row += 1;
            next;
        }
        $total += $triangle[$row][$col];
        $row += 1;
    }
    return $total;
}

my $start = clock();
my $answer = tri_path();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
