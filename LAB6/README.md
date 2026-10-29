# LAB6 — Code and Branch Coverage Analysis

**Name:** Shivansh Sharma
**SRN:** PES2UG24CS474
**SEC:** H
**Application:** Irrigation Scheduler (`irrigation_scheduler.py`)

## Overview
Measure and improve test coverage of the assigned module using Python's `coverage`
tool, achieving at least 90% **code (line)** coverage and at least 90% **branch**
coverage by writing additional targeted test cases.

## Coverage Highlights
- **Baseline Coverage:** 29% statement coverage, 24% branch coverage.
- **Code Coverage Suite:** **100% statement coverage**, 97% branch coverage.
- **Branch Coverage Suite:** **100% statement coverage**, **100% branch coverage** (0 missing branches, all 28 decision pathways tested).

## Files
| File | Description |
|------|-------------|
| `irrigation_scheduler.py` | Module under test |
| `CodeCoverageTest_PES2UG24CS474_irrigation_scheduler.py` | Line-coverage test cases |
| `BranchCoverageTest_PES2UG24CS474_irrigation_scheduler.py` | Branch-coverage test cases |
| `CodeCoverage_PES2UG24CS474.png` | Line-coverage report screenshot |
| `BranchCoverage_PES2UG24CS474.png` | Branch-coverage report screenshot |
| `PES2UG24CS474_SE_LAB6.pdf` | Full lab report |
| `COVERAGE_REPORT.md` | Detailed coverage analysis report |

## Commands
```bash
pip install coverage pytest

# Code (line) coverage
coverage erase
coverage run -m pytest CodeCoverageTest_irrigation_scheduler.py
coverage report -m

# Branch coverage
coverage erase
coverage run --branch -m pytest BranchCoverageTest_irrigation_scheduler.py
coverage report -m
```

## Results
| Metric | Coverage |
|--------|----------|
| Code (line) coverage | 100% |
| Branch coverage | 100% (28/28 branches) |

Both exceed the 90% requirement.
