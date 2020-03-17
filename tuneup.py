#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Sean Bailey, Koren Niles, Chris Wilson"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    def wrapper_fun(*args, **kwargs):
        profile_object = cProfile.Profile()
        profile_object.enable()
        result = func(*args, **kwargs)
        profile_object.disable()
        pstats.Stats(profile_object).strip_dirs(
        ).sort_stats('cumulative').print_stats()
        return result
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
    print('Reading file: {}'.format(src))
    with open(src, 'r') as movies:
        movies = sorted(movies.read().splitlines())
    duplicates = []
    previous_name = ""
    for movie in sorted(movies):
        if previous_name == movie:
            duplicates.append(movie)
        previous_name = movie
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(
        stmt="""find_duplicate_movies("movies.txt")""",
        setup="""from __main__ import find_duplicate_movies"""
    )
    runtime = t.repeat(repeat=7, number=3)
    # average_runtime = sum(runtime) / len(runtime)
    return ("From timeit_helper, find_duplicate_movies takes an average of {} \n \seconds to run.".format(min(runtime)/3))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print(timeit_helper())
    print('Found {} duplicate movies: \n{}'.format(
        len(result), "\n".join(result)))


if __name__ == '__main__':
    main()
