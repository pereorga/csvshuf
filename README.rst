csvshuf
=======

Shuffle cells by column in CSV files.


Usage
-----

Shuffle the first column of each row of foobar.csv

    csvshuf -c1 foobar.csv

Shuffle the third column of each row of foobar.csv using Sattolo's
algorithm

    csvshuf -c3 -s foobar.csv

Shuffle all columns of foobar.csv

    csvshuf foobar.csv

Shuffle all the columns but the first of foobar.csv

    csvshuf -C1 foobar.csv

Shuffle the first and third columns of the first ten lines of foobar.csv

    head -10 foobar.csv | csvshuf -c 1,3

Shuffle the first and third columns of the pipe-delimited foobar.csv

    csvshuf -c1,3 -d "|" foobar.csv

Shuffle the first and third columns of the tab-delimited foobar.csv

    csvshuf -c 1,3 -t foobar.csv

Shuffle the first three columns of the pipe-delimited foobar.csv; output
will be comma-delimited

    csvshuf -c 1,2,3 -d "|" -o , foobar.csv

Shuffle the first three columns of the comma-delimited foobar.csv;
output will be pipe-delimited

    csvshuf -c 1,2,3 -o "|" foobar.csv

Shuffle the first two columns of the comma-delimited, pipe-quoted
foobar.csv

    csvshuf -c 1,2 -d "," -q "|" foobar.csv


Installation
------------

    pip install csvshuf


Author
------

Pere Orga pere@orga.cat, 2016.

Originally forked from csvcut (https://gist.github.com/bycoffe/187278).
