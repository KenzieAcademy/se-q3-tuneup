#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "iam2anangel"  # Jen Browning

import cProfile
import pstats
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # cProfile.run(pr_func)
    def profile_function(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        pr_func = func(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr).sort_stats('cumulative')
        ps.print_stats()
        return pr_func
    return profile_function


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    return set([movie for movie in movies if movies.count(movie) > 1])


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = min(timeit.Timer('find_duplicate_movies("movies.txt")', setup='from __main__ import find_duplicate_movies').repeat(
        repeat=7, number=3))
    print "Best time across 7 repeats of 3 runs per repeat: {} sec".format(t)


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
