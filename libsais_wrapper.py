#!/bin/python3
# -----------------------------------------------------------------------------
# libsais_wrapper.py
#
# Authors: ChatGPT-4 and ChatGPT-3.5 by OpenAI
# Contributor: Newton Winter
#
# This Python wrapper module provides access to the libsais C library
# functions for constructing suffix arrays, BWT, and LCP arrays. The primary
# authors of the code are ChatGPT-4 and ChatGPT-3.5, AI language models by OpenAI.
# Newton Winter provided the prompts, composition, testing, bugfixes and code rearrangements.
# -----------------------------------------------------------------------------

import ctypes
import os
import sys
from ctypes import c_int64, c_uint8, POINTER
from ctypes.util import find_library

if sys.platform.startswith('win'):  # Windows
    libname = "./libsais-2.7.1.dll"
elif sys.platform.startswith('darwin'):  # macOS
    libname = "./libsais.2.dylib"
elif sys.platform.startswith('linux'):  # Linux
    libname = "./libsais.so.2"
else:
    print("OS not supported")
    sys.exit(1)

# Load the shared library
libsais = ctypes.CDLL(libname)
    
# Set the default number of threads for OMP functions
_DEFAULT_THREADS = 4
# Enable or disable OMP functions
_USE_OMP = False
#we need to test if the library is compiled with OMP first!

__all__ = [
    "libsais64",
    "libsais64_bwt",
    "libsais64_bwt_aux",
    "libsais64_unbwt",
    "libsais64_unbwt_aux",
    "libsais64_plcp",
    "libsais64_lcp"
]

"""
Wrapper for the libsais64 library, which is a library for linear time suffix array, longest common prefix array, and Burrows-Wheeler transform construction. 

Here is a summary of the functions provided by this library:

libsais64: Constructs the suffix array of a given string.
libsais64_omp: Constructs the suffix array of a given string in parallel using OpenMP.
libsais64_bwt: Constructs the Burrows-Wheeler transformed string (BWT) of a given string.
libsais64_bwt_aux: Constructs the Burrows-Wheeler transformed string (BWT) of a given string with auxiliary indexes.
libsais64_bwt_omp: Constructs the Burrows-Wheeler transformed string (BWT) of a given string in parallel using OpenMP.
libsais64_bwt_aux_omp: Constructs the Burrows-Wheeler transformed string (BWT) of a given string with auxiliary indexes in parallel using OpenMP.
libsais64_unbwt: Constructs the original string from a given Burrows-Wheeler transformed string (BWT) with primary index.
libsais64_unbwt_aux: Constructs the original string from a given Burrows-Wheeler transformed string (BWT) with auxiliary indexes.
libsais64_unbwt_omp: Constructs the original string from a given Burrows-Wheeler transformed string (BWT) with primary index in parallel using OpenMP.
libsais64_unbwt_aux_omp: Constructs the original string from a given Burrows-Wheeler transformed string (BWT) with auxiliary indexes in parallel using OpenMP.
libsais64_plcp: Constructs the permuted longest common prefix array (PLCP) of a given string and a suffix array.
libsais64_lcp: Constructs the longest common prefix array (LCP) of a given permuted longest common prefix array (PLCP) and a suffix array.
libsais64_plcp_omp: Constructs the permuted longest common prefix array (PLCP) of a given string and a suffix array in parallel using OpenMP.
libsais64_lcp_omp: Constructs the longest common prefix array (LCP) of a given permuted longest common prefix array (PLCP) and a suffix array in parallel using OpenMP.
"""

# Define the types of the arguments for the exported functions
libsais.libsais64.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.POINTER(ctypes.c_int64)]
libsais.libsais64_bwt.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.POINTER(ctypes.c_int64)]
libsais.libsais64_bwt_aux.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.POINTER(ctypes.c_int64)]
libsais.libsais64_unbwt.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64]
libsais.libsais64_unbwt_aux.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.POINTER(ctypes.c_int64)]
libsais.libsais64_plcp.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64]
libsais.libsais64_lcp.argtypes = [ctypes.POINTER(ctypes.c_int64), ctypes.POINTER(ctypes.c_int64), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64]

