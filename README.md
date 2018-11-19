# Tuneup Time
In this project, you will tune up some code that is not performing well.  By "not performing" we mean that it's terribly inefficient at what it is trying to do:  Eliminating duplicate entries in a list of popular movie titles.  Although the code is bad, it's representative of what you might encounter in the Real World (tm).

# NOTE:  PLEASE USE PYTHON3 for this assignment!

## Skills Required
- File and Stream I/O
- String and List slicing and indexing
- Profiling code with timeit and cProfile
- Creating a decorator function   
There is a lot of material wrapped up in this seemingly sparse exercise.  You are not expected to know how to use all of these tools and modules as you engage in this exercise.  The important part is that you know where to look, to begin figuring it out.

## Part A
The code runs as-is, out of the box-- but not well.  As part of its "batteries included" philosophy, Python has a module named `timeit` that allows rudimentary timing of small code snippets.  Please refresh your knowledge of the `timeit` module:
 - Python Docs - [timeit](https://docs.python.org/2/library/timeit.html#module-timeit)
 - Stack Overflow - [How to use timeit](https://stackoverflow.com/questions/8220801/how-to-use-timeit-module)

For the first part of this assignment, use timeit to measure the total amount of CPU time required to run the main function of the program, before you modify it.

## Part B
Complete the missing decorator function to create a profiler which can be used to "decorate" any function and profile it's CPU performance to expose bottlenecks:
 - Creates a cProfile() object inside the decorator
 - Enables the cProfile() object
 - Invokes the original function, passing all args and kwargs to original function
 - Disables the cProfile() object after original function returns
 - Uses the pstats module to collect stats from the cProfile object
 - Sort the stats by 'cumulative' time
 - Use the ps.print_stats() function to send the stats to an IO stream
 - print the IO stream results to the console

## Part C
Once you are satisfied with you decorator, apply it to the `find_duplicate_movies` function to see where the most time is being spent.  Edit all of the provided functions to reduce the overall time cost of the algorithm.


## Workflow for this Assignment
1. Fork this repository into your own personal github account.
2. Then Clone your own repo to your local development machine.
3. Create a separate branch named dev/your-github-username, and checkout the branch.
4. Commit your changes, then git push the branch back to your own github account.
5. From your own Github repo, create a pull request (PR) from your dev branch back to your own master.
6. Copy/Paste the URL link to your PR as your assignment submission.




