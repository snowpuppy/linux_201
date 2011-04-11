#!/usr/bin/perl


if ($#ARGV >= 0)
{
    $who = join(' ', @ARGV);
}
else
{
    $who = 'Everyone';
}

print "Hello, $who!\n";
