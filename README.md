# gmpy2-stubs

[![PyPI version](https://badge.fury.io/py/gmpy2-stubs.svg)](https://badge.fury.io/py/gmpy2-stubs)
[![TestPyPI version](https://badge.fury.io/py/gmpy2-stubs.svg?label=testpypi+version)](https://test.pypi.org/project/gmpy2-stubs/)

Type stubs for the [gmpy2](https://pypi.org/project/gmpy2/) library (version 2.2.1).

gmpy2 is a C-coded Python extension module that supports multiple-precision arithmetic.  It provides access to the GMP (GNU Multiple Precision Arithmetic Library), MPFR (Multiple-Precision Floating-Point Reliable Library), and MPC (Multiple-Precision Complex Library) libraries.  gmpy2 itself does *not* include type hints. This package provides them.

## Installation

```bash
pip install gmpy2-stubs
```
or, if you'd like to use a specific version.
```bash
pip install gmpy2-stubs==2.2.1.0
```

## Usage
These stubs are automatically used by mypy and other type checkers when you have both `gmpy2` and `gmpy2-stubs` installed.  You do *not* need to import anything from `gmpy2-stubs` directly.

```python
import gmpy2

# Type hints are available here!
x = gmpy2.mpz(123)
y = gmpy2.sqrt(x)
print(y)

```

## Contributing

Contributions and improvements to these stubs are very welcome!  

## License

These stubs are licensed under the MIT License (see the `LICENSE` file).  gmpy2 itself is licensed under the LGPLv3+ license.

## Author

[David Osipov] (<personal@david-osipov.vision>)

## Acknowledgements

Thanks to the gmpy2 developers for creating this powerful library!
```
