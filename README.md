<img height="120px" src="img/sluggish.jpg" />

# Tuneup Time
In this project, you will tune up some code that is not performing well. By "not performing" we mean that it's terribly inefficient at what it is trying to do: Eliminating duplicate entries in a list of popular movie titles. Although the code is bad, it's representative of what you might encounter in the Real World&#8482;.

## Objectives
- Hands-on experience with the `timeit` module
- Hands-on experience with `cProfile`
- Writing a decorator function
- Using profile results to enhance performance

There is a lot of material wrapped up in this seemingly sparse exercise. You are not expected to know how to use all of these tools and modules as you engage in this exercise. The important part is that you know where to look to begin figuring it out. Remember the objective is to use the profiling tools rather than rushing in to just fix the code because you can visually see why it's broken.

## Part A
The code runs as-is, out of the box &mdash; but not well. As part of its "batteries included" philosophy, Python has a module named `timeit` that allows rudimentary timing of small code snippets. Please refresh your knowledge of the `timeit` module.
 - Python Docs - [timeit](https://docs.python.org/3/library/timeit.html#module-timeit)

For the first part of this assignment, use timeit to measure the total amount of CPU time required to run the `main()` function of the program before you modify it. Use the `timeit` module within your code as opposed to the command line version. You will need to `import timeit` to do this. When profiling a function using `timeit`, the best practice is to take the "minimum of the average" of several measurements of execution time.
 - The `timeit()` method returns a floating point number that represents the TOTAL number of CPU seconds consumed over multiple runs of your function.
 - If you set `number=10` when using `timeit()`, you'll need to divide your resulting cumulative time reading by 10. This is an average, by definition.
 - If you set `repeat=3` when using `timeit`, you will get a list of 3 resulting cumulative time readings.

The timeit interface can be a bit confusing to use from within a program, so here are some tips.
 - Create a `timeit.Timer()` object and assign it the name `t`. You'll need to set the `stmt=` and `setup=` parameters when creating `t`.
 - Using your `t` object, call its `repeat()` method and supply the `repeat=` and `number=` parameters. For example, `result = t.repeat(repeat=7, number=3)`
 - `result` will be a list of 7 floating point numbers. Each float represents the cumulative time required to run the function 3 times.
 - To condense into a single numerical result, compute the average of each group of three, and take the minimum of those 7 averages.

There is a reason for using the minimum of the averages. The fastest time represents the best an algorithm can perform when the caches are loaded and the system isn't busy with other tasks (e.g. Garbage Collection). All the timings are "*noisy*" &mdash; the fastest time is the least noisy. It is easy to show that the fastest timings are the most reproducible and, therefore, the most useful when timing different implementations of an algorithm.

Your timing measurement should have an output message something like this:
```
Best time across 7 repeats of 5 runs per repeat: 1.85500779152 sec
```

## Part B
Complete the missing decorator function to create a profiler which can be used to "decorate" any function and profile its CPU performance to expose bottlenecks.
 - Create a `cProfile()` object inside the decorator's inner function
 - Enable the `cProfile()` object to start its timers
 - Invoke the original function, passing all args and kwargs to the original function
 - Disable the `cProfile()` object after the original function returns
 - Use the `pstats` module to create a `Stats` object which will collect statistics from the `cProfile` object
 - Sort the stats by 'cumulative' time so you can see which functions are costing the most time
 - Use the `Stats` object's `print_stats()` method to print the statistics


## Part C
Once you are satisfied with your decorator, apply it to the `find_duplicate_movies()` function to see where the most time is being spent. Edit all of the provided functions to reduce the overall time cost of the algorithm.

Here are some expected timing results from before and after improving the `find_duplicate_movies()` function.

BEFORE
```
Reading file: movies.txt
         6808570 function calls in 2.690 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002    2.690    2.690 tuneup.py:44(find_duplicate_movies)
```
AFTER
```
Reading file: movies.txt
         2618 function calls in 0.004 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.004    0.004 tuneup.py:55(find_duplicate_movies_improved)
```

You should be able to achieve at least a 670x improvement in the performance of `find_duplicate_movies()`.


## Submitting your work
To submit your solution for grading, you will need to create a github [Pull Request (PR)](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).  Refer to the `PR Workflow` article in your course content for details.