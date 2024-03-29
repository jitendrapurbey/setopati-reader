# Setopati Python Feed Reader

The Setopati Feed Reader is a basic [web feed](https://en.wikipedia.org/wiki/Web_feed) reader that can download the latest new from the Setopati news [Setopati feed](https://setopati.net/feed).

## Installation

You can install the Setopati Feed Reader from [PyPI](https://pypi.org/project/setopati-reader/):

    pip install setopati-reader

The reader is supported on Python 2.7, as well as Python 3.4 and above.

## How to use

The Setopati Feed Reader is a command line application, named `setopati`. To see a list of news simply call the program:

    $ setopati
    The latest tutorials from Setopati – Nepal's Digital Newspaper (https://setopati.net)
    0 Trump, Xi to talk trade
    1 Trump says he could meet Kim at DMZ
    2 Govt will have to spend almost Rs 1 billion for IIFA Awards
    3 SC asks govt reasons for doling out Rs 60m to federal lawmakers
    4 This govt will serve for five years: Barsha Man Pun
    5 Don’t meddle in the election: Trump jokes with Putin
    6 Man involved in attacks on women with pointed objects arrested
    7 Rivals target Biden as Democrats’ rifts emerge on race, age
    8 Boeing aims to finish software fix to 737 Max in September
    9 Oli woos ministers with Maoist background assuring there’ll be no cabinet reshuffle


You can also call the Real Setopait Feed Reader in your own Python code, by importing from the `reader` package:

    >>> from reader import feed
    >>> feed.get_titles()
    ['Trump, Xi to talk trade', ...]

