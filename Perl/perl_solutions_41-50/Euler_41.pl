use strict;
use warnings;
use Time::HiRes qw( clock );
use Math::Complex;


sub is_prime
{
    my ($n) = @_;
    if ($n == 2) {
        return 1;
    }
    if ($n == 1 or $n % 2 == 0) {
        return 0;
    }
    for my $i (3..int(sqrt($n) + 1)) {
        if ($n % $i == 0) {
            return 0;
        }
    }
    return 1;
}

sub pandigital_prime
{
    my @pan = ('9', '8', '7', '6', '5', '4', '3', '2', '1');
    my $len = $#pan;
    my $st = 0;
    while (1) {
        my @primes = permute(@pan[$st..$len]);
        if ($#primes > 0) {
            my $high = 0;
            for my $i (@primes) {
                if ($i > $high) {
                    $high = $i;
                }
            }
            return $high;
        }
        $len = $#pan; 
        $st++;
    }
}

sub permute
{
    my (@pan) = @_;
    my @primes;
    my $len = scalar(@pan);
    my ($l1, $l2) = (0, 0);
    my $f = "";
    my $cur = join("", @pan);
    while (1) { 
        my $i = $len - 2;
        for (; $i >= 0; $i--) {
            if ($pan[$i] lt $pan[$i + 1]) {
                $l1 = $i;
                $f = $pan[$i];
                last;
            }
        }
        my $low = "";
        for (; $i <= $len - 1; $i++) {
            if ($pan[$i] gt $f) {
                if ($low eq "") {
                    $l2 = $i;
                    $low = $pan[$i];
                } elsif ($low gt $pan[$i]) {
                    $l2 = $i;
                    $low = $pan[$i];
                }
            }
        }
        my $temp = $pan[$l2];
        $pan[$l2] = $pan[$l1];
        $pan[$l1] = $temp;
        if (!($l1 >= $len - 1)) {
            @pan = (@pan[0..$l1], sort(@pan[$l1 + 1..$len - 1]));
        }
        if (is_prime(join("", @pan))) {
            push @primes, join("", @pan);
        } elsif (join("", @pan) eq $cur) {
            return @primes;
        }
    }
}

my $start = clock();
my $answer = pandigital_prime();
my $stop = clock();

print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