# Define the return types of the exported functions
libsais.libsais64.restype = ctypes.c_int64
libsais.libsais64_bwt.restype = ctypes.c_int64
libsais.libsais64_bwt_aux.restype = ctypes.c_int64
libsais.libsais64_unbwt.restype = ctypes.c_int64
libsais.libsais64_unbwt_aux.restype = ctypes.c_int64
libsais.libsais64_plcp.restype = ctypes.c_int64
libsais.libsais64_lcp.restype = ctypes.c_int64

# OMP functions argtypes and restypes

if find_library("libsais64_omp") is not None:
    _USE_OMP = True
    
    # Define the types of the arguments for the exported OMP functions
    libsais.libsais64_omp.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int32]
    libsais.libsais64_bwt_omp.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int32]
    libsais.libsais64_bwt_aux_omp.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int32]
    libsais.libsais64_unbwt_omp.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int32]
    libsais.libsais64_unbwt_aux_omp.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_int32]
    libsais.libsais64_plcp_omp.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_int64), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int32]
    libsais.libsais64_lcp_omp.argtypes = [ctypes.POINTER(ctypes.c_int64), ctypes.POINTER(ctypes.c_int64), ctypes.POINTER(ctypes.c_int64), ctypes.c_int64, ctypes.c_int32]

    # Define the return types of the exported OMP functions
    libsais.libsais64_omp.restype = ctypes.c_int64
    libsais.libsais64_bwt_omp.restype = ctypes.c_int64
    libsais.libsais64_bwt_aux_omp.restype = ctypes.c_int64
    libsais.libsais64_unbwt_omp.restype = ctypes.c_int64
    libsais.libsais64_unbwt_aux_omp.restype = ctypes.c_int64
    libsais.libsais64_plcp_omp.restype = ctypes.c_int64
    libsais.libsais64_lcp_omp.restype = ctypes.c_int64

def libsais64(T, A, n, fs=0, freq=None, threads=_DEFAULT_THREADS):
    """
    Description:
        The libsais64 function is a Python wrapper for the libsais64 and libsais64_omp C functions. 
        It computes the suffix array A of a given input string T of length n, with an optional fs extra allocated space for the suffix array. 
        It also supports frequency counting of the input characters and allows for OpenMP parallelization based on the specified number of threads.

    Arguments:
        T (list of uint8): The input string, represented as a list of 8-bit unsigned integers.
        A (list of int64): The initial suffix array, represented as a list of 64-bit signed integers. The length of this list must be n + fs.
        n (int64): The length of the input string T.
        fs (int64, optional, default=0): The extra allocated space for the suffix array. The suffix array will have a length of n + fs.
        freq (list of int64, optional, default=None): A list of 64-bit signed integers of length 256 to store the frequency of each character in the input string T. If None, the function will not compute the frequency.
        threads (int, optional, default=_DEFAULT_THREADS): The number of threads to be used for OpenMP parallelization. 
        The function will use the libsais64_omp function if _USE_OMP is True and threads > 1. Otherwise, it will use the single-threaded libsais64 function.
        
    Returns:
        result (int): The return value from the underlying libsais64 or libsais64_omp C function. A value of 0 indicates success.
        A (list of int64): The computed suffix array, represented as a list of 64-bit signed integers. The length of this list will be n + fs.
        freq (list of int64 or None): A list of 64-bit signed integers of length 256 with the frequency of each character in the input string T, or None if the freq argument was None.
    """
    
    # Convert Python types to ctypes types
    T_ctypes = (ctypes.c_uint8 * n)(*T)
    A_ctypes = (ctypes.c_int64 * (n + fs))(*A)
    freq_ctypes = None if freq is None else (ctypes.c_int64 * 256)(*freq)
    
    # Call the appropriate function from the C library based on _USE_OMP and the number of threads
    if _USE_OMP and threads > 1:
        result = libsais.libsais64_omp(T_ctypes, A_ctypes, n, fs, freq_ctypes, threads)
    else:
        result = libsais.libsais64(T_ctypes, A_ctypes, n, fs, freq_ctypes)

    # Convert the ctypes arrays back to Python lists
    A = [ctypes.c_int64(a).value for a in A_ctypes]
    freq = None if freq is None else list(freq_ctypes)

    return result, A, freq

