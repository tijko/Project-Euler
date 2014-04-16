use strict;
use warnings;
use Time::HiRes qw( clock );


sub first_sundays
{
    my $sundays = 0;
    my $dayofweek = 1;
    my @Feb;
    for my $i (1901..2000) {
        if ($i % 4 == 0) {
            @Feb = (1..29);
        } else {
            @Feb = (1..28);
        }
        my @Jan = my @Mar = my @May = my @Jul = my @Aug = my @Oct = my @Dec = (1..31);
        my @Apr = my @Jun = my @Sep = my @Nov = (1..30);
        my @year = (\@Jan, \@Feb, \@Mar, \@Apr, \@May, \@Jun, 
                    \@Jul, \@Aug, \@Sep, \@Oct, \@Nov, \@Dec);
        foreach my $mos (@year) {
            foreach my $day (@$mos) {
                if ($dayofweek == $day && $day == 1) {
                    $sundays++;
                }
                $dayofweek++;
                if ($dayofweek > 7) {
                    $dayofweek = 1;
                }
            }
        }
    }
    return $sundays;
}

my $start = clock();
my $answer = first_sundays();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop -$start;
