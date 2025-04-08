<a id="2.2.1.4"></a>
# [2.2.1.4](https://github.com/DavidOsipov/gmpy2-stubs/releases/tag/2.2.1.4) - 2025-04-08

### Major Changes
1. **Added Changelog Generation Workflow**:
   - Added a new job `generate-changelog` in the GitHub Actions workflow to automatically generate and update `CHANGELOG.md` using the `rhysd/changelog-from-release` action.
   - Ensured `build-n-publish` job depends on the `generate-changelog` job.

2. **Updated Python Version in Configuration**:
   - Updated the Python version in `.vscode/settings.json` and `pyproject.toml` from `3.7` to `3.8`.

3. **Generated `CHANGELOG.md` File**:
   - A new `CHANGELOG.md` file was added to maintain a history of changes for the project.

4. **New Type Definitions and Improvements**:
   - Added `@final` decorator for classes `mpz`, `mpq`, `mpfr`, `mpc`, and `xmpz`.
   - Added several new dunder methods and positional-only markers for various methods to improve type checking accuracy.

### Merged Pull Requests
1. **[Update changelog for 2.2.1.3](https://github.com/DavidOsipov/gmpy2-stubs/pull/19)**: Automatically generated changelog for version 2.2.1.3.
2. **[Update rhysd/changelog-from-release digest to 589c79e](https://github.com/DavidOsipov/gmpy2-stubs/pull/18)**: Updated the `rhysd/changelog-from-release` GitHub Action digest.
3. **[Update rhysd/changelog-from-release digest to 589c79e](https://github.com/DavidOsipov/gmpy2-stubs/pull/17)**: Another update to the `rhysd/changelog-from-release` GitHub Action digest.
4. **[Added iroot and iroot_rem functions](https://github.com/DavidOsipov/gmpy2-stubs/pull/16)**: Added type hints for `gmpy2.iroot` and `gmpy2.iroot_rem` functions.
5. **[Update actions/setup-python digest to 8d9ed9a](https://github.com/DavidOsipov/gmpy2-stubs/pull/15)**: Updated `actions/setup-python` GitHub Action digest.
6. **[Update actions/setup-python digest to 19e4675](https://github.com/DavidOsipov/gmpy2-stubs/pull/14)**: Another update to `actions/setup-python` GitHub Action digest.
7. **[Update dependency python to 3.13](https://github.com/DavidOsipov/gmpy2-stubs/pull/12)**: Updated the Python dependency to version 3.13.
8. **[Update actions/checkout digest to 85e6279](https://github.com/DavidOsipov/gmpy2-stubs/pull/10)**: Updated `actions/checkout` GitHub Action digest.

### Note
There are a total of 16 merged pull requests. The above list includes the most recent ones. To view all merged pull requests, please visit [this link](https://github.com/DavidOsipov/gmpy2-stubs/pulls?q=is%3Apr+is%3Amerged).

If you need a complete list of changes or more details, please refer to the [commit comparison](https://github.com/DavidOsipov/gmpy2-stubs/compare/2.2.1.3...main) or the [pull requests page](https://github.com/DavidOsipov/gmpy2-stubs/pulls).

[Changes][2.2.1.4]


<a id="2.2.1.3"></a>
# [2.2.1.3](https://github.com/DavidOsipov/gmpy2-stubs/releases/tag/2.2.1.3) - 2025-03-30

This is a maintenance release focused on improving the compatibility of `gmpy2-stubs` with the Mypy static type checker. Several specific Mypy errors reported during type checking have been addressed by refining the stub (`.pyi`) file definitions.

These changes do **not** affect the runtime behavior of the `gmpy2` library itself; they only enhance the accuracy and reduce noise during static analysis for developers using these stubs.

## Fixes

*   **Corrected `xmpz` In-place Operator Signatures (`[misc]` error):**
    *   Mypy reported incompatible signatures between in-place operators (`__iadd__`, `__isub__`, `__imul__`) and their standard counterparts (`__add__`, `__sub__`, `__mul__`) within the `xmpz` class.
    *   This difference is intentional: in-place operators modify the mutable `xmpz` object and return `self` (`xmpz`), while standard operators create new objects, potentially promoting the type (e.g., to `mpz` or `mpfr`).
    *   Added `# type: ignore[misc]` to the definitions of `xmpz.__iadd__`, `xmpz.__isub__`, and `xmpz.__imul__` to suppress this Mypy warning, acknowledging the signature difference is correct stub behavior.

*   **Corrected Handling of Overloaded Function Implementation Signatures (`[misc]` error):**
    *   Mypy incorrectly reported errors ("An implementation for an overloaded function is not allowed in a stub file") on the required implementation signatures following `@overload` definitions for several functions/methods. According to PEP 484, stub files *must* include this non-decorated signature ending in `...` after `@overload` blocks.
    *   Affected functions/methods: `xmpz.__getitem__`, `log`, `sin_cos`, and `local_context`.
    *   Added `# type: ignore[misc]` to the implementation signature lines (the ones *without* `@overload` and ending in `...`) for these functions/methods. This suppresses the incorrect Mypy warning while preserving the standard, required structure for overloaded functions in stub files.

These changes ensure a smoother experience when using Mypy for static analysis with projects that depend on `gmpy2` and utilize these type stubs.

[Changes][2.2.1.3]


<a id="2.2.1.2"></a>
# [2.2.1.2](https://github.com/DavidOsipov/gmpy2-stubs/releases/tag/2.2.1.2) - 2025-03-30

This release significantly expands the type hint coverage for `gmpy2` version 2.2.1, adds hints for the experimental `xmpz` type, improves existing signatures, and updates the minimum required Python version.

### ✨ Key Highlights

*   **🐍 Minimum Python Version Increased:** The minimum required Python version is now **3.8+** (previously 3.7+).
*   **🧪 Added `xmpz` Mutable Integer Stubs:** Comprehensive type hints have been added for the experimental `xmpz` mutable integer type, including its methods and dunder implementations.
*   **➕ Added `iroot` and `iroot_rem`:** Type hints for the `gmpy2.iroot` and `gmpy2.iroot_rem` functions have been added (Thanks [@whoami730](https://github.com/whoami730)!).
*   **🏗️ Improved `mpfr` and `mpc` Constructors:** The `__new__` signatures for `mpfr` and `mpc` have been refined using `@overload` to provide much more accurate type checking based on the input arguments (numeric types, strings/bytes, precision, context, base).
*   **📈 Expanded Function/Method Coverage:** Added type hints for a large number of previously missing `gmpy2` functions and methods across `mpz`, `mpq`, `mpfr`, `mpc`, and the top-level module, including:
    *   Many number-theoretic functions (e.g., `is_divisible`, `is_power`, `is_congruent`, `digits` methods for `mpz`/`mpq`).
    *   Additional `context` methods mirroring top-level functions (e.g., `context.log2`, `context.fma`, `context.is_finite`).
    *   More MPFR/MPC specific utility functions (e.g., `to_binary`, `from_binary`, `cmp`, `get_exp`, `inf`, `nan`, `next_above`/`below`, `sign`, `polar`/`rect`, `norm`/`phase`).
    *   Added `rational_division` property and argument to `context`.
    *   Added `is_infinite()` methods to `mpfr`/`mpc` and `context`, marking `is_inf()` as deprecated in docstrings.
*   **🧹 Internal Improvements:**
    *   Consistently used string literals for forward references within class definitions for better compatibility.
    *   Enhanced header documentation and various docstrings for clarity.
    *   Updated the `__all__` list to reflect all additions accurately.

### 💥 Breaking Changes

*   **Python Version:** Requires Python 3.8 or higher. Users on Python 3.7 will need to upgrade Python or stay on `gmpy2-stubs` version 2.2.1.1.

### 🤖 Dependency Updates (from GitHub Auto-Notes)

*   Updated `actions/setup-python` GitHub Action digest to `8d9ed9a` (PR [#15](https://github.com/DavidOsipov/gmpy2-stubs/issues/15) by [@renovate](https://github.com/renovate)). This affects the CI pipeline, not the library code itself.

### 🎉 New Contributors

*   A warm welcome to [@whoami730](https://github.com/whoami730) who made their first contribution in PR [#16](https://github.com/DavidOsipov/gmpy2-stubs/issues/16)!

### Installation / Update

To get the latest version:
```bash
pip install --upgrade gmpy2-stubs
```

**Full Changelog**: https://github.com/DavidOsipov/gmpy2-stubs/compare/2.2.1.1...2.2.1.2

[Changes][2.2.1.2]


<a id="2.2.1.1"></a>
# [2.2.1.1](https://github.com/DavidOsipov/gmpy2-stubs/releases/tag/2.2.1.1) - 2025-03-24

## What's Changed
* Create dependabot.yml by [@DavidOsipov](https://github.com/DavidOsipov) in [#4](https://github.com/DavidOsipov/gmpy2-stubs/pull/4)
* Update README.md by [@DavidOsipov](https://github.com/DavidOsipov) in [#5](https://github.com/DavidOsipov/gmpy2-stubs/pull/5)
* Update README.md by [@DavidOsipov](https://github.com/DavidOsipov) in [#6](https://github.com/DavidOsipov/gmpy2-stubs/pull/6)
* Update README.md by [@DavidOsipov](https://github.com/DavidOsipov) in [#7](https://github.com/DavidOsipov/gmpy2-stubs/pull/7)
* Update README.md by [@DavidOsipov](https://github.com/DavidOsipov) in [#8](https://github.com/DavidOsipov/gmpy2-stubs/pull/8)
* Update actions/checkout digest to 85e6279 by [@renovate](https://github.com/renovate) in [#10](https://github.com/DavidOsipov/gmpy2-stubs/pull/10)
* Update actions/setup-python digest to 19e4675 by [@renovate](https://github.com/renovate) in [#11](https://github.com/DavidOsipov/gmpy2-stubs/pull/11)
* Update dependency python to 3.13 by [@renovate](https://github.com/renovate) in [#12](https://github.com/DavidOsipov/gmpy2-stubs/pull/12)
* Update actions/checkout digest to 85e6279 by [@renovate](https://github.com/renovate) in [#13](https://github.com/DavidOsipov/gmpy2-stubs/pull/13)
* Update actions/setup-python digest to 19e4675 by [@renovate](https://github.com/renovate) in [#14](https://github.com/DavidOsipov/gmpy2-stubs/pull/14)

## New Contributors
* [@DavidOsipov](https://github.com/DavidOsipov) made their first contribution in [#4](https://github.com/DavidOsipov/gmpy2-stubs/pull/4)

**Full Changelog**: https://github.com/DavidOsipov/gmpy2-stubs/compare/2.2.1.0...2.2.1.1

[Changes][2.2.1.1]


<a id="2.2.1.0"></a>
# [2.2.1.0](https://github.com/DavidOsipov/gmpy2-stubs/releases/tag/2.2.1.0) - 2025-03-23

Initial release for gmpy2 version 2.2.1

[Changes][2.2.1.0]


[2.2.1.4]: https://github.com/DavidOsipov/gmpy2-stubs/compare/2.2.1.3...2.2.1.4
[2.2.1.3]: https://github.com/DavidOsipov/gmpy2-stubs/compare/2.2.1.2...2.2.1.3
[2.2.1.2]: https://github.com/DavidOsipov/gmpy2-stubs/compare/2.2.1.1...2.2.1.2
[2.2.1.1]: https://github.com/DavidOsipov/gmpy2-stubs/compare/2.2.1.0...2.2.1.1
[2.2.1.0]: https://github.com/DavidOsipov/gmpy2-stubs/tree/2.2.1.0

<!-- Generated by https://github.com/rhysd/changelog-from-release v3.9.0 -->
