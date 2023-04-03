# -----------------------------------------------------------------------------
# example_integer.py
#
# Author: ChatGPT-4 by OpenAI
# Contributor: Newton Winter
#
# This example file demonstrates the usage of libsais_wrapper.py for
# processing integer sequences. The primary author of the code
# is ChatGPT-4, an AI language model by OpenAI. Newton Winter provided
# the prompts, composition, and minor rearrangements.
# -----------------------------------------------------------------------------
import libsais_wrapper as lw

# Sample input data
T = [2, 1, 3, 0, 1, 2]
A = [0] * len(T)
n = len(T)
fs = 0
threads = 2

# Example 1: libsais64
# Calculate the Suffix Array for the input T
result, A, _ = lw.libsais64(T, A, n, fs, threads=threads)
print("Example 1 - libsais64: Suffix Array:", A)

# Example 2: libsais64_bwt
# Calculate the Burrows-Wheeler Transform for the input T
U = [0] * len(T)
result, U, A, _ = lw.libsais64_bwt(T, U, A, n, fs, threads=threads)
print("Example 2 - libsais64_bwt: Burrows-Wheeler Transform:", U)

# Example 3: libsais64_bwt_aux
# Calculate the auxiliary Burrows-Wheeler Transform for the input T
result, U, A, _ = lw.libsais64_bwt_aux(T, U, A, n, fs, threads=threads)
print("Example 3 - libsais64_bwt_aux: Auxiliary Burrows-Wheeler Transform:", U)

# Example 4: libsais64_unbwt
# Calculate the inverse Burrows-Wheeler Transform for the input T
result, T, _ = lw.libsais64_unbwt(T, U, A, n, fs, threads=threads)
print("Example 4 - libsais64_unbwt: Inverse Burrows-Wheeler Transform:", T)

# Example 5: libsais64_unbwt_aux
# Calculate the auxiliary inverse Burrows-Wheeler Transform for the input T
result, T, _ = lw.libsais64_unbwt_aux(T, U, A, n, fs, threads=threads)
print("Example 5 - libsais64_unbwt_aux: Auxiliary Inverse Burrows-Wheeler Transform:", T)

# Example 6: libsais64_plcp
# Calculate the permuted LCP array for the input T
LCP = [0] * len(T)
result, LCP = lw.libsais64_plcp(T, A, LCP, n, threads=threads)
print("Example 6 - libsais64_plcp: Permuted LCP Array:", LCP)

# Example 7: libsais64_lcp
# Calculate the LCP array for the input T
result, LCP = lw.libsais64_lcp(T, A, LCP, n)
print("Example 7 - libsais64_lcp: LCP Array:", LCP)