# L6_L7_30 — Vending Machine

Lab 6: Code and Branch Coverage

## About

A small Python module that handles item selection, change-making and purchases for a coin-operated vending machine.

## Files

| File | Description |
|------|-------------|
| `vending_machine.py` | The module under test |
| `test_vending_machine.py` | Starter test file |
| `CodeCoverageTest_30_application.py` | Tests that execute every application statement |
| `BranchCoverageTest_30_application.py` | Tests that cover both outcomes of every decision |
| `LineCoverageReport.png` | Line coverage report screenshot |
| `BranchCoverageReport.png` | Line and branch coverage report screenshot |

## Run the coverage exercises

Install the tools and change to this directory:

```powershell
python -m pip install pytest coverage
cd lab6
```

Measure line coverage using the statement-focused test suite:

```powershell
python -m coverage run --data-file=.coverage.line --source=vending_machine -m pytest CodeCoverageTest_30_application.py
python -m coverage report --data-file=.coverage.line -m
```

Measure line and branch coverage using the branch-focused test suite:

```powershell
python -m coverage run --branch --data-file=.coverage.branch --source=vending_machine -m pytest BranchCoverageTest_30_application.py
python -m coverage report --data-file=.coverage.branch -m
```

The line-focused suite executes every application statement. The branch-focused
suite explicitly measures true and false outcomes, including invalid input,
insufficient credit, unrepresentable change, and successful purchase paths.
Both suites target `vending_machine.py` only. In this small module, the
statement-focused tests also happen to take every decision outcome; the branch
report verifies that rather than assuming full line coverage implies it.
