#!venv/bin/ python3
# -*- coding: utf-8 -*-
"""
┬┌─┌─┐┬ ┬┌─┐┌─┐┬  ┬  ┌─┐┌┬┐┌─┐┬─┐
├┴┐├┤ └┬┘│  │ ││  │  ├─┤ │ │ │├┬┘
┴ ┴└─┘ ┴ └─┘└─┘┴─┘┴─┘┴ ┴ ┴ └─┘┴└─
Description:
    Compares text in a file to reference/glossary/key-items/dictionary file.
Copyright (C) 2022 Rush Solutions, LLC
Author: David Rush <davidprush@gmail.com>
License: MIT
Example:

        $ python keycollator.py

        *Notes

Todo:

        *

"""
import sys
import click
from extractonator import ZTimer, KeyKrawler

# Default file names
LOGZ = "log.log"
TXTS = "text.txt"
REZF = "results.csv"
KEYZ = "keys.txt"


@click.group(
    context_settings=dict(
        ignore_unknown_options=True,
    ),
    invoke_without_command=True)
@click.option(
    '-v', '--set-verbose',
    is_flag=True,
    # default=0,
    # type=click.IntRange(0, 5, clamp=True),
    help="Turn on verbose"
)
@click.option(
    '-f', '--fuzzy-matching',
    default=99,
    type=click.IntRange(0, 99, clamp=True),
    help='''Find valid matches using edit distances or
        approximate matches, uses acceptance ratio of
        integer values from 0 to 99, where 99 is near identical'''
)
@click.option(
    '-k', '--key-file',
    default=KEYZ,
    type=click.Path(exists=True),
    help='''Path/file name of the key file containing a
        dictionary, key items, glossary, or reference
        list used to search the text file'''
)
@click.option(
    '-t', '--text-file',
    default=TXTS,
    type=click.Path(exists=True),
    help='''Path/file name of the text to be searched
    for against items in the key file'''
)
@click.option(
    '-o', '--output-file',
    default=REZF,
    type=click.Path(exists=True),
    help="Path/file name of the output file that \
        will contain the results (CSV or TXT)"
)
@click.option(
    '-U', '--ubound-limit',
    default=99999,
    type=click.IntRange(1, 99999, clamp=True),
    help="""
        Ignores items from the results with
        matches greater than the upper boundary (upper-limit);
        reduce eroneous matches
        """
)
@click.option(
    '-L', '--lbound-limit',
    default=0,
    type=click.IntRange(0, 99999, clamp=True),
    help="""
        Ignores items from the results with
        matches less than the lower boundary (lower-limit);
        reduce eroneous matches
        """
)
@click.option(
    '-l', '--set-logging',
    is_flag=True,
    help="Turn on logging"
)
@click.option(
    '-Z', '--log-file',
    default=LOGZ,
    type=click.Path(exists=True),
    help="Path/file name to be used for the log file"
)
def cli(
    set_verbose,
    fuzzy_matching,
    key_file,
    text_file,
    output_file,
    ubound_limit,
    lbound_limit,
    set_logging,
    log_file,
):
    """
    keycollator is an app that finds occurances of keys in a text file
    """
    krawler = KeyKrawler(
        text_file,
        key_file,
        output_file,
        log_file,
        set_verbose,
        ubound_limit,
        lbound_limit,
        fuzzy_matching
    )
    krawler.echo_stats()


def main(**kwargs):
    zt.stopit(sys._getframe().f_code.co_name)
    zt.echo(False, sys._getframe().f_code.co_name)


if __name__ == '__main__':
    zt = ZTimer(sys._getframe().f_code.co_name)
    cli()
    main(zt)
