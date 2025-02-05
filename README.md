# Uncommon Python Bug: ZeroDivisionError in Average Calculation

This repository demonstrates a subtle bug in a Python function that calculates the average of a list of numbers.  The function correctly handles the case of an empty list; however, an alternative implementation would be to explicitly check for an empty list and return zero or raise an exception.

The `bug.py` file contains the buggy code, and `bugSolution.py` provides a corrected version.

## Bug Description

The original code handles the case where the input list `numbers` is empty by returning 0. This is a reasonable approach. However, if an empty list was not considered this would raise a `ZeroDivisionError` exception. While this is a common error when not accounting for empty lists, the code is written to avoid this.