def libsais64_bwt(T, U, A, n, fs=0, freq=None, threads=_DEFAULT_THREADS):
    """
    Description:
        The libsais64_bwt function is a Python wrapper for the libsais64_bwt and libsais64_bwt_omp C functions. 
        It computes the Burrows-Wheeler Transform (BWT) U of a given input string T of length n and the corresponding suffix array A, with an optional fs extra allocated space for the suffix array. 
        It also supports frequency counting of the input characters and allows for OpenMP parallelization based on the specified number of threads.

    Arguments:
        T (list of uint8): The input string, represented as a list of 8-bit unsigned integers.
        U (list of uint8): The initial BWT, represented as a list of 8-bit unsigned integers. The length of this list must be n.
        A (list of int64): The initial suffix array, represented as a list of 64-bit signed integers. The length of this list must be n + fs.
        n (int64): The length of the input string T.
        fs (int64, optional, default=0): The extra allocated space for the suffix array. The suffix array will have a length of n + fs.
        freq (list of int64, optional, default=None): A list of 64-bit signed integers of length 256 to store the frequency of each character in the input string T. If None, the function will not compute the frequency.
        threads (int, optional, default=_DEFAULT_THREADS): The number of threads to be used for OpenMP parallelization. 
        The function will use the libsais64_bwt_omp function if _USE_OMP is True and threads > 1. Otherwise, it will use the single-threaded libsais64_bwt function.
    
    Returns:
        result (int): The return value from the underlying libsais64_bwt or libsais64_bwt_omp C function. A value of 0 indicates success.
        U (list of uint8): The computed BWT, represented as a list of 8-bit unsigned integers. The length of this list will be n.
        A (list of int64): The computed suffix array, represented as a list of 64-bit signed integers. The length of this list will be n + fs.
        freq (list of int64 or None): A list of 64-bit signed integers of length 256 with the frequency of each character in the input string T, or None if the freq argument was None.
    """
    
    # Convert Python types to ctypes types
    T_ctypes = (ctypes.c_uint8 * n)(*T)
    U_ctypes = (ctypes.c_uint8 * n)(*U)
    A_ctypes = (ctypes.c_int64 * (n + fs))(*A)
    freq_ctypes = None if freq is None else (ctypes.c_int64 * 256)(*freq)
 
    # Call the appropriate function from the C library based on _USE_OMP and the number of threads
    if _USE_OMP and threads > 1:
        result = libsais.libsais64_bwt_omp(T_ctypes, U_ctypes, A_ctypes, n, fs, freq_ctypes, threads)
    else:
        result = libsais.libsais64_bwt(T_ctypes, U_ctypes, A_ctypes, n, fs, freq_ctypes)

    # Convert the ctypes arrays back to Python lists
    U = list(U_ctypes)
    A = [ctypes.c_int64(a).value for a in A_ctypes]
    freq = None if freq is None else list(freq_ctypes)

    return result, U, A, freq
    
