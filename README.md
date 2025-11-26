Longest Palindromic Substring — Test Suite (Pytest Lab)

This repository contains a professional-grade automated test suite and implementation for the classic algorithm challenge Longest Palindromic Substring, built using pytest and following Test-Driven Development (TDD) principles.

The purpose of this project is to demonstrate how real-world engineering teams validate algorithms through automated testing before writing implementation code.

# Overview

This project includes:

- A comprehensive pytest test suite written before implementation (TDD)

Tests covering:

- Basic palindrome cases
- Edge cases (empty strings, single chars, no repeating chars)
- Mixed alphanumeric cases
- Stress tests
- Error handling
- A clean and fully passing algorithm implementation in palindrome.py
- A reproducible project environment using Pipenv

The test suite ensures correctness, robustness, and reliability—similar to how coding challenge platforms such as LeetCode, HackerRank, and Codewars validate submissions.

## Purpose of This Project

This lab demonstrates:

- How to design an automated test suite before writing code (TDD)
- How to structure Python projects for test discovery
- How to use pytest effectively
- How to validate edge cases and complex behavior
- How to implement an interview-level algorithm and verify correctness

#### Technologies Used
Technology	    |    Purpose
Python 3.12	    |    Programming language
Pytest 9.x	    |    Testing framework
Pipenv	        |    Dependency & virtual environment management
VSCode / CLI	|    Development environment
TDD Workflow	|    Methodology: write tests before implementation

#### Project Structure
python-pytest-code-challenge-lab/
│
├── lib/
│   ├── palindrome.py              # Algorithm implementation
│   └── testing/
│       └── test_palindrome.py     # Complete pytest test suite
│
├── pytest.ini                     # Configures test discovery + pythonpath
├── Pipfile                        # Environment + dependency definitions
├── Pipfile.lock                   # Locked dependency versions
└── README.md                      # Project documentation (this file)

Key Files

- lib/palindrome.py
-- Contains the implementation for longest_palindromic_substring().

- lib/testing/test_palindrome.py
-- Contains 16+ tests covering all expected behavior.

- pytest.ini
-- Ensures pytest can find modules under lib/.

#### Dependencies

This project uses Pipenv.
Dependencies include:

- Python (3.12 recommended)
- pytest

If Pipenv is not installed:
- pip install pipenv

#### Setup & Installation
1. Clone the Repository
git clone <your-repo-url>
cd python-pytest-code-challenge-lab

2. Install Dependencies with Pipenv
pipenv install
pipenv shell

This:
- Creates a virtual environment
- Installs pytest and all required packages

#### Running the Test Suite

Once inside the Pipenv shell, run:

pytest

Expected output (all tests passing):
- 16 passed in 0.02s

If you want more verbose output:
- pytest -vv


If you want to see print statements or debugging output:
- pytest -s

#### Implementation Behavior Validated by The Tests

The test suite validates:
- Odd-length palindromes ("babad" → "bab" or "aba")
- Even-length palindromes ("cbbd" → "bb")
- Full-string palindromes ("racecar")
- Single-character strings
- Empty strings
- Numeric palindromes ("1234321")
- Mixed alphanumeric palindromes
- Behavior with repeating blocks
- Internal palindromes in larger strings
- Type error handling for non-string inputs

The suite ensures that any valid implementation must handle both standard and edge-case scenarios.

#### Final Notes

This project is a complete demonstration of:
- Writing a professional-grade test suite
- Using TDD for algorithm development
- Managing dependencies with Pipenv
- Running automated tests using pytest
- Structuring a Python project for clarity and reproducibility

Feel free to extend this project with more algorithm challenges, CI/CD integrations, or additional test suites!