# libsais-python-wrapper

This repository contains a Python wrapper for the [libsais](https://github.com/IlyaGrebnov/libsais) C library, a high-performance implementation of the SA-IS linear time suffix array and Burrows-Wheeler transform construction algorithm.

The wrapper allows you to utilize the libsais C library in your Python projects easily, providing functions for various operations like suffix array construction, Burrows-Wheeler transform, inverse Burrows-Wheeler transform, and LCP array construction.

## Contents

- `libsais_wrapper.py`: The Python wrapper for the libsais C library
- `example_integer.py`: Example Python script demonstrating the usage of the wrapper with integer inputs
- `example_strings.py`: Example Python script demonstrating the usage of the wrapper with string and Unicode inputs
- `LICENSE`: License file for the repository
- `README.md`: This readme file
- `Makefile`: The Makefile compiles the library for Windows, macOS, and Linux platforms with OpenMP. The resulting library will be wrapped by the `libsais_wrapper.py` script.


## Prerequisites and Installation
To use the libsais-python-wrapper, you need to have the `libsais-2.7.1.dll` (or corresponding `.so` or `.dylib` file for Linux and macOS, respectively) from the [libsais](https://github.com/IlyaGrebnov/libsais) repository compiled and available in your system's library search path or in the same directory as your Python script. The repository is included as submodule, to clone the repository including the submodule, run:

```
git clone --recurse-submodules https://github.com/winternewt/libsais_wrapper
```

On macOS and Linux, ensure that you have the necessary build tools (GCC and Make) installed. E.g. for Debian-based. For building on Windows, we recommend using [Chocolatey](https://chocolatey.org/install) to install the required tools:
```cmd
choco install make
```
To compile libsais with OpenMP support use Makefile provided: 
```cmd
make all
```

The compiled library files will have the following names:
Windows: `libsais-2.7.1.dll`
macOS: `libsais-2.7.1.dylib`
Linux: `libsais.so.2`
The libsais_wrapper.py script expects these library names when loading the library on each platform.

## Default Settings

By default, the libsais-python-wrapper is configured to use OpenMP parallelization and utilize multiple threads to boost performance. Importing a library compilled without OpenMP will result in a warning displayed.
To disable OpenMP, you need to set the `_USE_OMP` flag to `False` in the `libsais_wrapper.py` file. Another option is to set `_DEFAULT_THREADS` variable to 1 or manually specify `threads=1` when calling any of the wrapped functions.
It is recommended ot set the default number of threads to the number of CPU cores available on your system, you can adjust this value by changing the `_DEFAULT_THREADS` variable in the `libsais_wrapper.py` file.

## Usage

Simply import the `libsais_wrapper.py` module in your Python script and use the provided functions to work with the libsais C library. See the `example_integer.py` and `example_strings.py` files for usage examples and explanations.

## License

This repository is licensed under the MIT License. The libsais C library, which this Python wrapper utilizes, is licensed under the Apache License, Version 2.0. Please see the `LICENSE` file for more information.
