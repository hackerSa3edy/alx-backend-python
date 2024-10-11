# Project: 0x00. Python - Variable Annotations

## Overview

This project focuses on Python's type annotations, which allow you to specify the expected data types of variables and function return values. Type annotations help improve code readability and maintainability, and they can also be used with tools like MyPy to perform static type checking.

## Resources

### Read or Watch

- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Learning Objectives

### General

- Understand type annotations in Python 3.
- Learn how to use type annotations to specify function signatures and variable types.
- Understand the concept of duck typing.
- Learn how to validate your code with `mypy`.

## Project Structure

The project consists of several tasks, each focusing on different aspects of type annotations. Below is a list of tasks and their corresponding files:

| Task                                             | File                                                     |
| ------------------------------------------------ | -------------------------------------------------------- |
| 0. Basic annotations - add                       | [0-add.py](./0-add.py)                                   |
| 1. Basic annotations - concat                    | [1-concat.py](./1-concat.py)                             |
| 2. Basic annotations - floor                     | [2-floor.py](./2-floor.py)                               |
| 3. Basic annotations - to string                 | [3-to_str.py](./3-to_str.py)                             |
| 4. Define variables                              | [4-define_variables.py](./4-define_variables.py)         |
| 5. Complex types - list of floats                | [5-sum_list.py](./5-sum_list.py)                         |
| 6. Complex types - mixed list                    | [6-sum_mixed_list.py](./6-sum_mixed_list.py)             |
| 7. Complex types - string and int/float to tuple | [7-to_kv.py](./7-to_kv.py)                               |
| 8. Complex types - functions                     | [8-make_multiplier.py](./8-make_multiplier.py)           |
| 9. Let's duck type an iterable object            | [9-element_length.py](./9-element_length.py)             |
| 10. Duck typing - first element of a sequence    | [100-safe_first_element.py](./100-safe_first_element.py) |
| 11. More involved type annotations               | [101-safely_get_value.py](./101-safely_get_value.py)     |
| 12. Type Checking                                | [102-type_checking.py](./102-type_checking.py)           |

## Detailed Task Descriptions

### 0. Basic annotations - add

File: [0-add.py](./0-add.py)

Defines a function `add` that takes two floating-point numbers and returns their sum.

### 1. Basic annotations - concat

File: [1-concat.py](./1-concat.py)

Defines a function `concat` that takes two strings and returns their concatenation.

### 2. Basic annotations - floor

File: [2-floor.py](./2-floor.py)

Defines a function `floor` that takes a floating-point number and returns its floor value as an integer.

### 3. Basic annotations - to string

File: [3-to_str.py](./3-to_str.py)

Defines a function `to_str` that takes a floating-point number and returns its string representation.

### 4. Define variables

File: [4-define_variables.py](./4-define_variables.py)

Defines and annotates several variables with different data types.

### 5. Complex types - list of floats

File: [5-sum_list.py](./5-sum_list.py)

Defines a function `sum_list` that takes a list of floating-point numbers and returns their sum.

### 6. Complex types - mixed list

File: [6-sum_mixed_list.py](./6-sum_mixed_list.py)

Defines a function `sum_mixed_list` that takes a list containing both integers and floating-point numbers and returns their sum as a floating-point number.

### 7. Complex types - string and int/float to tuple

File: [7-to_kv.py](./7-to_kv.py)

Defines a function `to_kv` that takes a string and an integer or float, and returns a tuple where the first element is the string and the second element is the square of the number.

### 8. Complex types - functions

File: [8-make_multiplier.py](./8-make_multiplier.py)

Defines a function `make_multiplier` that takes a float and returns a function that multiplies a float by the given multiplier.

### 9. Let's duck type an iterable object

File: [9-element_length.py](./9-element_length.py)

Defines a function `element_length` that takes an iterable of sequences and returns a list of tuples, each containing a sequence and its length.

### 10. Duck typing - first element of a sequence

File: [100-safe_first_element.py](./100-safe_first_element.py)

Defines a function `safe_first_element` that takes a sequence and returns its first element if it exists, otherwise returns `None`.

### 11. More involved type annotations

File: [101-safely_get_value.py](./101-safely_get_value.py)

Defines a function `safely_get_value` that takes a dictionary, a key, and an optional default value, and returns the value corresponding to the key if it exists, otherwise returns the default value.

### 12. Type Checking

File: [102-type_checking.py](./102-type_checking.py)

Defines a function `zoom_array` that takes a tuple and a factor, and returns a list with elements of the tuple repeated by the given factor.

## Usage

To run the scripts, simply execute them using Python 3. For example:

```sh
python3 0-add.py
```

To perform type checking with MyPy, run:

```sh
mypy <filename>.py
```

## Conclusion

This project provides a comprehensive introduction to type annotations in Python. By completing the tasks, you will gain a solid understanding of how to use type annotations to improve code readability and maintainability, and how to perform static type checking with MyPy.
