# Copilot Instructions for Algebra

## Project Overview
This is a Python project focused on algebraic operations and symbolic mathematics. The project is in early development with a minimal structure currently containing only `main.py`.

## Architecture & Structure
- **`main.py`**: Entry point and primary module for algebraic operations
- **`README.md`**: Project documentation
- No complex multi-component architecture exists yet—code should be organized within `main.py` or split into logical modules as the project grows

## Code Patterns & Conventions

### Organization
- Keep algebraic operations well-documented with docstrings explaining mathematical concepts
- Use descriptive variable names that reflect mathematical terminology (e.g., `coefficient`, `polynomial`, `equation` rather than generic names)
- Group related algebraic functions together in logical classes or namespaces

### Python Style
- Follow PEP 8 conventions for formatting and naming
- Use type hints for function parameters and return types to improve code clarity
- Include mathematical docstrings with examples of usage

## Development Workflow

### Testing
- No test framework currently established—consider adopting `pytest` for test-driven development
- Tests should validate both mathematical correctness and edge cases (e.g., zero coefficients, negative exponents)

### Running & Debugging
- Execute directly: `python main.py`
- No build process is required; Python files can be run directly

## Dependencies & Integration
- Keep external dependencies minimal—focus on core Python standard library functionality initially
- If algebraic operations require advanced math, consider `sympy` or `numpy` only if their specific capabilities are needed

## Key Considerations
- **Mathematical Accuracy**: Ensure all algebraic operations handle floating-point precision carefully
- **Edge Cases**: Test operations with zero, negative numbers, and special values
- **Extensibility**: Design functions to be easily extended as new algebraic features are added

---

*Last updated: November 29, 2025*
