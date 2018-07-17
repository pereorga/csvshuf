csvshuf
=======

Shuffle cells by column in CSV files.

Usage
-----

.. code-block:: bash

    csvfaker [-h] [-f] [-r ROWS] [-l LOCALE] [-s SEED] [-n]
             [-p REPLACE_NEWLINE] [-d DELIMITER] [--version]
             [FAKE [FAKE ...]]

    positional arguments:
      FAKE                  The name of the fake(s) to use to generate output,
                            separated by space. Will also be used as column
                            headers. If omitted, the fakes 'name job state' will
                            be used.

    optional arguments:
      -f, --list-fakes      Show a list of all available fakes.
      -r ROWS, --rows ROWS  Number of rows to generate. If omitted it defaults to
                            10.
      -l LOCALE, --locale LOCALE
                            Locale to use. Examples: 'en_US', 'es'.
      -s SEED, --seed SEED  Seed to use. Generated result will be the same when
                            called with the same seed.
      -n, --no-headers-row  Do not output columns headers.
      -p REPLACE_NEWLINE, --replace-newline REPLACE_NEWLINE
                            Replace newline character with provided string.
      -d DELIMITER, --delimiter DELIMITER
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
