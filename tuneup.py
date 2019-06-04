#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Tyler Ward"

import cProfile
import pstats
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    pr = cProfile.Profile()
    pr.enable()
    pr.run(f'{func}')
    pr.disable
    sortby = 'cumulative'
    ps = pstats.Stats(pr).sort_stats(sortby)
    ps.print_stats()


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    if title in movies:
        return True
    return False


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)

    duplicates = []

    seen = {}
    for movie in movies:
        if movie not in seen:
            seen[movie] = 1
        else:
            if seen[movie] == 1:
                duplicates.append(movie)
            seen[movie] += 1

#     duplicates = [
#             movie 
#             for index, movie in enumerate(movies)
#                 if is_duplicate(movie, movies[:index])
#         ]

#     while movies:
#         movie = movies.pop()
#         if is_duplicate(movie, movies):
#             duplicates.append(movie)

    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(
        stmt='main()', 
        setup='import cProfile; import pstats'
    )
    result = t.repeat(repeat=7, number=3)
    avg_of_min = min([time/3 for time in result])
    print(f'Best time across 7 repeats of 5 runs per repeat: {avg_of_min} sec')


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    profile("find_duplicate_movies('movies.txt')")
    timeit_helper()


if __name__ == '__main__':
    main()
