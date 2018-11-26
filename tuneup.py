#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Jake Johnson"

import cProfile
import pstats
import timeit
from collections import Counter


def profile(func):
    """A function that can be used as a decorator to meausre performance"""
    def function_wrapper(x):
        pr = cProfile.Profile()
        pr.enable()
        func(x)
        pr.disable()
        stats = pstats.Stats(pr).sort_stats('cumulative')
        stats.print_stats()
    return function_wrapper


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movie_counter = Counter([x.lower() for x in read_movies(src)])
    duplicates = [k for k, v in movie_counter.items() if v > 1]
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    n = 8
    r = 6
    t = timeit.Timer(lambda: find_duplicate_movies('movies.txt'))
    result = t.repeat(repeat=r, number=n)
    result = [x / n for x in result]
    print'Best time across {} repeats of {} runs per repeat: {} sec'.format(
        r, n, min(result))


def main():
    """Computes a list of duplicate movie entries"""
    find_duplicate_movies('movies.txt')
    timeit_helper()
#     result = find_duplicate_movies('movies.txt')
#     print('Found {} duplicate movies:'.format(len(result)))
#     print('\n'.join(result))


if __name__ == '__main__':
    main()
