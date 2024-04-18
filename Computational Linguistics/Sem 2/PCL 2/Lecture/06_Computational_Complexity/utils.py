import timeit
from collections import Counter

import pandas as pd
import seaborn as sns


def plot_time_complexity(func, input, regression_order=None, **kwargs):
    step = max(len(input) // 50, 1)
    input_sizes = range(0, len(input), step)
    times = []
    for i in input_sizes:
        if "number" not in kwargs:
            kwargs["number"] = 5
        input_i = input[:i]
        t = timeit.timeit(lambda: func(input_i), **kwargs)
        times.append(t)
    if regression_order is None:
        sns.pointplot(
            x="Input size",
            y="Time in seconds",
            data=pd.DataFrame({"Input size": input_sizes, "Time in seconds": times}),
            linestyle="none",
        )
    else:
        sns.lmplot(
            x="Input size",
            y="Time in seconds",
            data=pd.DataFrame({"Input size": input_sizes, "Time in seconds": times}),
            order=regression_order,
        )


class CallCounter:
    def __init__(self):
        self._counter = Counter()

    def register(self, func):
        func_name = func.__name__

        def wrapper(*args, **kwargs):
            arg_repr = [repr(arg) for arg in args]
            kwarg_repr = [f"{key}={value!r}" for key, value in kwargs.items()]
            arglist = ", ".join(arg_repr + kwarg_repr)
            self._counter[f"{func_name}({arglist})"] += 1
            return func(*args, **kwargs)

        return wrapper

    def print_most_common(self, n=None):
        for call, count in self._counter.most_common(n):
            print(count, call, sep="\t")
