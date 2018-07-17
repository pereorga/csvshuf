csvshuf
=======

Shuffle cells by column in CSV files.

Usage
-----

.. code-block:: bash

    usage: csvshuf [-h] [-s] [-c COLUMNS | -C NO_COLUMNS] [-d DELIMITER | -t]
                   [-q QUOTECHAR] [-o OUTPUT_DELIMITER] [-v]
                   [FILE]

    positional arguments:
      FILE                  Input CSV file. If omitted, read standard input.

    optional arguments:
      -s, --sattolo         Use Sattolo's shuffle algorithm.
      -c COLUMNS, --columns COLUMNS
                            Comma-separated list of columns to include.
      -C NO_COLUMNS, --no-columns NO_COLUMNS
                            Comma-separated list of columns to exclude.
      -d DELIMITER, --delimiter DELIMITER
                            Input column delimiter.
      -t, --tabbed          Delimit input with tabs.
      -q QUOTECHAR, --quotechar QUOTECHAR
                            Quote character.
      -o OUTPUT_DELIMITER, --output-delimiter OUTPUT_DELIMITER
                            Output column delimiter.


Examples
--------

Shuffle the first column of foobar.csv

    csvshuf -c1 foobar.csv

Shuffle the third column of foobar.csv using Sattolo's algorithm

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

or

    pip3 install csvshuf


Author
------

Pere Orga pere@orga.cat, 2016.

Originally forked from csvcut (https://gist.github.com/bycoffe/187278).
