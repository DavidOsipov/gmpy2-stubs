# Security Policy for gmpy2-stubs

## Supported Versions

This `gmpy2-stubs` package provides type hints for `gmpy2` version 2.2.1.  Only the latest version of the stubs corresponding to a supported `gmpy2` version will receive updates.  Since this package *only* contains type stubs and no runtime code, security updates are primarily focused on ensuring the accuracy and completeness of the type hints.

| gmpy2 Version | Stub Version | Supported          |
| ------------- | ------------ | ------------------ |
| 2.2.1         | 2.2.1.x      | :white_check_mark: |
| < 2.2.1       | N/A          | :x:                |

*Note:*  The stub version follows PEP 484, where the `x` in `2.2.1.x` is incremented for updates to the stubs themselves (e.g., fixing a type error, adding a missing function signature).

## Reporting Issues

While traditional security vulnerabilities (like buffer overflows or remote code execution) are not a concern for stub-only packages, there are still important issues to report:

*   **Incorrect Type Hints:** If you find a type hint that is incorrect (e.g., a function signature doesn't match the actual `gmpy2` behavior, a return type is wrong), please report it.  Incorrect type hints can lead to runtime errors that are not caught by type checkers.
*   **Missing Type Hints:** If a public function, class, or constant in `gmpy2` is missing from the stubs, please report it.  Complete stubs are crucial for effective type checking.
*   **Incompatibilities:** If you find that the stubs are incompatible with a particular version of `gmpy2` or a specific type checker (e.g., mypy, pyright), please report it.
*   **Documentation Errors:** Errors in the docstrings within the stub file should also be reported.

**How to Report:**

The best way to report an issue is to open an issue on the GitHub repository:

[https://github.com/DavidOsipov/gmpy2-stubs/issues](https://github.com/DavidOsipov/gmpy2-stubs/issues)

Please include the following information in your report:

1.  **Description of the Issue:** Clearly describe the incorrect or missing type hint, incompatibility, or documentation error.
2.  **gmpy2 Version:**  Specify the exact version of `gmpy2` you are using (e.g., 2.2.1).
3.  **Stub Version:** Specify the version of `gmpy2-stubs` you are using (e.g., 2.2.1.0).
4.  **Python Version:**  Specify your Python version (e.g., 3.9.7).
5.  **Type Checker (if applicable):**  If the issue is specific to a type checker, specify which one (e.g., mypy, pyright) and its version.
6.  **Code Example (if applicable):**  Provide a *minimal* code example that demonstrates the issue.  This is *extremely* helpful for reproducing and fixing the problem.
7.  **Expected Behavior:** Describe what you expect the type checker to do.
8.  **Actual Behavior:** Describe what the type checker actually does.

**What to Expect:**

*   I will acknowledge receipt of your report within a reasonable timeframe (usually within a few days).
*   I will investigate the issue and attempt to correct the stubs.
*   I will release a new version of the `gmpy2-stubs` package with the fix.
*   I will credit you in the release notes (if you wish).

**Important Considerations:**

*   This package contains *only* type stubs; it does *not* contain any executable code. Therefore, traditional security vulnerabilities are not a concern.
*   The accuracy of these stubs depends on the accuracy of the `gmpy2` documentation and my understanding of the library.
*   This is a volunteer effort. While I will strive to address issues promptly, there may be delays.

Thank you for helping to improve the `gmpy2-stubs` package!