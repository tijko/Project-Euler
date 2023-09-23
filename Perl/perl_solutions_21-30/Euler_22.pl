use strict;
use warnings;
use Time::HiRes qw( clock );


sub name_sum
{
    my $total = 0;
    my $pos = 1;
    open(my $f, "/home/tijko/Project_Euler/euler_txt/names1.txt");
    my @name_list = sort((split('"', <$f>)));
    for my $name (@name_list) {
        if (length($name) > 1) {
            my $name_total = 0;
            for my $letter (split(//, $name)) {
                $name_total += (ord($letter) - 64);
            }
            $total += ($name_total * $pos);
            $pos++;
        }
    }
    return $total;
}

my $start = clock();
my $answer = name_sum();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
