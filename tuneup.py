#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "iam2anangel"  # Jen Browning

import cProfile
import pstats
import timeit

#


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def wrapper():
        prof = cProfile.Profile()
        prof.enable()
        prof.runcall(func)
        prof.disable()
      return wrapper



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
    number = 10
    repeat = 3
    t = timeit.Timer(stmt=timeit_helper,
                     setup='text = "sample string"; char = "g"')
    result = t.repeat(repeat=7, number=3)

@profile
def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))




if __name__ == '__main__':
    main()
