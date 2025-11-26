#!/usr/bin/python3

# Author: <Hunter Steele>
# Date: <11/26/25>
# version: 1.1

import pytest
from lib.palindrome import longest_palindromic_substring


# Basic Expected Cases
def test_basic_babad():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]  # either answer is acceptable

def test_basic_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_two_character_non_palindrome():
    # Either "a" or "c" is a valid longest palindrome
    assert longest_palindromic_substring("ac") in ["a", "c"]

def test_full_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

# Edge Cases
def test_empty_string():
    # Depending on how you want to handle this, empty string is valid
    assert longest_palindromic_substring("") == ""

def test_no_repeating_characters():
    # Any single character is valid
    result = longest_palindromic_substring("abcdefg")
    assert result in list("abcdefg")

def test_all_same_character():
    assert longest_palindromic_substring("aaaaaaa") == "aaaaaaa"

def test_two_identical_characters():
    assert longest_palindromic_substring("aa") == "aa"

# Mixed Case / Digits / Alphanumeric
def test_mixed_case():
    # Case-sensitive: "Aa" is NOT a palindrome
    assert longest_palindromic_substring("Aa") in ["A", "a"]

def test_digits_only():
    assert longest_palindromic_substring("1234321") == "1234321"

def test_alphanumeric_mixed():
    assert longest_palindromic_substring("a1bcb1a") == "a1bcb1a"

# Complex / Stress Test Cases
def test_long_string_multiple_palindromes():
    s = "abacdgfdcaba"
    # Longest palindrome is "aba" (at start or end)
    assert longest_palindromic_substring(s) in ["aba"]

def test_large_repeated_pattern():
    s = "abcddcba" * 5
    result = longest_palindromic_substring(s)

    # The entire repeated string IS a palindrome, so both results are correct.
    assert result in ["abcddcba", s]

def test_palindrome_in_middle():
    s = "zzzabccbaqqq"
    assert longest_palindromic_substring(s) == "abccba"

# Error Handling / Type Checking (Optional if using TDD strictly)
def test_non_string_input():
    with pytest.raises(TypeError):
        longest_palindromic_substring(123)
