#!/usr/bin/perl

@array = ("hi", "how", "are", "you");

for my $word (@array)
{
    print $word, "\n";
    if ($word eq "are")
    {
        last;
    }
}
