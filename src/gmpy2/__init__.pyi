"""
Type stubs for gmpy2 - GNU Multiple Precision Arithmetic Library interface (version 2.2.1)

Stub file version: 2.2.1.4

This file provides type hints for the gmpy2 library functions. Initially it was created and used in Post-Quantum Feldman's VSS.

The gmpy2 library is a C-API wrapper around the GMP, MPFR, and MPC multiple-precision
libraries. These type stubs provide Python type hints for better IDE support and type checking
while working with arbitrary-precision arithmetic.

Key Features:

*   **Comprehensive Type Hints:**  Provides type hints for the vast majority of the gmpy2 API, including:
    *   `mpz`, `mpq`, `mpfr`, and `mpc` classes.
    *   `context` and `const_context` managers.
    *   Core arithmetic functions.
    *   Extensive number-theoretic functions.
    *   Random number generators.
    *   Utility functions.
    *   MPFR-specific functions and constants.
    *   Exception types.
*   **Improved Development Experience:**  Enables static type checking with tools like mypy and pyright, leading to:
    *   Earlier detection of type errors.
    *   Better code completion and suggestions in IDEs.
    *   Improved code maintainability.
*   **No Runtime Overhead:**  Because this is a stub-only package, it has *no* impact on the runtime performance of your code.
The stubs are only used during development and type checking.
*   **Version Specificity:** These stubs are specifically designed for gmpy2 version 2.2.1.

Limitations:

*   **`inspect.signature()`:** These stubs are intended for *static* type checking.  They will *not* improve the information
provided by the runtime introspection tool `inspect.signature()`.
This is a limitation of how C extension modules expose their signatures in Python, and is not a limitation of the stubs themselves.
For more details, see [gmpy2 issue #496](https://github.com/aleaxit/gmpy/issues/496) and
[CPython issue #121945](https://github.com/python/cpython/issues/121945).

Usage:

Install the `gmpy2-stubs` package alongside `gmpy2`.  Type checkers will automatically use the stubs.
You do *not* need to import anything from `gmpy2-stubs` directly in your code.

System Requirements:

*   Python 3.8+ (matches gmpy2's requirements)

Repository: https://github.com/DavidOsipov/gmpy2-stubs
PyPI: https://pypi.org/project/gmpy2-stubs/

Developer: David Osipov
    Github Profile: https://github.com/DavidOsipov
    Email: personal@david-osipov.vision
    PGP key: https://openpgpkey.david-osipov.vision/.well-known/openpgpkey/david-osipov.vision/D3FC4983E500AC3F7F136EB80E55C4A47454E82E.asc
    PGP fingerprint: D3FC 4983 E500 AC3F 7F13 6EB8 0E55 C4A4 7454 E82E
    Website: https://david-osipov.vision
    LinkedIn: https://www.linkedin.com/in/david-osipov/
"""

# /// script
# requires-python = ">=3.8"
# ///
# pyright: reportDeprecated=false, reportInvalidTypeForm=false

from types import TracebackType
from typing import Any, Iterator, Optional, Tuple, Type, TypeVar, Union, final, overload

# Type definitions
T = TypeVar("T")
# Removed _mpX_type variable definitions, using string literals directly

# Rounding modes for mpfr
MPFR_RNDN = 0  # Round to nearest, with ties to even
MPFR_RNDZ = 1  # Round toward zero
MPFR_RNDU = 2  # Round toward +Inf
MPFR_RNDD = 3  # Round toward -Inf
MPFR_RNDA = 4  # Round away from zero
MPFR_RNDF = 5  # Round to nearest, with ties to away (faithful rounding)

