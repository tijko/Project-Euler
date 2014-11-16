use strict;
use warnings;
use Time::HiRes qw( clock );


sub swap
{
    my ($perm_ref, $idx1, $idx2) = @_;
    my $tmp;

    $tmp = $perm_ref->[$idx1];
    $perm_ref->[$idx1] = $perm_ref->[$idx2];
    $perm_ref->[$idx2] = $tmp;
}

sub first_index
{
    my (@permutation) = @_;
    my $idx;

    for ($idx=$#permutation; $idx > 0; $idx--) {
        if ($permutation[$idx] gt $permutation[$idx - 1]) {
            return $idx - 1;
        }
    }   

    return $idx
}

sub second_index
{
    my ($idx1, @permutation) = @_;
    my $idx2;

    for ($idx2=$#permutation; $idx2 > $idx1; $idx2--) {
        if ($permutation[$idx1] lt $permutation[$idx2]) {
            return $idx2;
        }
    }

    return $idx2;
}

sub permute
{
    my @one_to_ten = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
    my ($permutation, $idx1, $idx2);

    for ($permutation=1; $permutation < 1000000; $permutation++) {

        $idx1 = first_index(@one_to_ten);
        $idx2 = second_index($idx1, @one_to_ten);
        swap(\@one_to_ten, $idx1, $idx2);
        @one_to_ten = (@one_to_ten[0..$idx1], 
                       sort(@one_to_ten[$idx1 + 1..$#one_to_ten]));
    }
    return join("", @one_to_ten);
}

my $start = clock();
my $answer = permute();
my $stop = clock();
print "Answer: $answer\n";
printf "Time: %.5f\n", $stop - $start;
