#!/usr/bin/perl

########################################################
# sequence_sum.pl
#
# Find sum of any sequential numbers begining with $begin
# and ending with $end
#########################################################

if ($#ARGV + 1 != 2)
{
    print "Usage: sequence_sum.pl <begin> <end>","\n";
    exit(1);
}

$begin = $ARGV[0];
$end = $ARGV[1];
$sum = 0;

# Find the number using a for loop:
foreach my $i ($begin..$end)
{
    $sum += $i;
}
print "Sum with for loop = $sum\n"; # expects sum = 105

# Find the number using a formula:
$sum2 = ( $end*($end+1)/2 - ($begin - 1)*($begin)/2 );
print "Sum with formula = $sum2\n";