@final
class mpz:
    """Multiple precision integer type"""

    def __new__(cls, x: Union[int, str, float, "mpz", "mpfr", "mpq", "mpc", bytes] = 0, base: int = 0) -> "mpz": ...
    # No __init__ needed, __new__ handles initialization
    def __str__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __repr__(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __format__(self, format_spec: str) -> str: ...
    def __lt__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __le__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __ge__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __add__(self, other: Union[int, "mpz", "mpfr"]) -> Union["mpz", "mpfr"]: ...
    def __radd__(self, other: Union[int, "mpz", "mpfr"]) -> Union["mpz", "mpfr"]: ...
    def __sub__(self, other: Union[int, "mpz", "mpfr"]) -> Union["mpz", "mpfr"]: ...
    def __rsub__(self, other: Union[int, "mpz", "mpfr"]) -> Union["mpz", "mpfr"]: ...
    def __mul__(self, other: Union[int, "mpz", "mpfr"]) -> Union["mpz", "mpfr"]: ...
    def __rmul__(self, other: Union[int, "mpz", "mpfr"]) -> Union["mpz", "mpfr"]: ...
    def __floordiv__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __rfloordiv__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __truediv__(self, other: Union[int, "mpz", "mpfr"]) -> "mpfr": ...
    def __rtruediv__(self, other: Union[int, "mpz", "mpfr"]) -> "mpfr": ...
    def __divmod__(self, other: Union[int, "mpz"]) -> Tuple["mpz", "mpz"]: ...
    def __rdivmod__(self, other: Union[int, "mpz"]) -> Tuple["mpz", "mpz"]: ...
    def __mod__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __rmod__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __pow__(self, other: Union[int, "mpz"], mod: Optional[Union[int, "mpz"]] = None) -> "mpz": ...
    def __rpow__(self, other: Union[int, "mpz"], mod: Optional[Union[int, "mpz"]] = None) -> "mpz": ...
    def __lshift__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __rlshift__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __rshift__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __rrshift__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __and__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __rand__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __or__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __ror__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __xor__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __rxor__(self, other: Union[int, "mpz"]) -> "mpz": ...
    def __neg__(self) -> "mpz": ...
    def __pos__(self) -> "mpz": ...
    def __abs__(self) -> "mpz": ...
    def __invert__(self) -> "mpz": ...
    def __ceil__(self, /) -> "mpz": ...
    def __floor__(self, /) -> "mpz": ...
    def __round__(self, ndigits: Optional[int] = None, /) -> "mpz": ...
    def __trunc__(self, /) -> "mpz": ...
    def bit_length(self) -> int: ...
    def bit_test(self, n: int, /) -> bool: ...
    def bit_set(self, n: int, /) -> "mpz": ...
    def bit_clear(self, n: int, /) -> "mpz": ...
    def bit_flip(self, n: int, /) -> "mpz": ...
    def bit_scan0(self, starting_bit: int = 0, /) -> Optional[int]: ...
    def bit_scan1(self, starting_bit: int = 0, /) -> Optional[int]: ...
    def bit_count(self) -> int: ...
    def num_digits(self, base: int = 10, /) -> int: ...
    def is_square(self) -> bool: ...
    def is_power(self) -> bool: ...
    def is_prime(self, n: int = 25, /) -> bool: ...
    def is_probab_prime(self, n: int = 25, /) -> int: ...
    def is_congruent(self, other: Union[int, "mpz"], mod: Union[int, "mpz"], /) -> bool: ...
    def is_divisible(self, d: Union[int, "mpz"], /) -> bool: ...
    def is_even(self) -> bool: ...
    def is_odd(self) -> bool: ...
    def to_bytes(self, length: int, byteorder: str, *, signed: bool = False) -> bytes: ...
    @classmethod
    def from_bytes(cls, bytes_val: bytes, byteorder: str, *, signed: bool = False) -> "mpz": ...
    def as_integer_ratio(self) -> Tuple["mpz", "mpz"]: ...
    def conjugate(self) -> "mpz": ...  # Returns self
    def digits(self, base: int = 10, /) -> str: ...
    @property
    def denominator(self) -> "mpz": ...  # Returns 1
    @property
    def imag(self) -> "mpz": ...  # Returns 0
    @property
    def numerator(self) -> "mpz": ...  # Returns self
    @property
    def real(self) -> "mpz": ...  # Returns self

@final
class mpq:
    """Multiple precision rational type"""

    def __new__(cls, num: Union[int, str, float, "mpz", "mpfr", "mpq", bytes] = 0, den: Union[int, "mpz"] = 1) -> "mpq": ...
    # No __init__ needed, __new__ handles initialization
    def __str__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __repr__(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __le__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __ge__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __add__(self, other: Union[int, "mpz", "mpfr", "mpq"]) -> Union["mpq", "mpfr"]: ...
    def __radd__(self, other: Union[int, "mpz", "mpfr", "mpq"]) -> Union["mpq", "mpfr"]: ...
    def __sub__(self, other: Union[int, "mpz", "mpfr", "mpq"]) -> Union["mpq", "mpfr"]: ...
    def __rsub__(self, other: Union[int, "mpz", "mpfr", "mpq"]) -> Union["mpq", "mpfr"]: ...
    def __mul__(self, other: Union[int, "mpz", "mpfr", "mpq"]) -> Union["mpq", "mpfr"]: ...
    def __rmul__(self, other: Union[int, "mpz", "mpfr", "mpq"]) -> Union["mpq", "mpfr"]: ...
    def __truediv__(self, other: Union[int, "mpz", "mpfr", "mpq"]) -> Union["mpq", "mpfr"]: ...
    def __rtruediv__(self, other: Union[int, "mpz", "mpfr", "mpq"]) -> Union["mpq", "mpfr"]: ...
    def __neg__(self) -> "mpq": ...
    def __pos__(self) -> "mpq": ...
    def __abs__(self) -> "mpq": ...
    def __ceil__(self, /) -> "mpq": ...
    def __floor__(self, /) -> "mpq": ...
    def __round__(self, ndigits: Optional[int] = None, /) -> "mpq": ...
    def __trunc__(self, /) -> "mpq": ...
    @property
    def numerator(self) -> "mpz": ...
    @property
    def denominator(self) -> "mpz": ...
    @classmethod
    def from_float(cls, f: float, /) -> "mpq": ...
    @classmethod
    def from_decimal(cls, d: Any, /) -> "mpq": ...  # Assuming 'Any' is a placeholder for 'decimal.Decimal'
    def as_integer_ratio(self) -> Tuple["mpz", "mpz"]: ...
    def conjugate(self) -> "mpq": ...
    def digits(self, base: int = 10, /) -> str: ...
    @property
    def real(self) -> "mpq": ...  # Returns self
    @property
    def imag(self) -> "mpq": ...  # Returns 0

@final
class mpfr:
    """Multiple precision floating-point type (Based on MPFR library)"""

    # Corrected __new__ signature using string literals for forward references
    @overload
    def __new__(cls, n: Union[int, float, "mpz", "mpfr", "mpq", "mpc"] = 0, /, precision: int = 0) -> "mpfr": ...
    @overload
    def __new__(cls, n: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /, precision: int, context: "context") -> "mpfr": ...
    @overload
    def __new__(cls, s: Union[str, bytes], /, precision: int = 0, base: int = 0) -> "mpfr": ...
    @overload
    def __new__(cls, s: Union[str, bytes], /, precision: int, base: int, context: "context") -> "mpfr": ...

    # Implementation signature
    def __new__(  # type: ignore[misc]
        cls,
        x: Union[int, str, float, "mpz", "mpfr", "mpq", "mpc", bytes] = 0,
        precision: int = 0,
        base: int = 0,
        context: Optional["context"] = None,  # Use Optional["context"]
    ) -> "mpfr":
        """
        Return a floating-point number after converting a numeric value n or a string s.
        precision=0 (default) uses the current context's precision.
        base is used for string conversion (0=auto-detect).
        An optional context can be provided.
        """
        ...
    # No __init__ needed, __new__ handles initialization
    def __str__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __repr__(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __format__(self, format_spec: str) -> str: ...
    def __lt__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __le__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __ge__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> bool: ...
    def __add__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr": ...
    def __radd__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr": ...
    def __sub__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr": ...
    def __rsub__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr": ...
    def __mul__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr": ...
    def __rmul__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr": ...
    def __truediv__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr": ...
    def __rtruediv__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr": ...
    def __pow__(self, other: Union[int, float, "mpz", "mpfr", "mpq"], mod: Optional[Union[int, "mpz"]] = None, /) -> "mpfr": ...
    def __rpow__(self, other: Union[int, float, "mpz", "mpfr", "mpq"], mod: Optional[Union[int, "mpz"]] = None, /) -> "mpfr": ...
    def __neg__(self) -> "mpfr": ...
    def __pos__(self) -> "mpfr": ...
    def __abs__(self) -> "mpfr": ...
    def __ceil__(self, /) -> "mpfr": ...
    def __floor__(self, /) -> "mpfr": ...
    def __round__(self, ndigits: Optional[int] = None, /) -> "mpfr": ...
    def __trunc__(self, /) -> "mpfr": ...
    def is_integer(self) -> bool: ...
    def is_zero(self) -> bool: ...
    def is_nan(self) -> bool: ...
    # is_inf is deprecated but present in runtime
    def is_inf(self) -> bool:
        """Checks if x is an Infinity."""
        ...
    def is_infinite(self) -> bool:
        """Return True if x is +Infinity or -Infinity. If x is an mpc, return True if either x.real or x.imag is infinite. Otherwise return
        False."""
        ...
    def is_finite(self) -> bool: ...
    def is_signed(self) -> bool: ...
    def is_regular(self) -> bool: ...
    def digits(self, base: int = 10, prec: int = 0, /) -> Tuple[str, int, int]: ...
    @property
    def precision(self) -> int: ...
    def as_integer_ratio(self) -> Tuple["mpz", "mpz"]: ...
    def as_mantissa_exp(self) -> Tuple["mpz", int]: ...
    def as_simple_fraction(self, precision: int = 0, /) -> "mpq": ...
    def conjugate(self) -> "mpfr": ...  # Returns self
    @property
    def real(self) -> "mpfr": ...  # Returns self
    @property
    def imag(self) -> "mpfr": ...  # Returns 0
    @property
    def rc(self) -> int: ...  # Return code of the last mpfr operation

@final
class mpc:
    """Multi-precision complex number type (Based on MPC library)"""

    # Corrected __new__ signature using string literals
    @overload
    def __new__(
        cls, c: Union[int, float, complex, "mpz", "mpfr", "mpq", "mpc"] = 0, /, precision: Union[int, Tuple[int, int]] = 0
    ) -> "mpc": ...
    @overload
    def __new__(
        cls, c: Union[int, float, complex, "mpz", "mpfr", "mpq", "mpc"], /, precision: Union[int, Tuple[int, int]], context: "context"
    ) -> "mpc": ...
    @overload
    def __new__(
        cls,
        real: Union[int, float, "mpz", "mpfr", "mpq"],
        imag: Union[int, float, "mpz", "mpfr", "mpq"] = 0,
        /,
        precision: Union[int, Tuple[int, int]] = 0,
    ) -> "mpc": ...
    @overload
    def __new__(
        cls,
        real: Union[int, float, "mpz", "mpfr", "mpq"],
        imag: Union[int, float, "mpz", "mpfr", "mpq"],
        /,
        precision: Union[int, Tuple[int, int]],
        context: "context",
    ) -> "mpc": ...
    @overload
    def __new__(cls, s: Union[str, bytes], /, precision: Union[int, Tuple[int, int]] = 0, base: int = 10) -> "mpc": ...
    @overload
    def __new__(cls, s: Union[str, bytes], /, precision: Union[int, Tuple[int, int]], base: int, context: "context") -> "mpc": ...

    # Implementation signature
    def __new__(  # type: ignore[misc]
        cls,
        real: Union[int, str, float, complex, "mpz", "mpfr", "mpq", "mpc", bytes] = 0,
        imag: Union[int, str, float, "mpz", "mpfr", "mpq", bytes] = 0,
        precision: Union[int, Tuple[int, int]] = 0,
        base: int = 10,
        context: Optional["context"] = None,  # Use Optional["context"]
    ) -> "mpc":
        """
        Return a complex floating-point number.
        Can be constructed from a single complex/numeric value, real/imag parts, or a string.
        precision=0 (default) uses the current context's precision(s).
        base (<=36) is used for string conversion (default 10).
        An optional context can be provided.
        """
        ...
    # No __init__ needed, __new__ handles initialization
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __format__(self, format_spec: str) -> str: ...
    def __lt__(self, other: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> bool: ...
    def __le__(self, other: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> bool: ...
    def __ge__(self, other: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> bool: ...
    def __add__(self, other: Union[int, float, "mpz", "mpc", "mpfr"]) -> "mpc": ...
    def __radd__(self, other: Union[int, float, "mpz", "mpc", "mpfr"]) -> "mpc": ...
    def __sub__(self, other: Union[int, float, "mpz", "mpc", "mpfr"]) -> "mpc": ...
    def __rsub__(self, other: Union[int, float, "mpz", "mpc", "mpfr"]) -> "mpc": ...
    def __mul__(self, other: Union[int, float, "mpz", "mpc", "mpfr"]) -> "mpc": ...
    def __rmul__(self, other: Union[int, float, "mpz", "mpc", "mpfr"]) -> "mpc": ...
    def __truediv__(self, other: Union[int, float, "mpz", "mpc", "mpfr"]) -> "mpc": ...
    def __rtruediv__(self, other: Union[int, float, "mpz", "mpc", "mpfr"]) -> "mpc": ...
    def __pow__(self, other: Union[int, float, "mpz", "mpc", "mpfr"], mod: Optional[Union[int, "mpz"]] = None, /) -> "mpc": ...
    def __rpow__(self, other: Union[int, float, "mpz", "mpc", "mpfr"], mod: Optional[Union[int, "mpz"]] = None, /) -> "mpc": ...
    def __neg__(self) -> "mpc": ...
    def __pos__(self) -> "mpc": ...
    def __abs__(self) -> "mpfr": ...
    def __complex__(self, /) -> complex: ...
    def conjugate(self) -> "mpc": ...
    def digits(self, base: int = 10, prec: int = 0, /) -> Tuple[Tuple[str, int, int], Tuple[str, int, int]]: ...
    @property
    def real(self: "mpc") -> "mpfr": ...
    @property
    def imag(self: "mpc") -> "mpfr": ...
    # phase and norm are module-level functions or context methods, not instance methods
    def is_finite(self) -> bool: ...
    # is_inf is deprecated but present in runtime
    def is_inf(self) -> bool:
        """Checks if x is an Infinity."""
        ...
    def is_infinite(self) -> bool:
        """Return True if x is +Infinity or -Infinity. If x is an mpc, return True if either x.real or x.imag is infinite.
        Otherwise return False."""
        ...
    def is_nan(self) -> bool: ...
    def is_zero(self) -> bool: ...
    @property
    def precision(self) -> Tuple[int, int]: ...  # Precision for real and imag parts
    @property
    def rc(self) -> Tuple[int, int]: ...  # Return codes for real and imag parts

@final
class xmpz:
    """Mutable multiple precision integer type (EXPERIMENTAL).

    Instances of xmpz are mutable and cannot be used as dictionary keys.
    In-place operations (+=, //=, etc.) modify the object directly.
    """

    limb_size: int = 8

    def __new__(cls, x: Union[int, str, float, "mpz", "mpfr", "mpq", "mpc", bytes, "xmpz"] = 0, base: int = 0) -> "xmpz": ...

    # --- Dunder Methods ---
    def __str__(self) -> str: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __repr__(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __format__(self, format_spec: str) -> str: ...

    # Comparison
    def __lt__(self, other: Union[int, float, "mpz", "mpfr", "mpq", "xmpz"]) -> bool: ...
    def __le__(self, other: Union[int, float, "mpz", "mpfr", "mpq", "xmpz"]) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: Union[int, float, "mpz", "mpfr", "mpq", "xmpz"]) -> bool: ...
    def __ge__(self, other: Union[int, float, "mpz", "mpfr", "mpq", "xmpz"]) -> bool: ...

    # Arithmetic (Standard) - Assume they return new mpz/mpfr for mixed ops
    def __add__(self, other: Union[int, "mpz", "mpfr", "xmpz"]) -> Union["mpz", "mpfr"]: ...
    def __radd__(self, other: Union[int, "mpz", "mpfr", "xmpz"]) -> Union["mpz", "mpfr"]: ...
    def __sub__(self, other: Union[int, "mpz", "mpfr", "xmpz"]) -> Union["mpz", "mpfr"]: ...
    def __rsub__(self, other: Union[int, "mpz", "mpfr", "xmpz"]) -> Union["mpz", "mpfr"]: ...
    def __mul__(self, other: Union[int, "mpz", "mpfr", "xmpz"]) -> Union["mpz", "mpfr"]: ...
    def __rmul__(self, other: Union[int, "mpz", "mpfr", "xmpz"]) -> Union["mpz", "mpfr"]: ...
    def __floordiv__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __rfloordiv__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __truediv__(self, other: Union[int, "mpz", "mpfr", "xmpz"]) -> "mpfr": ...
    def __rtruediv__(self, other: Union[int, "mpz", "mpfr", "xmpz"]) -> "mpfr": ...
    def __divmod__(self, other: Union[int, "mpz", "xmpz"]) -> Tuple["mpz", "mpz"]: ...
    def __rdivmod__(self, other: Union[int, "mpz", "xmpz"]) -> Tuple["mpz", "mpz"]: ...
    def __mod__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __rmod__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __pow__(self, other: Union[int, "mpz", "xmpz"], mod: Optional[Union[int, "mpz", "xmpz"]] = None) -> "mpz": ...
    def __rpow__(self, other: Union[int, "mpz", "xmpz"], mod: Optional[Union[int, "mpz", "xmpz"]] = None) -> "mpz": ...

    # Arithmetic (In-place) - Modify self
    def __iadd__(self, other: Union[int, "mpz", "xmpz"]) -> "xmpz": ...  # type: ignore[misc]
    def __isub__(self, other: Union[int, "mpz", "xmpz"]) -> "xmpz": ...  # type: ignore[misc]
    def __imul__(self, other: Union[int, "mpz", "xmpz"]) -> "xmpz": ...  # type: ignore[misc]
    def __ifloordiv__(self, other: Union[int, "mpz", "xmpz"]) -> "xmpz": ...
    def __imod__(self, other: Union[int, "mpz", "xmpz"]) -> "xmpz": ...
    def __ipow__(self, other: Union[int, "mpz", "xmpz"], mod: Optional[Union[int, "mpz", "xmpz"]] = None) -> "xmpz": ...

    # Bitwise (Standard)
    def __lshift__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __rlshift__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __rshift__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __rrshift__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __and__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __rand__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __or__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __ror__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __xor__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...
    def __rxor__(self, other: Union[int, "mpz", "xmpz"]) -> "mpz": ...

    # Bitwise (In-place)
    def __ilshift__(self, other: Union[int, "mpz", "xmpz"]) -> "xmpz": ...
    def __irshift__(self, other: Union[int, "mpz", "xmpz"]) -> "xmpz": ...
    def __iand__(self, other: Union[int, "mpz", "xmpz"]) -> "xmpz": ...
    def __ior__(self, other: Union[int, "mpz", "xmpz"]) -> "xmpz": ...
    def __ixor__(self, other: Union[int, "mpz", "xmpz"]) -> "xmpz": ...

    # Unary
    def __neg__(self) -> "mpz": ...
    def __pos__(self) -> "mpz": ...
    def __abs__(self) -> "mpz": ...
    def __invert__(self) -> "mpz": ...

    # Slice access
    @overload
    def __getitem__(self, key: int) -> int: ...
    @overload
    def __getitem__(self, key: slice) -> int: ...
    def __getitem__(self, key: Union[int, slice]) -> int: ...  # type: ignore[misc]
    def __setitem__(self, key: Union[int, slice], value: Union[int, "xmpz"]) -> None: ...

    # Regular Methods
    def bit_clear(self, n: int, /) -> "xmpz": ...
    def bit_count(self) -> int: ...
    def bit_flip(self, n: int, /) -> "xmpz": ...
    def bit_length(self) -> int: ...
    def bit_scan0(self, n: int = 0, /) -> Optional[int]: ...
    def bit_scan1(self, n: int = 0, /) -> Optional[int]: ...
    def bit_set(self, n: int, /) -> "xmpz": ...
    def bit_test(self, n: int, /) -> bool: ...
    def conjugate(self) -> "xmpz": ...
    def copy(self) -> "xmpz": ...
    def digits(self, base: int = 10, /) -> str: ...
    def iter_bits(self, start: int = 0, stop: int = -1) -> Iterator[bool]: ...
    def iter_clear(self, start: int = 0, stop: int = -1) -> Iterator[int]: ...
    def iter_set(self, start: int = 0, stop: int = -1) -> Iterator[int]: ...
    def limbs_finish(self, n: int, /) -> None: ...
    def limbs_modify(self, n: int, /) -> int: ...
    def limbs_read(self) -> int: ...
    def limbs_write(self, n: int, /) -> int: ...
    def make_mpz(self) -> "mpz": ...
    def num_digits(self, base: int = 10, /) -> int: ...
    def num_limbs(self) -> int: ...

    # Properties
    @property
    def denominator(self) -> "mpz": ...
    # imag removed as it's not present at runtime
    @property
    def numerator(self) -> "xmpz": ...
    @property
    def real(self) -> "xmpz": ...

# Exception types
class Gmpy2Error(Exception): ...
class RoundingError(Gmpy2Error): ...
class InexactResultError(RoundingError): ...
class UnderflowResultError(RoundingError): ...
class OverflowResultError(RoundingError): ...
class InvalidOperationError(Gmpy2Error, ValueError): ...  # Inherits from ValueError too
class DivisionByZeroError(Gmpy2Error, ZeroDivisionError): ...
class RangeError(Gmpy2Error): ...

# General functions
def version() -> str:
    """Returns the gmpy2 version as a string."""
    ...

def mp_version() -> str:
    """Returns the GMP/MPIR version as a string."""
    ...

def mpc_version() -> str:
    """Returns the MPC version as a string."""
    ...

def mpfr_version() -> str:
    """Returns the MPFR version as a string."""
    ...

# get_cache and set_cache removed as not present at runtime

def get_max_precision() -> int:
    """Returns the current maximum precision for mpfr operations."""
    ...

# set_max_precision removed as not present at runtime

# get_minprec and get_maxprec removed as not present at runtime

def get_emax_max() -> int:
    """Return the maximum possible exponent that can be set for mpfr."""
    ...

def get_emin_min() -> int:
    """Return the minimum possible exponent that can be set for mpfr."""
    ...

# Context manager for precision control
class context:
    """Context manager for changing precision and rounding modes locally."""

    def __init__(
        self,
        *,
        precision: Optional[int] = None,
        real_prec: Optional[int] = None,
        imag_prec: Optional[int] = None,
        round: Optional[int] = None,
        real_round: Optional[int] = None,
        imag_round: Optional[int] = None,
        subnormalize: Optional[bool] = None,
        trap_underflow: Optional[bool] = None,
        trap_overflow: Optional[bool] = None,
        trap_inexact: Optional[bool] = None,
        trap_invalid: Optional[bool] = None,
        trap_erange: Optional[bool] = None,
        trap_divzero: Optional[bool] = None,
        # trap_expbound removed as not present at runtime
        allow_complex: bool = False,
        allow_release_gil: bool = False,
        rational_division: Optional[bool] = None,
    ) -> None: ...
    def __enter__(self) -> "context": ...
    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]
    ) -> None: ...

    # Context attributes (mirrors instance attributes of mpfr/mpc)
    @property
    def precision(self) -> int:
        """The precision in bits for mpfr operations."""
        ...

    @precision.setter
    def precision(self, value: int) -> None: ...
    @property
    def real_prec(self) -> int:
        """The precision in bits for the real part of mpc operations."""
        ...

    @real_prec.setter
    def real_prec(self, value: int) -> None: ...
    @property
    def imag_prec(self) -> int:
        """The precision in bits for the imaginary part of mpc operations."""
        ...

    @imag_prec.setter
    def imag_prec(self, value: int) -> None: ...
    @property
    def round(self) -> int:
        """The rounding mode for mpfr operations."""
        ...

    @round.setter
    def round(self, value: int) -> None: ...
    @property
    def real_round(self) -> int:
        """The rounding mode for the real part of mpc operations."""
        ...

    @real_round.setter
    def real_round(self, value: int) -> None: ...
    @property
    def imag_round(self) -> int:
        """The rounding mode for the imaginary part of mpc operations."""
        ...

    @imag_round.setter
    def imag_round(self, value: int) -> None: ...
    @property
    def subnormalize(self) -> bool:
        """Enable/disable subnormal number support."""
        ...

    @subnormalize.setter
    def subnormalize(self, value: bool) -> None: ...
    @property
    def trap_underflow(self) -> bool:
        """Trap underflow exceptions."""
        ...

    @trap_underflow.setter
    def trap_underflow(self, value: bool) -> None: ...
    @property
    def trap_overflow(self) -> bool:
        """Trap overflow exceptions."""
        ...

    @trap_overflow.setter
    def trap_overflow(self, value: bool) -> None: ...
    @property
    def trap_inexact(self) -> bool:
        """Trap inexact exceptions."""
        ...

    @trap_inexact.setter
    def trap_inexact(self, value: bool) -> None: ...
    @property
    def trap_invalid(self) -> bool:
        """Trap invalid operation exceptions."""
        ...

    @trap_invalid.setter
    def trap_invalid(self, value: bool) -> None: ...
    @property
    def trap_erange(self) -> bool:
        """Trap range error exceptions."""
        ...

    @trap_erange.setter
    def trap_erange(self, value: bool) -> None: ...
    @property
    def trap_divzero(self) -> bool:
        """Trap division by zero exceptions."""
        ...

    @trap_divzero.setter
    def trap_divzero(self, value: bool) -> None: ...
    # trap_expbound removed
    @property
    def allow_complex(self) -> bool:
        """Allow complex results from real operations."""
        ...

    @allow_complex.setter
    def allow_complex(self, value: bool) -> None: ...
    @property
    def allow_release_gil(self) -> bool:
        """Release the GIL during long computations."""
        ...

    @allow_release_gil.setter
    def allow_release_gil(self, value: bool) -> None: ...
    @property
    def rational_division(self) -> bool:
        """Return mpq instead of mpfr for mpz/mpz if True."""
        ...

    @rational_division.setter
    def rational_division(self, value: bool) -> None: ...

    # Methods to query flags (not settable)
    @property
    def underflow(self) -> bool:
        """Check if underflow occurred."""
        ...

    @property
    def overflow(self) -> bool:
        """Check if overflow occurred."""
        ...

    @property
    def divzero(self) -> bool:
        """Check if division by zero occurred."""
        ...

    @property
    def inexact(self) -> bool:
        """Check if inexact result occurred."""
        ...

    @property
    def invalid(self) -> bool:
        """Check if invalid operation occurred."""
        ...

    @property
    def erange(self) -> bool:
        """Check if range error occurred."""
        ...

    @property
    def emax(self) -> int:
        """Get the maximum exponent value."""
        ...

    @property
    def emin(self) -> int:
        """Get the minimum exponent value."""
        ...

    # Context methods (mirror gmpy2 functions) - Added positional-only markers
    def abs(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpz, mpfr, mpq]:
        """Computes the absolute value of x."""
        ...

    def acos(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the arccosine of x."""
        ...

    def acosh(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the inverse hyperbolic cosine of x."""
        ...

    def add(self, x: Union[int, float, mpz, mpfr, mpq, mpc], y: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes the sum of x and y."""
        ...

    def agm(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the arithmetic-geometric mean of x and y."""
        ...

    def ai(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the Airy function of x."""
        ...

    def asin(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the arcsine of x."""
        ...

    def asinh(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the inverse hyperbolic sine of x."""
        ...

    def atan(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the arctangent of x."""
        ...

    def atan2(self, y: Union[int, float, mpz, mpfr, mpq], x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the two-argument arctangent of y/x."""
        ...

    def atanh(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the inverse hyperbolic tangent of x."""
        ...

    def cbrt(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the cube root of x."""
        ...

    def ceil(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the ceiling of x."""
        ...

    def const_catalan(self) -> "mpfr":
        """Returns Catalan's constant with the context's precision."""
        ...

    def const_euler(self) -> "mpfr":
        """Returns Euler's constant with the context's precision."""
        ...

    def const_log2(self) -> "mpfr":
        """Returns the natural logarithm of 2 with the context's precision."""
        ...

    def const_pi(self) -> "mpfr":
        """Returns the value of pi with the context's precision."""
        ...

    def cos(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the cosine of x."""
        ...

    def cosh(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the hyperbolic cosine of x."""
        ...

    def cot(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the cotangent of x."""
        ...

    def coth(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the hyperbolic cotangent of x."""
        ...

    def csc(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the cosecant of x."""
        ...

    def csch(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the hyperbolic cosecant of x."""
        ...

    def degrees(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Converts angle x from radians to degrees."""
        ...

    def digamma(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the digamma function of x."""
        ...

    def div(self, x: Union[int, float, mpz, mpfr, mpq, mpc], y: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpq, mpfr, mpc]:
        """Computes the division of x by y."""
        ...

    def div_2exp(self, x: Union[int, float, mpz, mpfr, mpq, mpc], n: int, /) -> Union[mpfr, mpc]:
        """Computes x divided by 2^n."""
        ...

    def divmod(self, x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> Tuple["mpz", "mpz"]:
        """Computes the quotient and remainder of x divided by y."""
        ...

    def eint(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the exponential integral of x."""
        ...

    def erf(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the error function of x."""
        ...

    def erfc(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the complementary error function of x."""
        ...

    def exp(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the exponential function e^x."""
        ...

    def exp10(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes 10^x."""
        ...

    def exp2(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes 2^x."""
        ...

    def expm1(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes exp(x) - 1."""
        ...

    def factorial(self, n: Union[int, mpz], /) -> mpfr:
        """Computes the floating-point approximation to the factorial of n."""
        ...

    def floor(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the floor of x."""
        ...

    def floor_div(self, x: Union[int, mpz, mpfr, mpq], y: Union[int, mpz, mpfr, mpq], /) -> Union[mpz, mpfr]:
        """Computes the floor division of x by y."""
        ...

    def fma(
        self,
        x: Union[int, float, mpz, mpfr, mpq, mpc],
        y: Union[int, float, mpz, mpfr, mpq, mpc],
        z: Union[int, float, mpz, mpfr, mpq, mpc],
        /,
    ) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes (x * y) + z with a single rounding."""
        ...

    def fmma(
        self,
        x: Union[int, float, mpz, mpfr, mpq],
        y: Union[int, float, mpz, mpfr, mpq],
        z: Union[int, float, mpz, mpfr, mpq],
        t: Union[int, float, mpz, mpfr, mpq],
        /,
    ) -> mpfr:
        """Computes (x * y) + (z * t) with a single rounding."""
        ...

    def fmms(
        self,
        x: Union[int, float, mpz, mpfr, mpq],
        y: Union[int, float, mpz, mpfr, mpq],
        z: Union[int, float, mpz, mpfr, mpq],
        t: Union[int, float, mpz, mpfr, mpq],
        /,
    ) -> mpfr:
        """Computes (x * y) - (z * t) with a single rounding."""
        ...

    def fmod(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the floating-point remainder of x/y."""
        ...

    def fms(
        self,
        x: Union[int, float, mpz, mpfr, mpq, mpc],
        y: Union[int, float, mpz, mpfr, mpq, mpc],
        z: Union[int, float, mpz, mpfr, mpq, mpc],
        /,
    ) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes (x * y) - z with a single rounding."""
        ...

    def frac(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the fractional part of x."""
        ...

    def frexp(self, x: Union[int, float, mpz, mpfr, mpq], /) -> Tuple[int, mpfr]:
        """Returns the mantissa and exponent of x."""
        ...

    def fsum(self, iterable: Iterator[Union[int, float, mpz, mpfr, mpq]], /) -> mpfr:
        """Computes an accurate sum of the values in the iterable."""
        ...

    def gamma(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the gamma function of x."""
        ...

    def gamma_inc(self, a: Union[int, float, mpz, mpfr, mpq], x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the incomplete gamma function of a and x."""
        ...

    def hypot(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the square root of (x^2 + y^2)."""
        ...

    def j0(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the Bessel function of the first kind of order 0 of x."""
        ...

    def j1(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the Bessel function of the first kind of order 1 of x."""
        ...

    def jn(self, n: int, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the Bessel function of the first kind of order n of x."""
        ...

    def lgamma(self, x: Union[int, float, mpz, mpfr, mpq], /) -> Tuple[mpfr, int]:
        """Computes the logarithm of the absolute value of gamma(x) and the sign of gamma(x)."""
        ...

    def li2(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the real part of the dilogarithm of x."""
        ...

    def lngamma(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the natural logarithm of the absolute value of gamma(x)."""
        ...

    @overload
    def log(self, x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
        """Computes the natural logarithm of x."""
        ...

    @overload
    def log(self, x: Union[int, float, "mpz", "mpfr", "mpq"], base: Union[int, float, "mpz", "mpfr"], /) -> "mpfr":
        """Computes the logarithm of x to the specified base."""
        ...

    def log(  # type: ignore[misc]
        self, x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], base: Optional[Union[int, float, "mpz", "mpfr"]] = None, /
    ) -> Union["mpfr", "mpc"]: ...
    def log10(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the base-10 logarithm of x."""
        ...

    def log1p(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the natural logarithm of (1+x)."""
        ...

    def log2(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the base-2 logarithm of x."""
        ...

    def maxnum(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Returns the maximum of x and y."""
        ...

    def minnum(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Returns the minimum of x and y."""
        ...

    def mod(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the remainder of x/y (using context settings)."""
        ...

    def modf(self, x: Union[int, float, mpz, mpfr, mpq], /) -> Tuple[mpfr, mpfr]:
        """Returns the fractional and integer parts of x."""
        ...

    def mul(self, x: Union[int, float, mpz, mpfr, mpq, mpc], y: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes the product of x and y."""
        ...

    def mul_2exp(self, x: Union[int, float, mpz, mpfr, mpq, mpc], n: int, /) -> Union[mpfr, mpc]:
        """Computes x multiplied by 2^n."""
        ...

    def next_above(self, x: "mpfr", /) -> "mpfr":
        """Returns the next representable floating-point number above x."""
        ...

    def next_below(self, x: "mpfr", /) -> "mpfr":
        """Returns the next representable floating-point number below x."""
        ...

    def next_toward(self, x: "mpfr", y: "mpfr", /) -> "mpfr":
        """Returns the next representable floating-point number from x in the direction of y."""
        ...

    def norm(self, x: "mpc", /) -> "mpfr":
        """Computes the norm of the complex number x."""
        ...

    def phase(self, x: "mpc", /) -> "mpfr":
        """Computes the phase (argument) of the complex number x."""
        ...

    def polar(self, x: "mpc", /) -> Tuple["mpfr", "mpfr"]:
        """Converts a complex number from rectangular to polar coordinates."""
        ...

    def pow(self, x: Union[int, float, mpz, mpfr, mpq, mpc], y: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes x raised to the power of y."""
        ...

    def proj(self, x: "mpc", /) -> "mpc":
        """Computes the projection of a complex number onto the Riemann sphere."""
        ...

    def radians(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Converts angle x from degrees to radians."""
        ...

    def rec_sqrt(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the reciprocal of the square root of x."""
        ...

    def reldiff(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the relative difference between x and y."""
        ...

    def remainder(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the IEEE remainder of x/y."""
        ...

    def remquo(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq], /) -> Tuple[mpfr, int]:
        """Computes the remainder and low bits of the quotient."""
        ...

    def rint(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Rounds x to the nearest integer, using the current rounding mode."""
        ...

    def rint_ceil(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Rounds x to the nearest integer, rounding up."""
        ...

    def rint_floor(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Rounds x to the nearest integer, rounding down."""
        ...

    def rint_round(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Rounds x to the nearest integer, rounding to even for ties."""
        ...

    def rint_trunc(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Rounds x to the nearest integer, rounding towards zero."""
        ...

    def root(self, x: Union[int, float, mpz, mpfr, mpq], n: int, /) -> mpfr:
        """Computes the nth root of x."""
        ...

    def root_of_unity(self, n: int, k: int, /) -> mpc:
        """Computes the (n,k)-th root of unity."""
        ...

    def rootn(self, x: Union[int, float, mpz, mpfr, mpq], n: int, /) -> mpfr:
        """Computes the nth root of x (IEEE 754-2008 compliant)."""
        ...

    def round2(self, x: Union[int, float, mpz, mpfr, mpq], n: int = 0, /) -> mpfr:
        """Rounds x to the nearest multiple of 2^n."""
        ...

    def round_away(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Rounds x to the nearest integer, away from 0 in case of a tie."""
        ...

    def sec(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the secant of x."""
        ...

    def sech(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the hyperbolic secant of x."""
        ...

    def sin(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the sine of x."""
        ...

    def sin_cos(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[Tuple[mpfr, mpfr], Tuple[mpc, mpc]]:
        """Computes the sine and cosine of x."""
        ...

    def sinh(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the hyperbolic sine of x."""
        ...

    def sinh_cosh(self, x: Union[int, float, mpz, mpfr, mpq], /) -> Tuple[mpfr, mpfr]:
        """Computes the hyperbolic sine and cosine of x."""
        ...

    def sqrt(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the square root of x."""
        ...

    def square(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes the square of x."""
        ...

    def sub(self, x: Union[int, float, mpz, mpfr, mpq, mpc], y: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes the difference of x and y."""
        ...

    def tan(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the tangent of x."""
        ...

    def tanh(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpfr, mpc]:
        """Computes the hyperbolic tangent of x."""
        ...

    def trunc(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Truncates x towards zero."""
        ...

    def y0(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the Bessel function of the second kind of order 0 of x."""
        ...

    def y1(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the Bessel function of the second kind of order 1 of x."""
        ...

    def yn(self, n: int, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the Bessel function of the second kind of order n of x."""
        ...

    def zeta(self, x: Union[int, float, mpz, mpfr, mpq], /) -> mpfr:
        """Computes the Riemann zeta function of x."""
        ...

    def clear_flags(self) -> None:
        """Clears all exception flags."""
        ...

    def copy(self) -> "context":
        """Returns a copy of the context."""
        ...

    # These were defined as methods in the original stub, but are module-level functions
    # def ieee(self, size: int, subnormalize: bool = True) -> "context": ...
    # def local_context(self, **kwargs: Any) -> ContextManager["context"]: ...

    def check_range(self, x: Union[int, float, mpz, mpfr, mpq], /) -> "mpfr":
        """Return a new mpfr with exponent within the context's emin/emax range."""
        ...

    def is_finite(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> bool:
        """Checks if x is finite (not NaN or Infinity)."""
        ...

    def is_infinite(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> bool:
        """Checks if x is an Infinity."""
        ...

    def is_integer(self, x: Union[int, float, mpz, mpfr, mpq], /) -> bool:
        """Checks if x is an integer value."""
        ...

    def is_nan(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> bool:
        """Checks if x is Not-A-Number (NaN)."""
        ...

    def is_regular(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> bool:
        """Checks if x is not zero, NaN, or Infinity."""
        ...

    def is_signed(self, x: Union[int, float, mpz, mpfr, mpq], /) -> bool:
        """Checks if the sign bit of x is set."""
        ...

    def is_zero(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> bool:
        """Checks if x is equal to zero."""
        ...

    def minus(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes the negation of x (-x)."""
        ...

    def plus(self, x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes the identity of x (+x)."""
        ...

    def rect(self, r: Union[int, float, mpz, mpfr, mpq], phi: Union[int, float, mpz, mpfr, mpq], /) -> "mpc":
        """Converts polar coordinates (r, phi) to a complex number."""
        ...

class const_context:
    """Context manager for constant creation with specific precision."""

    def __init__(self, precision: int) -> None: ...
    def __enter__(self) -> "const_context": ...
    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]
    ) -> None: ...

# Number theoretic functions - Added positional-only markers
def powmod(x: Union[int, "mpz"], y: Union[int, "mpz"], m: Union[int, "mpz"], /) -> "mpz":
    """Computes (x**y) mod m efficiently."""
    ...

def invert(x: Union[int, "mpz"], m: Union[int, "mpz"], /) -> "mpz":
    """Computes the multiplicative inverse of x modulo m."""
    ...

def is_prime(x: Union[int, "mpz"], n: int = 25, /) -> bool:
    """Performs probabilistic primality test on x."""
    ...

def is_probab_prime(x: Union[int, "mpz"], n: int = 25, /) -> int:
    """Performs probabilistic primality test on x."""
    ...

def gcd(*integers: Union[int, "mpz"]) -> "mpz":
    """Computes the greatest common divisor of integers."""
    ...

def lcm(*integers: Union[int, "mpz"]) -> "mpz":
    """Computes the least common multiple of integers."""
    ...

def gcdext(a: Union[int, "mpz"], b: Union[int, "mpz"], /) -> Tuple["mpz", "mpz", "mpz"]:
    """Computes the extended GCD of a and b."""
    ...

def divm(a: Union[int, "mpz"], b: Union[int, "mpz"], m: Union[int, "mpz"], /) -> "mpz":
    """Computes (a/b) mod m, which is equivalent to (a * invert(b, m)) mod m."""
    ...

def fac(n: Union[int, "mpz"], /) -> "mpz":
    """Computes the factorial of n."""
    ...

def fib(n: Union[int, "mpz"], /) -> "mpz":
    """Computes the nth Fibonacci number F(n)."""
    ...

def fib2(n: Union[int, "mpz"], /) -> Tuple["mpz", "mpz"]:
    """Computes a tuple of Fibonacci numbers (F(n), F(n-1))."""
    ...

def lucas(n: Union[int, "mpz"], /) -> "mpz":
    """Computes the nth Lucas number L(n)."""
    ...

def lucas2(n: Union[int, "mpz"], /) -> Tuple["mpz", "mpz"]:
    """Computes a tuple of Lucas numbers (L(n), L(n-1))."""
    ...

def jacobi(a: Union[int, "mpz"], b: Union[int, "mpz"], /) -> int:
    """Computes the Jacobi symbol (a/b)."""
    ...

def legendre(a: Union[int, "mpz"], p: Union[int, "mpz"], /) -> int:
    """Computes the Legendre symbol (a/p)."""
    ...

def kronecker(a: Union[int, "mpz"], b: Union[int, "mpz"], /) -> int:
    """Computes the Kronecker symbol (a/b)."""
    ...

def next_prime(x: Union[int, "mpz"], /) -> "mpz":
    """Finds the next prime number greater than x."""
    ...

def prev_prime(x: Union[int, "mpz"], /) -> "mpz":
    """Finds the previous prime number less than x."""
    ...

def bincoef(n: Union[int, "mpz"], k: Union[int, "mpz"], /) -> "mpz":
    """Computes the binomial coefficient (n choose k)."""
    ...

def comb(n: Union[int, "mpz"], k: Union[int, "mpz"], /) -> "mpz":
    """Return the number of combinations of n things, taking k at a time'. k >= 0. Same as bincoef(n, k)"""
    ...

def divexact(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> "mpz":
    """Return the quotient of x divided by y. Faster than standard division but requires the remainder is zero!"""
    ...

def double_fac(n: Union[int, "mpz"], /) -> "mpz":
    """Return the exact double factorial (n!!) of n."""
    ...

def f2q(x: "mpfr", err: int = 0, /) -> Union["mpz", "mpq"]:
    """Return the 'best' mpq approximating x to within relative error err."""
    ...

def is_bpsw_prp(n: Union[int, "mpz"], /) -> bool:
    """Return True if n is a Baillie-Pomerance-Selfridge-Wagstaff probable prime."""
    ...

def is_euler_prp(n: Union[int, "mpz"], a: Union[int, "mpz"], /) -> bool:
    """Return True if n is an Euler (also known as Solovay-Strassen) probable prime to the base a."""
    ...

def is_extra_strong_lucas_prp(n: Union[int, "mpz"], p: Union[int, "mpz"], /) -> bool:
    """Return True if n is an extra strong Lucas probable prime with parameters (p,1)."""
    ...

def is_fermat_prp(n: Union[int, "mpz"], a: Union[int, "mpz"], /) -> bool:
    """Return True if n is a Fermat probable prime to the base a."""
    ...

def is_fibonacci_prp(n: Union[int, "mpz"], p: Union[int, "mpz"], q: Union[int, "mpz"], /) -> bool:
    """Return True if n is a Fibonacci probable prime with parameters (p,q)."""
    ...

def is_lucas_prp(n: Union[int, "mpz"], p: Union[int, "mpz"], q: Union[int, "mpz"], /) -> bool:
    """Return True if n is a Lucas probable prime with parameters (p,q)."""
    ...

def is_selfridge_prp(n: Union[int, "mpz"], /) -> bool:
    """Return True if n is a Lucas probable prime with Selfidge parameters (p,q)."""
    ...

def is_strong_bpsw_prp(n: Union[int, "mpz"], /) -> bool:
    """Return True if n is a strong Baillie-Pomerance-Selfridge-Wagstaff probable prime."""
    ...

def is_strong_lucas_prp(n: Union[int, "mpz"], p: Union[int, "mpz"], q: Union[int, "mpz"], /) -> bool:
    """Return True if n is a strong Lucas probable prime with parameters (p,q)."""
    ...

def is_strong_prp(n: Union[int, "mpz"], a: Union[int, "mpz"], /) -> bool:
    """Return True if n is a strong (also known as Miller-Rabin) probable prime to the base a."""
    ...

def is_strong_selfridge_prp(n: Union[int, "mpz"], /) -> bool:
    """Return True if n is a strong Lucas probable prime with Selfidge parameters (p,q)."""
    ...

def lucasu(p: Union[int, "mpz"], q: Union[int, "mpz"], k: Union[int, "mpz"], /) -> "mpz":
    """Return the k-th element of the Lucas U sequence defined by p,q."""
    ...

def lucasu_mod(p: Union[int, "mpz"], q: Union[int, "mpz"], k: Union[int, "mpz"], n: Union[int, "mpz"], /) -> "mpz":
    """Return the k-th element of the Lucas U sequence defined by p,q (mod n)."""
    ...

def lucasv(p: Union[int, "mpz"], q: Union[int, "mpz"], k: Union[int, "mpz"], /) -> "mpz":
    """Return the k-th element of the Lucas V sequence defined by p,q."""
    ...

def lucasv_mod(p: Union[int, "mpz"], q: Union[int, "mpz"], k: Union[int, "mpz"], n: Union[int, "mpz"], /) -> "mpz":
    """Return the k-th element of the Lucas V sequence defined by p,q (mod n)."""
    ...

def multi_fac(n: Union[int, "mpz"], m: Union[int, "mpz"], /) -> "mpz":
    """Return the exact m-multi factorial of n."""
    ...

def pack(lst: list[int], n: int, /) -> "mpz":
    """Pack a list of integers lst into a single mpz."""
    ...

def powmod_base_list(base_lst: list[Union[int, "mpz"]], exp: Union[int, "mpz"], mod: Union[int, "mpz"], /) -> list["mpz"]:
    """Returns list(powmod(i, exp, mod) for i in base_lst)."""
    ...

def powmod_exp_list(base: Union[int, "mpz"], exp_lst: list[Union[int, "mpz"]], mod: Union[int, "mpz"], /) -> list["mpz"]:
    """Returns list(powmod(base, i, mod) for i in exp_lst)."""
    ...

def powmod_sec(x: Union[int, "mpz"], y: Union[int, "mpz"], m: Union[int, "mpz"], /) -> "mpz":
    """Return (x**y) mod m, using a more secure algorithm."""
    ...

def primorial(n: Union[int, "mpz"], /) -> "mpz":
    """Return the product of all positive prime numbers less than or equal to n."""
    ...

def remove(x: Union[int, "mpz"], f: Union[int, "mpz"], /) -> Tuple["mpz", int]:
    """Return a 2-element tuple (y,m) such that x=y*(f**m) and f does not divide y."""
    ...

def unpack(x: Union[int, "mpz"], n: int, /) -> list[int]:
    """Unpack an integer x into a list of n-bit values."""
    ...

# Core arithmetic functions - Added positional-only markers
def add(x: Union[int, "mpz", "mpfr", "mpq", "mpc"], y: Union[int, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpz", "mpfr", "mpq", "mpc"]:
    """Adds two numbers."""
    ...

def sub(x: Union[int, "mpz", "mpfr", "mpq", "mpc"], y: Union[int, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpz", "mpfr", "mpq", "mpc"]:
    """Subtracts y from x."""
    ...

def mul(x: Union[int, "mpz", "mpfr", "mpq", "mpc"], y: Union[int, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpz", "mpfr", "mpq", "mpc"]:
    """Multiplies two numbers."""
    ...

def div(x: Union[int, "mpz", "mpfr", "mpq", "mpc"], y: Union[int, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpq", "mpc"]:
    """Divides x by y."""
    ...

# divmod removed as not present at module level

def mod(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> "mpz":
    """Computes x mod y."""
    ...

def sqrt(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the square root of x."""
    ...

def isqrt(x: Union[int, "mpz"], /) -> "mpz":
    """Computes the integer square root of x (floor of sqrt(x))."""
    ...

def isqrt_rem(x: Union[int, "mpz"], /) -> Tuple["mpz", "mpz"]:
    """Computes the integer square root and remainder of x."""
    ...

def square(x: Union[int, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpz", "mpfr", "mpq", "mpc"]:
    """Computes the square of x."""
    ...

def iroot(x: Union[int, "mpz"], n: Union[int, "mpz"], /) -> Tuple["mpz", bool]:
    """Computes the integer nth root of x (floor of x^(1/n))."""
    ...

def iroot_rem(x: Union[int, "mpz"], n: Union[int, "mpz"], /) -> Tuple["mpz", "mpz"]:
    """Computes the integer nth root and remainder of x."""
    ...

# Random number generators - Added positional-only markers
def random_state(seed: Optional[Union[int, str, bytes, Any]] = None, /) -> Any:
    """Creates a random state object for use with the random number generators."""
    ...

def mpz_random(state: Any, n: Union[int, "mpz"], /) -> "mpz":
    """Generates a uniformly distributed random integer in the range [0, n-1]."""
    ...

def mpz_rrandomb(state: Any, b: int, /) -> "mpz":
    """Generates a random integer with exactly b random bits."""
    ...

def mpz_urandomb(state: Any, b: int, /) -> "mpz":
    """Generates a uniformly distributed random integer in the range [0, 2^b-1]."""
    ...

def mpfr_grandom(state: Any, /) -> Tuple["mpfr", "mpfr"]:
    """Generates two random numbers with gaussian distribution."""
    ...

def mpfr_nrandom(state: Any, /) -> "mpfr":
    """Return a random number with gaussian distribution."""
    ...

def mpfr_random(state: Any, /) -> "mpfr":
    """Return uniformly distributed number between [0,1]."""
    ...

def mpc_random(state: Any, /) -> "mpc":
    """Return uniformly distributed number in the unit square [0,1]x[0,1]."""
    ...

# Other utility functions - Added positional-only markers

def hamdist(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> int:
    """Computes the Hamming distance between x and y."""
    ...

def popcount(x: Union[int, "mpz"], /) -> int:
    """Counts the number of 1-bits in the binary representation of x."""
    ...

def bit_mask(n: int, /) -> "mpz":
    """Creates a bit mask with n 1-bits."""
    ...

def bit_clear(x: Union[int, "mpz"], n: int, /) -> "mpz":
    """Return a copy of x with the n-th bit cleared."""
    ...

def bit_count(x: Union[int, "mpz"], /) -> int:
    """Return the number of 1-bits set in abs(x)."""
    ...

def bit_flip(x: Union[int, "mpz"], n: int, /) -> "mpz":
    """Return a copy of x with the n-th bit inverted."""
    ...

def bit_length(x: Union[int, "mpz"], /) -> int:
    """Return the number of significant bits in the radix-2 representation of x."""
    ...

def bit_scan0(x: Union[int, "mpz"], n: int = 0, /) -> Optional[int]:
    """Return the index of the first 0-bit of x with index >= n."""
    ...

def bit_scan1(x: Union[int, "mpz"], n: int = 0, /) -> Optional[int]:
    """Return the index of the first 1-bit of x with index >= n."""
    ...

def bit_set(x: Union[int, "mpz"], n: int, /) -> "mpz":
    """Return a copy of x with the n-th bit set."""
    ...

def bit_test(x: Union[int, "mpz"], n: int, /) -> bool:
    """Return the value of the n-th bit of x."""
    ...

def num_digits(x: Union[int, "mpz"], base: int = 10, /) -> int:
    """Return length of string representing the absolute value of x in the given base."""
    ...

def is_divisible(x: Union[int, "mpz"], d: Union[int, "mpz"], /) -> bool:
    """Returns True if x is divisible by d, else return False."""
    ...

def is_even(x: Union[int, "mpz"], /) -> bool:
    """Return True if x is even, False otherwise."""
    ...

def is_odd(x: Union[int, "mpz"], /) -> bool:
    """Return True if x is odd, False otherwise."""
    ...

def is_power(x: Union[int, "mpz"], /) -> bool:
    """Return True if x is a perfect power."""
    ...

def is_square(x: Union[int, "mpz"], /) -> bool:
    """Returns True if x is a perfect square."""
    ...

def is_congruent(x: Union[int, "mpz"], y: Union[int, "mpz"], m: Union[int, "mpz"], /) -> bool:
    """Returns True if x is congruent to y modulo m."""
    ...

# MPFR specific functions - Added positional-only markers
def const_log2(precision: int = 0, /) -> "mpfr":
    """Returns the natural logarithm of 2 with specified precision."""
    ...

def const_pi(precision: int = 0, /) -> "mpfr":
    """Returns the value of pi with specified precision."""
    ...

def const_euler(precision: int = 0, /) -> "mpfr":
    """Returns Euler's constant with specified precision."""
    ...

def const_catalan(precision: int = 0, /) -> "mpfr":
    """Returns Catalan's constant with specified precision."""
    ...

# Corrected log signature
@overload
def log(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]: ...
@overload
def log(x: Union[int, float, "mpz", "mpfr", "mpq"], base: Union[int, float, "mpz", "mpfr"], /) -> "mpfr": ...
def log(  # type: ignore[misc]
    x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], base: Optional[Union[int, float, "mpz", "mpfr"]] = None, /
) -> Union["mpfr", "mpc"]: ...
def log10(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the base-10 logarithm of x."""
    ...

def exp(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the exponential function e^x."""
    ...

def sin(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the sine of x."""
    ...

def cos(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the cosine of x."""
    ...

def tan(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the tangent of x."""
    ...

def atan(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the arctangent of x."""
    ...

def atan2(y: Union[int, float, "mpz", "mpfr", "mpq"], x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Computes the two-argument arctangent of y/x."""
    ...

def sinh(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the hyperbolic sine of x."""
    ...

def cosh(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the hyperbolic cosine of x."""
    ...

def tanh(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the hyperbolic tangent of x."""
    ...

def atanh(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the inverse hyperbolic tangent of x."""
    ...

def asin(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the arcsine of x."""
    ...

def acos(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the arccosine of x."""
    ...

def asinh(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the inverse hyperbolic sine of x."""
    ...

def acosh(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"], /) -> Union["mpfr", "mpc"]:
    """Computes the inverse hyperbolic cosine of x."""
    ...

def floor(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Computes the floor of x."""
    ...

def ceil(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Computes the ceiling of x."""
    ...

def trunc(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Truncates x towards zero."""
    ...

def round2(x: Union[int, float, "mpz", "mpfr", "mpq"], n: int = 0, /) -> "mpfr":
    """Rounds x to the nearest multiple of 2^n."""
    ...

def round_away(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Rounds x to the nearest integer, away from 0 in case of a tie."""
    ...

def fmod(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Computes the floating-point remainder of x/y with the same sign as x."""
    ...

def remainder(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Computes the IEEE remainder of x/y."""
    ...

def remquo(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"], /) -> Tuple["mpfr", int]:
    """Computes the remainder and low bits of the quotient."""
    ...

def rint(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Rounds x to the nearest integer, using current rounding mode."""
    ...

def rint_ceil(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Rounds x to the nearest integer, rounding up."""
    ...

def rint_floor(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Rounds x to the nearest integer, rounding down"""
    ...

def rint_round(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Rounds x to the nearest integer, rounding away from 0 for ties."""
    ...

def rint_trunc(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Rounds x to the nearest integer, rounding towards zero."""
    ...

def root_of_unity(n: int, k: int, /) -> "mpc":
    """Return the n-th root of mpc(1) raised to the k-th power."""
    ...

def c_div(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> "mpz":
    """Return the quotient of x divided by y, rounded towards +Inf (ceiling rounding)."""
    ...

def c_div_2exp(x: Union[int, "mpz"], n: int, /) -> "mpz":
    """Returns the quotient of x divided by 2**n, rounded towards +Inf (ceiling rounding)."""
    ...

def c_divmod(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by y, quotient rounded towards +Inf (ceiling rounding)."""
    ...

def c_divmod_2exp(x: Union[int, "mpz"], n: int, /) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by 2**n, quotient rounded towards +Inf (ceiling rounding)"""
    ...

def c_mod(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> "mpz":
    """Return the remainder of x divided by y. The remainder will have the opposite sign of y."""
    ...

def c_mod_2exp(x: Union[int, "mpz"], n: int, /) -> "mpz":
    """Return the remainder of x divided by 2**n. The remainder will be negative."""
    ...

def f_div(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> "mpz":
    """Return the quotient of x divided by y, rounded towards -Inf (floor rounding)."""
    ...

def f_div_2exp(x: Union[int, "mpz"], n: int, /) -> "mpz":
    """Return the quotient of x divided by 2**n, rounded towards -Inf (floor rounding)."""
    ...

def f_divmod(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by y, quotient rounded towards -Inf (floor rounding)."""
    ...

def f_divmod_2exp(x: Union[int, "mpz"], n: int, /) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by 2**n, quotient rounded towards -Inf (floor rounding)."""
    ...

def f_mod(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> "mpz":
    """Return the remainder of x divided by y. The remainder will have the same sign as y."""
    ...

def f_mod_2exp(x: Union[int, "mpz"], n: int, /) -> "mpz":
    """Return remainder of x divided by 2**n. The remainder will be positive."""
    ...

def t_div(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> "mpz":
    """Return the quotient of x divided by y, rounded towards 0."""
    ...

def t_div_2exp(x: Union[int, "mpz"], n: int, /) -> "mpz":
    """Return the quotient of x divided by 2**n, rounded towards zero (truncation)."""
    ...

def t_divmod(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by y, quotient rounded towards zero (truncation)"""
    ...

def t_divmod_2exp(x: Union[int, "mpz"], n: int, /) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by 2**n, quotient rounded towards zero (truncation)."""
    ...

def t_mod(x: Union[int, "mpz"], y: Union[int, "mpz"], /) -> "mpz":
    """Return the remainder of x divided by y. The remainder will have the same sign as x."""
    ...

def t_mod_2exp(x: Union[int, "mpz"], n: int, /) -> "mpz":
    """Return the remainder of x divided by 2**n. The remainder will have the same sign as x."""
    ...

def cbrt(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return the cube root of x."""
    ...

def digamma(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return digamma of x."""
    ...

def eint(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return exponential integral of x."""
    ...

def erf(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return error function of x."""
    ...

def erfc(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return complementary error function of x."""
    ...

def exp10(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return 10**x."""
    ...

def exp2(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return 2**x."""
    ...

def expm1(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return exp(x) - 1."""
    ...

def fma(
    x: Union[int, float, mpz, mpfr, mpq, mpc],
    y: Union[int, float, mpz, mpfr, mpq, mpc],
    z: Union[int, float, mpz, mpfr, mpq, mpc],
    /,
) -> Union[mpz, mpq, mpfr, mpc]:
    """Return correctly rounded result of (x * y) + z."""
    ...

def fms(
    x: Union[int, float, mpz, mpfr, mpq, mpc],
    y: Union[int, float, mpz, mpfr, mpq, mpc],
    z: Union[int, float, mpz, mpfr, mpq, mpc],
    /,
) -> Union[mpz, mpq, mpfr, mpc]:
    """Return correctly rounded result of (x * y) - z."""
    ...

def fmma(
    x: Union[int, float, "mpz", "mpfr", "mpq"],
    y: Union[int, float, "mpz", "mpfr", "mpq"],
    z: Union[int, float, "mpz", "mpfr", "mpq"],
    t: Union[int, float, "mpz", "mpfr", "mpq"],
    /,
) -> "mpfr":
    """Return correctly rounded result of (x * y) + (z * t)."""
    ...

def fmms(
    x: Union[int, float, "mpz", "mpfr", "mpq"],
    y: Union[int, float, "mpz", "mpfr", "mpq"],
    z: Union[int, float, "mpz", "mpfr", "mpq"],
    t: Union[int, float, "mpz", "mpfr", "mpq"],
    /,
) -> "mpfr":
    """Return correctly rounded result of (x * y) - (z * t)."""
    ...

def frexp(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> Tuple[int, "mpfr"]:
    """Return a tuple containing the exponent and mantissa of x."""
    ...

def fsum(iterable: Iterator[Union[int, float, "mpz", "mpfr", "mpq"]], /) -> "mpfr":
    """Return an accurate sum of the values in the iterable."""
    ...

def gamma(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return gamma of x."""
    ...

def gamma_inc(a: Union[int, float, "mpz", "mpfr", "mpq"], x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return (upper) incomplete gamma of a and x."""
    ...

def hypot(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return square root of (x**2 + y**2)."""
    ...

def j0(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return first kind Bessel function of order 0 of x."""
    ...

def j1(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return first kind Bessel function of order 1 of x."""
    ...

def jn(n: int, x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return the first kind Bessel function of order n of x."""
    ...

def lgamma(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> Tuple["mpfr", int]:
    """Return a tuple containing the logarithm of the absolute value of gamma(x) and the sign of gamma(x)"""
    ...

def li2(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return real part of dilogarithm of x."""
    ...

def lngamma(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return natural logarithm of gamma(x)."""
    ...

def log1p(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return natural logarithm of (1+x)."""
    ...

def log2(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return base-2 logarithm of x."""
    ...

def maxnum(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return the maximum number of x and y."""
    ...

def minnum(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return the minimum number of x and y."""
    ...

def modf(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> Tuple["mpfr", "mpfr"]:
    """Return a tuple containing the integer and fractional portions of x."""
    ...

def reldiff(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return the relative difference between x and y."""
    ...

def root(x: Union[int, float, "mpz", "mpfr", "mpq"], n: int, /) -> "mpfr":
    """Return n-th root of x."""
    ...

def rootn(x: Union[int, float, "mpz", "mpfr", "mpq"], n: int, /) -> "mpfr":
    """Return n-th root of x (IEEE 754-2008 compliant)."""
    ...

def sec(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return secant of x; x in radians."""
    ...

def sech(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return hyperbolic secant of x."""
    ...

@overload
def sin_cos(x: Union[int, float, mpz, mpfr, mpq], /) -> Tuple["mpfr", "mpfr"]: ...
@overload
def sin_cos(x: "mpc", /) -> Tuple["mpc", "mpc"]: ...
def sin_cos(x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> Union[Tuple["mpfr", "mpfr"], Tuple["mpc", "mpc"]]:  # type: ignore[misc]
    """Return a tuple containing the sine and cosine of x."""
    ...

def sinh_cosh(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> Tuple["mpfr", "mpfr"]:
    """Return a tuple containing the hyperbolic sine and cosine of x."""
    ...

def y0(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return second kind Bessel function of order 0 of x."""
    ...

def y1(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return second kind Bessel function of order 1 of x."""
    ...

def yn(n: int, x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return the second kind Bessel function of order n of x."""
    ...

def zeta(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return Riemann zeta of x."""
    ...

def qdiv(x: Union[int, "mpz", "mpq"], y: Union[int, "mpz", "mpq"] = 1, /) -> Union["mpz", "mpq"]:
    """Return x/y as mpz if possible, or as mpq if x is not exactly divisible by y."""
    ...

def ieee(size: int, subnormalize: bool = True, /) -> context:
    """Return a new context corresponding to a standard IEEE floating-point format."""
    ...

@overload
def local_context(**kwargs: Any) -> context: ...
@overload
def local_context(ctx: context, /, **kwargs: Any) -> context: ...
def local_context(*args: Any, **kwargs: Any) -> context:  # type: ignore[misc]
    """Return a new context for controlling gmpy2 arithmetic, based either on the current context or
    on a ctx value."""
    ...

def set_context(context: context, /) -> None:
    """Activate a context object controlling gmpy2 arithmetic."""
    ...

def get_context() -> context:
    """Return a reference to the current context."""
    ...

def digits(x: Union[int, float, mpz, mpq, mpfr, mpc], base: int = 10, prec: int = 0, /) -> str:
    """Return string representing a number x."""
    ...

def to_binary(x: Union["mpz", "xmpz", "mpq", "mpfr", "mpc"], /) -> bytes:
    """Return a Python byte sequence that is a portable binary representation of x."""
    ...

def from_binary(data: bytes, /) -> Union["mpz", "xmpz", "mpq", "mpfr", "mpc"]:
    """Return a Python object from a byte sequence created by to_binary()."""
    ...

def license() -> str:
    """Return string giving license information."""
    ...

def mp_limbsize() -> int:
    """Return the number of bits per limb."""
    ...

def cmp(x: Union[int, float, mpz, mpq, mpfr], y: Union[int, float, mpz, mpq, mpfr], /) -> int:
    """Return -1 if x < y; 0 if x = y; or 1 if x > y."""
    ...

def cmp_abs(x: Union[int, float, mpz, mpfr, mpq, mpc], y: Union[int, float, mpz, mpfr, mpq, mpc], /) -> int:
    """Return -1 if abs(x) < abs(y); 0 if abs(x) = abs(y); or 1 else."""
    ...

def get_exp(x: Union[int, float, mpz, mpfr], /) -> int:
    """Return the exponent of x."""
    ...

def inf(n: Optional[Union[int, float, mpz, mpfr]] = None, /) -> "mpfr":
    """Return an mpfr initialized to Infinity with the same sign as n."""
    ...

def is_finite(x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> bool:
    """Return True if x is an actual number (i.e. non NaN or Infinity)."""
    ...

def is_infinite(x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> bool:
    """Return True if x is +Infinity or -Infinity."""
    ...

def is_integer(x: Union[int, float, mpz, mpfr, mpq], /) -> bool:
    """Return True if x is an integer; False otherwise."""
    ...

def is_nan(x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> bool:
    """Return True if x is NaN (Not-A-Number) else False."""
    ...

def is_regular(x: Union[int, float, mpz, mpfr, mpq], /) -> bool:
    """Return True if x is not zero, NaN, or Infinity; False otherwise."""
    ...

def is_signed(x: Union[int, float, mpz, mpfr], /) -> bool:
    """Return True if the sign bit of x is set."""
    ...

def is_unordered(x: Union[int, float, mpz, mpfr], y: Union[int, float, mpz, mpfr], /) -> bool:
    """Return True if either x and/or y is NaN."""
    ...

def is_zero(x: Union[int, float, mpz, mpfr, mpq, mpc], /) -> bool:
    """Return True if x is equal to 0."""
    ...

def mpfr_from_old_binary(data: bytes, /) -> "mpfr":
    """Return an mpfr from a GMPY 1.x binary mpf format."""
    ...

def nan() -> "mpfr":
    """Return an mpfr initialized to NaN (Not-A-Number)."""
    ...

def next_above(x: "mpfr", /) -> "mpfr":
    """Return the next mpfr from x toward +Infinity."""
    ...

def next_below(x: "mpfr", /) -> "mpfr":
    """Return the next mpfr from x toward -Infinity."""
    ...

def radians(x: Union[int, float, mpz, mpfr, mpq], /) -> "mpfr":
    """Convert angle x from degrees to radians."""
    ...

def degrees(x: Union[int, float, mpz, mpfr, mpq], /) -> "mpfr":
    """Convert angle x from radians to degrees."""
    ...

def rec_sqrt(x: Union[int, float, mpz, mpfr, mpq], /) -> "mpfr":
    """Return the reciprocal of the square root of x."""
    ...

def set_exp(x: "mpfr", n: int, /) -> "mpfr":
    """Set the exponent of x to n."""
    ...

def set_sign(x: "mpfr", s: bool, /) -> "mpfr":
    """If s is True, then return x with the sign bit set."""
    ...

def sign(x: Union[int, float, mpz, mpfr, mpq], /) -> int:
    """Return -1 if x < 0, 0 if x == 0, or +1 if x > 0."""
    ...

def zero(n: Optional[Union[int, float, mpz, mpfr]] = None, /) -> "mpfr":
    """Return an mpfr initialized to 0.0 with the same sign as n."""
    ...

def copy_sign(x: "mpfr", y: Union[int, float, mpz, mpfr], /) -> "mpfr":
    """Return an mpfr composed of x with the sign of y."""
    ...

def can_round(b: "mpfr", err: int, rnd1: int, rnd2: int, prec: int, /) -> bool:
    """Check if a number 'b' with error 'err' can be rounded correctly."""
    ...

def free_cache() -> None:
    """Free the internal cache of constants maintained by MPFR."""
    ...

def check_range(x: Union[int, float, "mpz", "mpfr", "mpq"], /) -> "mpfr":
    """Return a new mpfr with exponent that lies within the current range of emin and emax."""
    ...

def polar(x: "mpc", /) -> Tuple["mpfr", "mpfr"]:
    """Return the polar coordinate form of a complex x that is in rectangular form."""
    ...

def proj(x: "mpc", /) -> "mpc":
    """Returns the projection of a complex x on to the Riemann sphere."""
    ...

def rect(r: Union[int, float, mpz, mpfr, mpq], phi: Union[int, float, mpz, mpfr, mpq], /) -> "mpc":
    """Return the rectangular coordinate form of a complex number that is given in polar form."""
    ...

def norm(x: "mpc", /) -> "mpfr":
    """Return the norm of a complex x."""
    ...

def phase(x: "mpc", /) -> "mpfr":
    """Return the phase angle, also known as argument, of a complex x."""
    ...

def div_2exp(x: Union[mpfr, mpc], n: int, /) -> Union[mpfr, mpc]:
    """Return x divided by 2**n."""
    ...

def mul_2exp(x: Union[mpfr, mpc], n: int, /) -> Union[mpfr, mpc]:
    """Return x multiplied by 2**n."""
    ...

# Internal support for mpmath (marked as internal with leading underscore)
# Omit _mpmath_create and _mpmath_normalize

# Internal C API (marked as internal)
# Omit _C_API

# Constants
__version__: str = "2.2.1"  # Use the actual version from the documentation
__libgmp_version__: str = "6.3.0"  # Use string, get from docs if available, otherwise a reasonable guess
__libmpfr_version__: str = "4.2.1"  # Use string, get from docs if available, otherwise a reasonable guess
__libmpc_version__: str = "1.3.1"  # Use string, get from docs if available, otherwise a reasonable guess

# For IDE autocompletion and to make the linter happy.
__all__ = [
    # Classes
    "mpz",
    "mpq",
    "mpfr",
    "mpc",
    "xmpz",
    "context",
    "const_context",
    # Core arithmetic functions
    "add",
    "sub",
    "mul",
    "div",
    # "divmod", # Removed module level
    "mod",
    "sqrt",
    "isqrt",
    "isqrt_rem",
    "square",
    "iroot",
    "iroot_rem",
    # Number theoretic functions
    "powmod",
    "invert",
    "is_prime",
    "is_probab_prime",
    "gcd",
    "lcm",
    "gcdext",
    "divm",
    "fac",
    "bincoef",
    "fib",
    "fib2",
    "lucas",
    "lucas2",
    "jacobi",
    "legendre",
    "kronecker",
    "next_prime",
    "prev_prime",
    "comb",
    "divexact",
    "double_fac",
    "f2q",
    "is_bpsw_prp",
    "is_euler_prp",
    "is_extra_strong_lucas_prp",
    "is_fermat_prp",
    "is_fibonacci_prp",
    "is_lucas_prp",
    "is_selfridge_prp",
    "is_strong_bpsw_prp",
    "is_strong_lucas_prp",
    "is_strong_prp",
    "is_strong_selfridge_prp",
    "lucasu",
    "lucasu_mod",
    "lucasv",
    "lucasv_mod",
    "multi_fac",
    "pack",
    "powmod_base_list",
    "powmod_exp_list",
    "powmod_sec",
    "primorial",
    "remove",
    "unpack",
    "c_div",
    "c_div_2exp",
    "c_divmod",
    "c_divmod_2exp",
    "c_mod",
    "c_mod_2exp",
    "f_div",
    "f_div_2exp",
    "f_divmod",
    "f_divmod_2exp",
    "f_mod",
    "f_mod_2exp",
    "t_div",
    "t_div_2exp",
    "t_divmod",
    "t_divmod_2exp",
    "t_mod",
    "t_mod_2exp",
    "cbrt",
    "digamma",
    "eint",
    "erf",
    "erfc",
    "exp10",
    "exp2",
    "expm1",
    "fma",
    "fms",
    "fmma",
    "fmms",
    "frexp",
    "fsum",
    "gamma",
    "gamma_inc",
    "hypot",
    "j0",
    "j1",
    "jn",
    "lgamma",
    "li2",
    "lngamma",
    "log1p",
    "log2",
    "maxnum",
    "minnum",
    "modf",
    "reldiff",
    "root",
    "rootn",
    "sec",
    "sech",
    "sin_cos",
    "sinh_cosh",
    "y0",
    "y1",
    "yn",
    "zeta",
    "qdiv",
    "ieee",
    "local_context",
    "set_context",
    "get_context",
    # Random number generators
    "random_state",
    "mpz_random",
    "mpz_rrandomb",
    "mpz_urandomb",
    "mpfr_grandom",
    "mpfr_nrandom",
    "mpfr_random",
    "mpc_random",
    # Utility functions
    "hamdist",
    "popcount",
    "bit_mask",
    "bit_clear",
    "bit_count",
    "bit_flip",
    "bit_length",
    "bit_scan0",
    "bit_scan1",
    "bit_set",
    "bit_test",
    "num_digits",
    "is_divisible",
    "is_even",
    "is_odd",
    "is_power",
    "is_square",
    "is_congruent",
    "digits",
    "to_binary",
    "from_binary",
    "license",
    "mp_limbsize",
    "cmp",
    "cmp_abs",
    # MPFR constants and functions
    "const_log2",
    "const_pi",
    "const_euler",
    "const_catalan",
    "log",
    "log10",
    "exp",
    "sin",
    "cos",
    "tan",
    "atan",
    "atan2",
    "sinh",
    "cosh",
    "tanh",
    "atanh",
    "asin",
    "acos",
    "asinh",
    "acosh",
    "floor",
    "ceil",
    "trunc",
    "round2",
    "round_away",
    "fmod",
    "remainder",
    "remquo",
    "rint",
    "rint_ceil",
    "rint_floor",
    "rint_round",
    "rint_trunc",
    "root_of_unity",
    "get_exp",
    "inf",
    "is_finite",
    "is_infinite",
    "is_integer",
    "is_nan",
    "is_regular",
    "is_signed",
    "is_unordered",
    "is_zero",
    "mpfr_from_old_binary",
    "nan",
    "next_above",
    "next_below",
    "radians",
    "degrees",
    "rec_sqrt",
    "set_exp",
    "set_sign",
    "sign",
    "zero",
    "copy_sign",
    "can_round",
    "free_cache",
    "check_range",
    # MPC functions
    "polar",
    "proj",
    "rect",
    "norm",
    "phase",
    "div_2exp",
    "mul_2exp",
    # Library information
    "version",
    "mp_version",
    # "get_cache", # Removed
    # "set_cache", # Removed
    "get_max_precision",
    # "set_max_precision", # Removed
    # "get_minprec", # Removed
    # "get_maxprec", # Removed
    "get_emax_max",
    "get_emin_min",
    "mpc_version",
    "mpfr_version",
    # Version strings
    "__version__",
    "__libgmp_version__",
    "__libmpfr_version__",
    "__libmpc_version__",
    # Rounding Modes
    "MPFR_RNDN",
    "MPFR_RNDZ",
    "MPFR_RNDU",
    "MPFR_RNDD",
    "MPFR_RNDA",
    "MPFR_RNDF",
    # Exceptions
    "Gmpy2Error",
    "RoundingError",
    "InexactResultError",
    "UnderflowResultError",
    "OverflowResultError",
    "InvalidOperationError",
    "DivisionByZeroError",
    "RangeError",
]
