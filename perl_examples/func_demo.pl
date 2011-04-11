#!/usr/bin/perl

sub myname;

$me = myname($ARGV[0],1,1,1) or die "can't get myname";

print $me,"\n";


sub myname
{
    ($name) = @_;
    return $name;
}