def libsais64_bwt_aux(T, U, A, n, fs=0, freq=None, threads=_DEFAULT_THREADS):
    """
    Description:
        The libsais64_bwt_aux function is a Python wrapper for the libsais64_bwt_aux and libsais64_bwt_aux_omp C functions. It computes the Burrows-Wheeler Transform (BWT) U of a given input string T of length n and the corresponding auxiliary array A, with an optional fs extra allocated space for the auxiliary array. It also supports frequency counting of the input characters and allows for OpenMP parallelization based on the specified number of threads.

    Arguments:
        T (list of uint8): The input string, represented as a list of 8-bit unsigned integers.
        U (list of uint8): The initial BWT, represented as a list of 8-bit unsigned integers. The length of this list must be n.
        A (list of int64): The initial auxiliary array, represented as a list of 64-bit signed integers. The length of this list must be n + fs.
        n (int64): The length of the input string T.
        fs (int64, optional, default=0): The extra allocated space for the auxiliary array. The auxiliary array will have a length of n + fs.
        freq (list of int64, optional, default=None): A list of 64-bit signed integers of length 256 to store the frequency of each character in the input string T. If None, the function will not compute the frequency.
        threads (int, optional, default=_DEFAULT_THREADS): The number of threads to be used for OpenMP parallelization. 
        The function will use the libsais64_bwt_aux_omp function if _USE_OMP is True and threads > 1. Otherwise, it will use the single-threaded libsais64_bwt_aux function.
        
    Returns:
        result (int): The return value from the underlying libsais64_bwt_aux or libsais64_bwt_aux_omp C function. A value of 0 indicates success.
        U (list of uint8): The computed BWT, represented as a list of 8-bit unsigned integers. The length of this list will be n.
        A (list of int64): The computed auxiliary array, represented as a list of 64-bit signed integers. The length of this list will be n + fs.
        freq (list of int64 or None): A list of 64-bit signed integers of length 256 with the frequency of each character in the input string T, or None if the freq argument was None.
    """
    
    # Convert Python types to ctypes types
    T_ctypes = (ctypes.c_uint8 * n)(*T)
    U_ctypes = (ctypes.c_uint8 * n)(*U)
    A_ctypes = (ctypes.c_int64 * (n + fs))(*A)
    freq_ctypes = None if freq is None else (ctypes.c_int64 * 256)(*freq)
    
    # Call the appropriate function from the C library based on _USE_OMP and the number of threads
    if _USE_OMP and threads > 1:
        result = libsais.libsais64_bwt_aux_omp(T_ctypes, U_ctypes, A_ctypes, n, fs, freq_ctypes, threads)
    else:
        result = libsais.libsais64_bwt_aux(T_ctypes, U_ctypes, A_ctypes, n, fs, freq_ctypes)

    # Convert the ctypes arrays back to Python lists
    U = list(U_ctypes)
    A = [ctypes.c_int64(a).value for a in A_ctypes]
    freq = None if freq is None else list(freq_ctypes)

    return result, U, A, freq
    
def libsais64_unbwt(T, U, A, n, fs=0, freq=None, threads=_DEFAULT_THREADS):
    """
    Description:
        The libsais64_unbwt function is a Python wrapper for the libsais64_unbwt and libsais64_unbwt_omp C functions. 
        It computes the inverse Burrows-Wheeler Transform (iBWT) U of a given input string T of length n and the corresponding auxiliary array A, with a specified fs extra allocated space for the auxiliary array. 
        It also supports frequency counting of the input characters and allows for OpenMP parallelization based on the specified number of threads.

    Arguments:
        T (list of int8): The input string, represented as a list of 64-bit signed integers.
        U (list of int8): The initial iBWT, represented as a list of 64-bit signed integers. The length of this list must be n.
        A (list of int64): The initial auxiliary array, represented as a list of 64-bit signed integers. The length of this list must be n + fs.
        n (int64): The length of the input string T.
        fs (int64, optional, default=0): The extra allocated space for the auxiliary array. The auxiliary array will have a length of n + fs.
        freq (list of int64, optional, default=None): A list of 64-bit signed integers of length 256 to store the frequency of each character in the input string T. If None, the function will not compute the frequency.
        threads (int, optional, default=_DEFAULT_THREADS): The number of threads to be used for OpenMP parallelization. 
        The function will use the libsais64_unbwt_omp function if _USE_OMP is True and threads > 1. Otherwise, it will use the single-threaded libsais64_unbwt function.
        
    Returns:
        result (int): The return value from the underlying libsais64_unbwt or libsais64_unbwt_omp C function. A value of 0 indicates success.
        U (list of int64): The computed iBWT, represented as a list of 64-bit signed integers. The length of this list will be n.
        freq (list of int64 or None): A list of 64-bit signed integers of length 256 with the frequency of each character in the input string T, or None if the freq argument was None.
    """
    
    # Convert Python lists to ctypes arrays
    T_ctypes = (ctypes.c_uint8 * n)(*T)
    U_ctypes = (ctypes.c_uint8 * n)(*U)
    A_ctypes = (ctypes.c_int64 * (n + fs))(*A)
    freq_ctypes = None if freq is None else (ctypes.c_int64 * 256)(*freq)

    # Call the appropriate function from the C library based on _USE_OMP and the number of threads
    if _USE_OMP and threads > 1:
        result = libsais.libsais64_unbwt_omp(T_ctypes, U_ctypes, A_ctypes, n, freq_ctypes, fs, threads)
    else:
        result = libsais.libsais64_unbwt(T_ctypes, U_ctypes, A_ctypes, n, freq_ctypes, fs)


    # Convert the ctypes arrays back to Python lists
    T = list(T_ctypes)
    freq = None if freq is None else list(freq_ctypes)

    return result, T, freq

