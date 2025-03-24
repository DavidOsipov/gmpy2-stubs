# gmpy2-stubs

[![PyPI version](https://badge.fury.io/py/gmpy2-stubs.svg?icon=si%3Apython&icon_color=%23ffffff)](https://badge.fury.io/py/gmpy2-stubs)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Type stubs for the [gmpy2](https://pypi.org/project/gmpy2/) library (version 2.2.1).

gmpy2 is a C-coded Python extension module that supports multiple-precision arithmetic. It provides access to the GMP (GNU Multiple Precision Arithmetic Library), MPFR (Multiple-Precision Floating-Point Reliable Library), and MPC (Multiple-Precision Complex Library) libraries. gmpy2 itself does *not* include type hints. This package provides them.

## Installation

```bash
pip install gmpy2-stubs
```

or, if you'd like to use a specific version:

```bash
pip install gmpy2-stubs==2.2.1.0
```

## Usage

These stubs are automatically used by static type checkers like [mypy](https://mypy-lang.org/) and [pyright](https://github.com/microsoft/pyright) when you have both `gmpy2` and `gmpy2-stubs` installed. You do *not* need to import anything from `gmpy2-stubs` directly.

```python
import gmpy2

# Type hints are available here!
x = gmpy2.mpz(123)
y = gmpy2.sqrt(x)
print(y)
```

## Limitations: `inspect.signature()`

It's important to understand that these stubs are designed for *static* type checking.  They will *not* affect the behavior of runtime introspection tools like `inspect.signature()`.

gmpy2, like many C extension modules, does not provide complete runtime signature information.  The standard library's `inspect.signature()` function relies on information that is usually available for pure Python functions (like docstrings and argument annotations) but is often missing or incomplete for C extensions.

There have been discussions about improving this situation, including:

*   **gmpy2 issue #496:** [Type declarations to allow integration with type checking and linting tools](https://github.com/aleaxit/gmpy/issues/496) - Discusses the general problem and potential solutions (including this stub package!).
*   **CPython issue #121945:** [Use *.pyi stub files as source for the inspect.signature()](https://github.com/python/cpython/issues/121945) - A proposal to make `inspect.signature()` use stub files as a fallback, but this was **closed as not planned**.

Therefore, if you use `inspect.signature()` on gmpy2 functions, you will likely get a generic signature (e.g., `(*args, **kwargs)`) rather than a detailed one.  This is a limitation of the current Python introspection mechanisms, *not* a limitation of these stubs.  The stubs *will* provide full type information to static type checkers.

## Contributing

Contributions and improvements to these stubs are very welcome!  Please submit pull requests or open issues on the [GitHub repository](<YOUR GITHUB REPO URL HERE>).

## License

These stubs are licensed under the MIT License (see the `LICENSE` file). gmpy2 itself is licensed under the LGPLv3+ license.

## Author

David Osipov (personal@david-osipov.vision)

*   ISNI: [0000 0005 1802 960X](https://isni.org/isni/000000051802960X)
*   ORCID: [0009-0005-2713-9242](https://orcid.org/0009-0005-2713-9242)
*   PGP key: [https://openpgpkey.david-osipov.vision/.well-known/openpgpkey/david-osipov.vision/D3FC4983E500AC3F7F136EB80E55C4A47454E82E.asc](https://openpgpkey.david-osipov.vision/.well-known/openpgpkey/david-osipov.vision/D3FC4983E500AC3F7F136EB80E55C4A47454E82E.asc)
*   PGP fingerprint: D3FC 4983 E500 AC3F 7F13 6EB8 0E55 C4A4 7454 E82E
*   Website: [https://david-osipov.vision](https://david-osipov.vision)
*   LinkedIn: [https://www.linkedin.com/in/david-osipov/](https://www.linkedin.com/in/david-osipov/)

## Acknowledgements

Thanks to the gmpy2 developers for creating this powerful library!
