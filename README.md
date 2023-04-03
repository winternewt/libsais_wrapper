# libsais-python-wrapper

This repository contains a Python wrapper for the [libsais](https://github.com/IlyaGrebnov/libsais) C library, a high-performance implementation of the SA-IS linear time suffix array and Burrows-Wheeler transform construction algorithm.

The wrapper allows you to utilize the libsais C library in your Python projects easily, providing functions for various operations like suffix array construction, Burrows-Wheeler transform, inverse Burrows-Wheeler transform, and LCP array construction.

## Contents

- `libsais_wrapper.py`: The Python wrapper for the libsais C library
- `example_integer.py`: Example Python script demonstrating the usage of the wrapper with integer inputs
- `example_strings.py`: Example Python script demonstrating the usage of the wrapper with string and Unicode inputs
- `LICENSE`: License file for the repository
- `README.md`: This readme file

## Prerequisites

To use the libsais-python-wrapper, you need to have the `sais-2.7.1.dll` (or corresponding `.so` or `.dylib` file for Linux and macOS, respectively) from the [libsais](https://github.com/IlyaGrebnov/libsais) repository compiled and available in your system's library search path or in the same directory as your Python script.

## Default Settings

By default, the libsais-python-wrapper is configured to use a single thread. To enable OpenMP parallelization and utilize multiple threads, you need to set the `_USE_OMP` flag to `True` in the `libsais_wrapper.py` file and recompile the libsais C library with OpenMP support. The default number of threads is set to the number of CPU cores available on your system, but you can adjust this value by changing the `_DEFAULT_THREADS` variable in the `libsais_wrapper.py` file.

## Usage

Simply import the `libsais_wrapper.py` module in your Python script and use the provided functions to work with the libsais C library. See the `example_integer.py` and `example_strings.py` files for usage examples and explanations.

## License

This repository is licensed under the MIT License. The libsais C library, which this Python wrapper utilizes, is licensed under the Apache License, Version 2.0. Please see the `LICENSE` file for more information.
