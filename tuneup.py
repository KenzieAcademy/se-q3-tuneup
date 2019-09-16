#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "dchristenson"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""

    @functools.wraps(func)
    def inner(*args, **kwargs):
        c = cProfile.Profile()
        c.enable()
        result = func(*args, **kwargs)
        c.disable()
        sort_by = 'cumulative'
        cs = pstats.Stats(c).sort_stats(sort_by)
        cs.print_stats()
        return result
    return inner


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
    movies_dict = {}
    duplicates = []
    for movie in movies:
        if movie not in movies_dict:
            movies_dict[movie] = movie
        else:
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Timed function to measure performance"""
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")',
                     setup='from __main__ import find_duplicate_movies')
    runs_per_call = 3
    repeats = 7
    result = t.repeat(repeat=repeats, number=runs_per_call)
    print(min(result) / float(runs_per_call))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
