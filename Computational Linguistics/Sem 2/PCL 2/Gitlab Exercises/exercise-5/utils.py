import timeit
from typing import Callable, Any, Sequence

import pandas as pd
import seaborn as sns


def plot_time_complexity_sequence(
    func: Callable[[Sequence], Any], input_sequence: Sequence, title=None, ax=None
):
    """
    Plot the time complexity of a given function with respect to the length of the input sequence.

    This function measures the execution time of the provided function for different input sizes and plots the results.
    The input sizes range from 0 to `len(input_sequence)`. The execution time is measured using the `timeit` module.

    Parameters:
    func (Callable[[Sequence], Any]): The function to measure. This function should take a sequence (e.g., a list or string) as its only argument.
    input_sequence (Sequence): The input sequence to the function.

    Returns:
    None
    """
    times = []
    step = len(input_sequence) // 20
    input_sizes = list(range(0, len(input_sequence), step))
    for i in input_sizes:
        t = timeit.timeit(lambda: func(input_sequence[:i]), number=5)
        times.append(t * 1000)

    sns.pointplot(
        x="Input size",
        y="Time in seconds",
        data=pd.DataFrame({"Input size": input_sizes, "Time in seconds": times}),
        ax=ax,
    ).set_title(title)


def plot_time_complexity_int(func: Callable[[int], Any], max_input: int, title=None, ax=None):
    """
    Plot the time complexity of a given function with respect to the input integer.
    (Same as `plot_time_complexity_list`, but the function input is an integer instead of a list.)

    This function measures the execution time of the provided function for different inputs and plots the results.
    The inputs range from 0 to `max_input`. The execution time is measured using the `timeit` module.

    Parameters:
    func (Callable[[int], Any]): The function to measure. This function should take an integer as its only argument.
    max_input (int): The maximum input argument to the function.

    Returns:
    None
    """
    times = []
    step = max(max_input // 20, 1)
    inputs = list(range(0, max_input, step))
    for i in inputs:
        t = timeit.timeit(lambda: func(i), number=5)
        times.append(t * 1000)

    sns.pointplot(
        x="Input number",
        y="Time in seconds",
        data=pd.DataFrame({"Input number": inputs, "Time in seconds": times}),
        ax=ax,
    ).set_title(title)
