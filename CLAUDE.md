# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a personal solutions repository for *Cracking the Coding Interview*. Solutions are written in Python, organized by chapter. Each solution file is standalone and self-executing.

## Running Solutions

Each Python solution file acts as its own test runner. Run any solution directly:

```bash
python coding_solution_python/chapter1/1-is-unique
python coding_solution_python/chapter1/3-URLify.py
```

Note: some files have no `.py` extension (e.g., `1-is-unique`, `2-check-permutation`) — they are still valid Python scripts and run the same way.

There is no test framework, build system, or package manager. No `pip install` needed.

## Solution File Structure

Each solution follows the pattern in `coding_solution_python/solution_template.py`:

1. Docstring with the **Problem** statement
2. Docstring with **Questions** to ask and **Algorithm** analysis (time/space complexity)
3. Implementation function(s)
4. `if __name__ == "__main__":` block with inline test cases that print results or raise `Exception` on failure

## Repository Structure

```
coding_solution_python/
  solution_template.py       # Template for new solutions
  chapter1/                  # Arrays & Strings
    1-is-unique
    2-check-permutation
    3-URLify.py
cracking_coding_interview    # Binary (compiled C++ executable, legacy)
```

The `coding_solution/` C++ project (Visual Studio + Makefile) has been removed from the working tree (tracked as deleted in git) and is no longer active.

## Adding New Solutions

Copy `solution_template.py`, fill in the Problem/Questions/Algorithm docstrings, implement the function, and add test cases in the `__main__` block. Name the file `<number>-<kebab-case-problem-name>.py` (or without extension, matching existing convention).
