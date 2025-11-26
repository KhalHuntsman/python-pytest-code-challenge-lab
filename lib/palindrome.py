#!/usr/bin/python3

# Author: <Hunter Steele>
# Date: <11/26/25>
# version: 1.1

def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """

    # --- Type Validation ---
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    n = len(s)

    # Edge case: empty string
    if n == 0:
        return ""

    # Edge case: single character
    if n == 1:
        return s

    start = 0
    max_len = 1

    # Helper: expand around the center
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        # subtract 1 on both sides because the loop over-expanded
        return right - left - 1

    # Try all centers
    for i in range(n):
        # Odd-length palindromes
        len1 = expand_around_center(i, i)
        # Even-length palindromes
        len2 = expand_around_center(i, i + 1)

        current_len = max(len1, len2)

        if current_len > max_len:
            max_len = current_len
            start = i - (current_len - 1) // 2

    return s[start:start + max_len]
