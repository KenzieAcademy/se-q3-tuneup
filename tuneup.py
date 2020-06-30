#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "Iris Hoffmeyer and StackOverflow contributors\
(https://stackoverflow.com/a/9835819, https://stackoverflow.com/a/282589)"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    profiler = cProfile.Profile()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        pstat = pstats.Stats(profiler)
        pstat.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats()
        return result

    return wrapper


def read_movies(src):
    """Returns a list of movie titles."""
    # print(f'Reading file: {src}')
    with open(src, 'r') as file_handle:
        return file_handle.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    seen = {}
    for movie in movies:
        if movie not in seen:
            seen[movie] = True
        else:
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    print("Now finding the best time over 7 repeats of 5 runs per repeat..")
    timer_for_dup_movies = timeit.Timer(
        stmt='find_duplicate_movies("movies.txt")',
        setup='from __main__ import find_duplicate_movies')
    result = timer_for_dup_movies.repeat(repeat=7, number=5)
    print("Best time across 7 repeats of 5 runs per repeat: {}"
          .format(min(result) / 5))


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
    # timeit_helper()
