use Math::BigFloat;

Math::BigFloat->div_scale(400);

my $x = Math::BigFloat->new(1);
my $y = $x->copy();
my $top = 0;
my $high = 0;
foreach my $i (2..999) {
    $x->bdiv($i);
    if ($i == 983) {
        print "$x\n";
    }
    foreach my $j (3..50) {
        my $sl = substr($x, 2, $j);
        if ($sl and length($sl) == $j) {
            if ($x =~ /$sl/ and $j > $high) {
                $top = $i;
                $high = $j;
            }
        } else {
            next;
        }
    }
    $x = $y;
    $y = $x->copy();
}

#print "$high\n";
#print "$top\n";
