#!/usr/bin/perl -w

# List main global variables
$word = "";
$line = "";
$dict_filename = "dictionary.txt";

&check_valid_args($#ARGV);
&open_dictionary;
&find_word;
&print_word;
&close_dictionary;

sub check_valid_args
{
    my $args = @_;
    if ($args != 1)
    {
        print "Usage: my_dict <word>\n";
        exit(1);
    }
    $word = $ARGV[0];
}

sub open_dictionary
{
    open (DICT_FILE, "<$dict_filename") or die $!;
}

sub find_word
{
    my ($my_line, $my_word,@my_word_list, $definition);
    FORLOOP:
    {
    for $my_line (<DICT_FILE>)
    {
        @my_word_list = split(/ /, $my_line);
        $my_word = $my_word_list[0];
        if ($my_word eq $word)
        {
            # we found the word. save the whole line and exit.
            $line = $my_line;
            last FORLOOP;
        }
    }
    }
}

sub print_word
{
    print $line;
}

sub close_dictionary
{
    close DICT_FILE;
}
