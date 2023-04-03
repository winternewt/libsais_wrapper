# -----------------------------------------------------------------------------
# example_strings.py
#
# Author: ChatGPT-4 by OpenAI
# Contributor: Newton Winter
#
# This example file demonstrates the usage of libsais_wrapper.py for
# processing ASCII and Unicode strings. The primary author of the code
# is ChatGPT-4, an AI language model by OpenAI. Newton Winter provided
# the prompts, composition, and minor rearrangements.
# -----------------------------------------------------------------------------

import libsais_wrapper as lw

def string_to_ascii_list(s):
    return [ord(c) for c in s]

def unicode_to_int64_list(u):
    return [c for c in u.encode('utf-32-le')]

# ASCII string input
ascii_str = 'abbrashwabbrakadabbra'
T_ascii = string_to_ascii_list(ascii_str)
A_ascii = [0] * len(T_ascii)
n_ascii = len(T_ascii)

# Unicode string input (emoji)
unicode_str = '😀😁😂😃😄😅😆😀😁😂😃😀😁😂😀😁😃😄😅😆😂😃😄😅😆'
T_unicode = unicode_to_int64_list(unicode_str)
A_unicode = [0] * len(T_unicode)
n_unicode = len(T_unicode)

# Parameters
fs = 0
threads = 2

# ASCII example
result, A_ascii, _ = lw.libsais64(T_ascii, A_ascii, n_ascii, fs, threads=threads)
print("ASCII Example - libsais64: Suffix Array:", A_ascii)

# Unicode example
result, A_unicode, _ = lw.libsais64(T_unicode, A_unicode, n_unicode, fs, threads=threads)
print("Unicode Example - libsais64: Suffix Array:", A_unicode)
