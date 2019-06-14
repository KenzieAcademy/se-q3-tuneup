#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Tyler Ward"

import cProfile
import pstats
import timeit
from collections import Counter
import functools


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        sortby = 'cumulative'
        ps = pstats.Stats(pr).sort_stats(sortby)
        ps.print_stats(10)
        return result
    return inner



def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    return title in movies


def sort_movies(src):
    result = sorted([
        movie.lower() 
            for movie in read_movies(src)
    ])

    assert result is not None
    return result

@profile
def find_duplicate_movies_zip(src):
    movies = sort_movies(src)

    return [
        m1 
            for m1, m2 in zip(movies[1:], movies[:-1])
                 if m1 == m2
    ]


@profile
def find_duplicate_movies_counter(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)

    movie_counter = Counter(movies)

    duplicates = [
        movie 
            for movie, count in movie_counter.items() 
                if count > 1
    ]

    return duplicates


@profile
def find_duplicate_movies_boss(src):
    movies = read_movies(src)
    duplicates = []
    seen={}
    for movie in movies:
        if movie not in seen:
            seen[movie] = 1
        else:
            if seen[movie] == 1:
                duplicates.append(movie)
            seen[movie] += 1

    return duplicates


@profile
def find_duplicate_movies_list_comp(src):
    movies = read_movies(src)

    duplicates = [
            movie 
            for index, movie in enumerate(movies)
                if is_duplicate(movie, movies[:index])
        ]
    
    return duplicates


@profile 
def find_duplicate_movies_while(src):
    movies = read_movies(src)
    duplicates = []

    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)

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
    movie_funcs = [
        find_duplicate_movies_boss, 
        find_duplicate_movies_counter,
        find_duplicate_movies_list_comp,
        find_duplicate_movies_while,
        find_duplicate_movies_zip
    ]
    for func in movie_funcs:
        print(f'\n\nHey this is the function {func.__name__}:\n\n')
        result = func('movies.txt')
        print('Found {} duplicate movies:'.format(len(result)))
        print('\n'.join(result))
    # timeit_helper()


if __name__ == '__main__':
    main()
