# Mechanism Unit Specification

A Mechanism Unit represents one system mechanism.

## Required Sections

- Problem: what problem does it solve?
- Constraints: what limitations exist?
- Design: why this design?
- Mechanism: how does it work internally?
- Evidence: how is it verified?
- Conclusion: stable understanding.

## Additional Metadata

Each unit should include:

- Source references
- Dependencies on other mechanisms
- Verification experiments

## Unit Boundary

One unit should contain one core mechanism and one verification loop.

Examples:

- user/kernel boundary
- system call path
- fork/exec process creation
- virtual memory mapping