def libsais64_unbwt_aux(T, U, A, n, r, I, fs=0, freq=None, threads=_DEFAULT_THREADS):
    """
    Description:
        The libsais64_unbwt_aux function is a Python wrapper for the libsais64_unbwt_aux and libsais64_unbwt_aux_omp C functions. 
        It computes the inverse Burrows-Wheeler Transform (iBWT) U of a given input string T of length n and the corresponding auxiliary array A, with a specified r sampling rate for auxiliary indexes. 
        This function also reconstructs the input string T from the computed iBWT U. It supports frequency counting of the input characters and allows for OpenMP parallelization based on the specified number of threads.

    Arguments:
        T (list of int8): The input string, represented as a list of 8-bit unsigned integers.
        U (list of int8): The initial iBWT, represented as a list of 8-bit unsigned integers. The length of this list must be n.
        A (list of int64): The initial auxiliary array, represented as a list of 64-bit signed integers. The length of this list must be n + 1.
        n (int64): The length of the input string T.
        r (int64): The sampling rate for auxiliary indexes (must be a power of 2).
        I (list of int64): The input auxiliary indexes, represented as a list of 64-bit signed integers. The length of this list must be (n - 1) // r.
        fs (int64, optional, default=0): The extra allocated space for the auxiliary array. The auxiliary array will have a length of n + fs.
        freq (list of int64, optional, default=None): A list of 64-bit signed integers of length 256 to store the frequency of each character in the input string T. If None, the function will not compute the frequency.
        threads (int, optional, default=_DEFAULT_THREADS): The number of threads to be used for OpenMP parallelization. 
        The function will use the libsais64_unbwt_aux_omp function if _USE_OMP is True and threads > 1. Otherwise, it will use the single-threaded libsais64_unbwt_aux function.

    Returns:
        result (int): The return value from the underlying libsais64_unbwt_aux or libsais64_unbwt_aux_omp C function. A value of 0 indicates success.
        U (list of int8): The computed iBWT, represented as a list of 8-bit unsigned integers. The length of this list will be n.
        freq (list of int64 or None): A list of 64-bit signed integers of length 256 with the frequency of each character in the input string T, or None if the freq argument was None.
    """
    # Convert Python lists to ctypes arrays
    T_ctypes = (ctypes.c_uint8 * n)(*T)
    U_ctypes = (ctypes.c_uint8 * n)(*U)
    A_ctypes = (ctypes.c_int64 * (n + fs))(*A)
    freq_ctypes = None if freq is None else (ctypes.c_int64 * 256)(*freq)
    I_ctypes = (ctypes.c_int64 * len(I))(*I)

      # Call the appropriate function from the C library based on _USE_OMP and the number of threads
    if _USE_OMP and threads > 1:
        result = libsais.libsais64_unbwt_aux_omp(T_ctypes, U_ctypes, A_ctypes, n, freq_ctypes, r, I_ctypes, threads)
    else:
        result = libsais.libsais64_unbwt_aux(T_ctypes, U_ctypes, A_ctypes, n, freq_ctypes, r, I_ctypes)

    # Convert the ctypes arrays back to Python lists
    T = list(T_ctypes)
    freq = None if freq is None else list(freq_ctypes)

    return result, T, freq

