# Lab 6: Code Coverage and Branch Coverage Analysis

## 1. Overview

This project demonstrates code coverage and branch coverage testing for the Credit Card Rewards application using Python, pytest, and Coverage.py.

The objective is to measure how effectively the test cases exercise the application's statements and decision branches, identify untested paths, and improve test completeness.

## 2. Objectives

- Understand the difference between code coverage and branch coverage.
- Measure statement and branch coverage using Coverage.py.
- Test normal inputs, invalid inputs, boundary values, and alternative decision outcomes.
- Generate terminal reports as evidence of test coverage.
- Maintain separate test files for code coverage and branch coverage.

## 3. Tools and Requirements

- Python 3.12
- pytest
- Coverage.py
- Git and GitHub

Install the required Python packages using:

```cmd
python -m pip install pytest coverage
```

## 4. Project Files

| File | Description |
|---|---|
| `credit_card_rewards.py` | Application being tested |
| `test_credit_card_rewards.py` | Original test file supplied with the repository |
| `CodeCoverageTest_xxxx_application.py` | Additional tests for code coverage |
| `BranchCoverageTest_xxxx_application.py` | Tests targeting decision branches |
| `CodeCoverage.png` | Screenshot showing code coverage results |
| `BranchCoverage.png` | Screenshot showing branch coverage results |
| `README.md` | Original README supplied with the repository |
| `README_LAB6_RESULTS.md` | Documentation of this lab's work and results |

## 5. Experiment 1: Code Coverage Analysis

### Objective

Measure the percentage of executable statements in the application that are executed by the code coverage test cases.

### Test File

`CodeCoverageTest_xxxx_application.py`

### Commands

Run these commands from the `LAB6` directory:

```cmd
coverage erase
coverage run --source=credit_card_rewards -m pytest -q CodeCoverageTest_xxxx_application.py
coverage report -m
```

### Results

| Metric | Result |
|---|---:|
| Test cases passed | 14 |
| Test cases failed | 0 |
| Executable statements | 35 |
| Statements missed | 0 |
| Statement coverage | 100% |

### Analysis

All 14 test cases passed. The coverage report showed that all 35 executable statements in `credit_card_rewards.py` were executed, with zero statements missed.

The resulting statement coverage was 100%, exceeding the minimum 90% coverage target.

### Screenshot

See `CodeCoverage.png` for the terminal output showing the test results and coverage report.

## 6. Experiment 2: Branch Coverage Analysis

### Objective

Measure branch coverage by checking whether alternative outcomes of decision conditions in the application are exercised by tests.

### Test File

`BranchCoverageTest_xxxx_application.py`

### Areas Tested

- Card tier validation and invalid purchase amounts.
- Fuel, dining, travel, and ordinary purchase categories.
- Weekend reward bonuses.
- Late payment fee conditions and balance boundaries.
- Additional fees for payments delayed by more than 30 days.
- Frozen cards, blocked cards, utilisation warnings, and good card status.

### Commands

Run these commands from the `LAB6` directory:

```cmd
coverage erase
coverage run --branch --source=credit_card_rewards -m pytest -q BranchCoverageTest_xxxx_application.py
coverage report -m
```

### Results

| Metric | Result |
|---|---:|
| Test cases passed | 24 |
| Test cases failed | 0 |
| Executable statements | 35 |
| Statements missed | 0 |
| Branch exits | 26 |
| Partially covered branches | 0 |
| Reported coverage | 100% |

### Analysis

All 24 branch coverage test cases passed. The report showed 35 executable statements, zero missed statements, 26 branch exits, and zero partially covered branches.

The reported coverage was 100%, exceeding the minimum 90% target.

Branch coverage provides additional information beyond statement coverage because it checks alternative decision outcomes.

### Screenshot

See `BranchCoverage.png` for the terminal output showing the passing tests and branch coverage report.

## 7. Summary

Both experiments achieved 100% reported coverage.

| Experiment | Tests Passed | Coverage |
|---|---:|---:|
| Code coverage | 14 | 100% |
| Branch coverage | 24 | 100% |

The experiments demonstrate how additional test cases can improve test completeness and how Coverage.py can be used to analyse statement and branch coverage.

## 8. Git Commit History

The following commits record the two required deliverables:

- `d0657ef` — Add code coverage tests and report
- `17b4db0` — Add branch coverage tests and report

The results documentation is maintained separately from the original README supplied with the repository.
