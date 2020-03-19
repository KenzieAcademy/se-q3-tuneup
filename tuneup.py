#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "benjmm with help from knmarvel and Janell-Huyck's wonderful guide"

import cProfile
import pstats
import functools
import sys
import timeit

if sys.version_info[0] < 3:
    raise Exception("This program requires python3 interpreter")


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    @functools.wraps(func)
    def wrapper_fun(*args, **kwargs):
        profile_object = cProfile.Profile()
        profile_object.enable()
        result = func(*args, **kwargs)
        profile_object.disable()
        stats_object = pstats.Stats(profile_object)
        stats_object.strip_dirs()
        stats_object.sort_stats('cumulative')
        stats_object.print_stats()
        return(result)
    return wrapper_fun


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    setup_code = """from __main__ import find_duplicate_movies"""
    statement_code = """find_duplicate_movies("movies.txt")"""
    repeat = 7
    number = 3
    t = timeit.Timer(setup=setup_code, stmt=statement_code)
    result = t.repeat(repeat=repeat, number=number)
    averages = [cum/3 for cum in result]
    print('Best time across {} repeats of {} runs per repeat: {} sec'.format(
        repeat, number, min(averages)))


def main():
    """Computes a list of duplicate movie entries"""
    # timeit_helper()
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