def libsais64_plcp(T, A, LCP, n, threads=_DEFAULT_THREADS):
    """
    Description:
        The libsais64_plcp function is a Python wrapper for the libsais64_plcp and libsais64_plcp_omp C functions. 
        It computes the permuted longest common prefix (PLCP) array LCP of a given input string T of length n and the corresponding suffix array A. 
        This function allows for OpenMP parallelization based on the specified number of threads.
        
    Arguments:
        T (list of uint8): The input string, represented as a list of 64-bit signed integers.
        A (list of int64): The suffix array of the input string T, represented as a list of 64-bit signed integers. The length of this list must be n.
        LCP (list of int64): The initial PLCP array, represented as a list of 64-bit signed integers. The length of this list must be n.
        n (int64): The length of the input string T.
        threads (int, optional): The number of threads to use for OpenMP parallelization. Defaults to _DEFAULT_THREADS.
        The function will use the libsais64_plcp_omp if _USE_OMP is True and threads > 1. Otherwise, it will use the single-threaded libsais64_plcp function.
        
    Returns:
        result (int): The return value from the underlying libsais64_plcp or libsais64_plcp_omp C function. A value of 0 indicates success.
        LCP (list of int64): The computed PLCP array, represented as a list of 64-bit signed integers. The length of this list will be n.
    """
    # Convert Python lists to ctypes arrays
    T_ctypes = (ctypes.c_uint8 * n)(*T)
    A_ctypes = (ctypes.c_int64 * n)(*A)
    LCP_ctypes = (ctypes.c_int64 * n)(*LCP)

    # Print ctypes arrays
    #print("T_ctypes:", [T_ctypes[i] for i in range(n)])
    #print("A_ctypes:", [A_ctypes[i] for i in range(n)])
    #print("LCP_ctypes:", [LCP_ctypes[i] for i in range(n)])

    # Call the appropriate function from the C library based on _USE_OMP and the number of threads
    if _USE_OMP and threads > 1:
        result = libsais.libsais64_plcp_omp(T_ctypes, A_ctypes, LCP_ctypes, n, threads)
    else:
        result = libsais.libsais64_plcp(T_ctypes, A_ctypes, LCP_ctypes, n)

    # Convert the ctypes arrays back to Python lists
    LCP = list(LCP_ctypes)

    return result, LCP

def libsais64_lcp(T, A, LCP, n, threads=_DEFAULT_THREADS):
    """
    Description:
        The libsais64_lcp function is a Python wrapper for the libsais64_lcp and libsais64_lcp_omp C functions. 
        It computes the longest common prefix (LCP) array LCP of a given input string T of length n and the corresponding suffix array A. 
        This function allows for OpenMP parallelization based on the specified number of threads.

    Arguments:
        T (list of int64): The input string, represented as a list of 64-bit signed integers.
        A (list of int64): The suffix array of the input string T, represented as a list of 64-bit signed integers. The length of this list must be n.
        LCP (list of int64): The initial LCP array, represented as a list of 64-bit signed integers. The length of this list must be n.
        n (int64): The length of the input string T.
        threads (int, optional): The number of threads to use for OpenMP parallelization. Defaults to _DEFAULT_THREADS. 
        The function will use the libsais64_lcp_omp if _USE_OMP is True and threads > 1. Otherwise, it will use the single-threaded libsais64_lcp function.
    Returns:
        result (int): The return value from the underlying libsais64_lcp or libsais64_lcp_omp C function. A value of 0 indicates success.
        LCP (list of int64): The computed LCP array, represented as a list of 64-bit signed integers. The length of this list will be n.

    """
    # Convert Python lists to ctypes arrays
    T_ctypes = (ctypes.c_int64 * n)(*T)
    A_ctypes = (ctypes.c_int64 * n)(*A)
    LCP_ctypes = (ctypes.c_int64 * n)(*LCP)

    # Print ctypes arrays
    #print("T_ctypes:", [T_ctypes[i] for i in range(n)])
    #print("A_ctypes:", [A_ctypes[i] for i in range(n)])
    #print("LCP_ctypes:", [LCP_ctypes[i] for i in range(n)])

    # Call the appropriate function from the C library based on _USE_OMP and the number of threads
    if _USE_OMP and threads > 1:
        result = libsais.libsais64_lcp_omp(T_ctypes, A_ctypes, LCP_ctypes, n, threads)
    else:
        result = libsais.libsais64_lcp(T_ctypes, A_ctypes, LCP_ctypes, n)

    # Convert the ctypes arrays back to Python lists
    LCP = list(LCP_ctypes)

    return result, LCP

# Check if this module is being run as the main program
if __name__ == '__main__':
    print("This is a service module, not a program.")

