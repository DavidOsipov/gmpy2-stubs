"""
Type stubs for gmpy2 - GNU Multiple Precision Arithmetic Library interface (version 2.2.1)

Stub file version: 2.2.1.1

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

*   Python 3.7+ (matches gmpy2's requirements)

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
# pyright: reportDeprecated=false

from types import TracebackType
from typing import Any, ContextManager, Iterator, Optional, Tuple, Type, TypeVar, Union, overload

# Type definitions
T = TypeVar("T")
_mpz_type = "mpz"  # Use string forward reference
_mpq_type = "mpq"
_mpfr_type = "mpfr"
_mpc_type = "mpc"

# Rounding modes for mpfr
MPFR_RNDN = 0  # Round to nearest, with ties to even
MPFR_RNDZ = 1  # Round toward zero
MPFR_RNDU = 2  # Round toward +Inf
MPFR_RNDD = 3  # Round toward -Inf
MPFR_RNDA = 4  # Round away from zero
MPFR_RNDF = 5  # Round to nearest, with ties to away (faithful rounding)

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
    def bit_length(self) -> int: ...
    def bit_test(self, n: int) -> bool: ...
    def bit_set(self, n: int) -> "mpz": ...
    def bit_clear(self, n: int) -> "mpz": ...
    def bit_flip(self, n: int) -> "mpz": ...
    def bit_scan0(self, starting_bit: int = 0) -> int: ...
    def bit_scan1(self, starting_bit: int = 0) -> int: ...
    def num_digits(self, base: int = 10) -> int: ...
    def is_square(self) -> bool: ...
    def is_power(self) -> bool: ...
    def is_prime(self, n: int = 25) -> bool: ...
    def is_probab_prime(self, n: int = 25) -> int: ...
    def is_congruent(self, other: Union[int, "mpz"], mod: Union[int, "mpz"]) -> bool: ...
    def to_bytes(self, length: int, byteorder: str, *, signed: bool = False) -> bytes: ...
    @classmethod
    def from_bytes(cls, bytes_val: bytes, byteorder: str, *, signed: bool = False) -> "mpz": ...
    def as_integer_ratio(self) -> Tuple["mpz", "mpz"]: ...
    def conjugate(self) -> "mpz": ...  # Returns self
    @property
    def denominator(self) -> "mpz": ...  # Returns 1
    @property
    def imag(self) -> "mpz": ...  # Returns 0
    @property
    def numerator(self) -> "mpz": ...  # Returns self
    @property
    def real(self) -> "mpz": ...  # Returns self

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
    @property
    def numerator(self) -> "mpz": ...  # numerator is a property in the actual class
    @property
    def denominator(self) -> "mpz": ...  # denominator is a property in the actual class
    @classmethod
    def from_float(cls, f: float) -> "mpq": ...
    @classmethod
    def from_decimal(cls, d: Any) -> "mpq": ...  # Assuming 'Any' is a placeholder for 'decimal.Decimal'
    def as_integer_ratio(self) -> Tuple["mpz", "mpz"]: ...
    def conjugate(self) -> "mpq": ...
    @property
    def real(self) -> "mpq": ...  # Returns self
    @property
    def imag(self) -> "mpq": ...  # Returns 0

class mpfr:
    """Multiple precision floating-point type"""

    def __new__(
        cls,
        x: Union[int, str, float, "mpz", "mpfr", "mpq", "mpc", bytes] = 0,
        precision: int = 53,  # Default precision
        rounding: int = MPFR_RNDN,
    ) -> "mpfr": ...  # Default rounding
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
    def __pow__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr": ...
    def __rpow__(self, other: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr": ...
    def __neg__(self) -> "mpfr": ...
    def __pos__(self) -> "mpfr": ...
    def __abs__(self) -> "mpfr": ...
    def is_integer(self) -> bool: ...
    def is_zero(self) -> bool: ...
    def is_nan(self) -> bool: ...
    def is_inf(self) -> bool: ...
    def is_finite(self) -> bool: ...
    def is_signed(self) -> bool: ...
    @property
    def precision(self) -> int: ...  # precision is a property in the actual class.
    def as_integer_ratio(self) -> Tuple["mpz", "mpz"]: ...
    def as_mantissa_exp(self) -> Tuple["mpz", int]: ...
    def as_simple_fraction(self, precision: int = 0) -> "mpq": ...
    def conjugate(self) -> "mpfr": ...  # Returns self
    @property
    def real(self) -> "mpfr": ...  # Returns self
    @property
    def imag(self) -> "mpfr": ...  # Returns 0
    @property
    def rc(self) -> int: ...  # Return code of the last mpfr operation

class mpc:
    """Multi-precision complex number type"""

    def __new__(
        cls,
        re: Union[int, str, float, "mpz", "mpfr", "mpc", bytes] = 0,
        im: Union[int, str, float, "mpz", "mpfr", "mpc", bytes] = 0,
        precision: Union[int, Tuple[int, int]] = 53,
        rounding: Union[int, Tuple[int, int]] = MPFR_RNDN,
    ) -> "mpc": ...
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
    def __pow__(self, other: Union[int, float, "mpz", "mpc", "mpfr"]) -> "mpc": ...
    def __rpow__(self, other: Union[int, float, "mpz", "mpc", "mpfr"]) -> "mpc": ...
    def __neg__(self) -> "mpc": ...
    def __pos__(self) -> "mpc": ...
    def __abs__(self) -> "mpfr": ...
    def conjugate(self) -> "mpc": ...
    def real(self) -> "mpfr": ...
    def imag(self) -> "mpfr": ...
    def phase(self) -> "mpfr": ...
    def norm(self) -> "mpfr": ...
    def is_finite(self) -> bool: ...
    def is_inf(self) -> bool: ...
    def is_nan(self) -> bool: ...
    def is_zero(self) -> bool: ...
    @property
    def rc(self) -> Tuple[int, int]: ...  # Return codes for real and imag parts

# Exception types
class Gmpy2Error(Exception): ...
class RoundingError(Gmpy2Error): ...
class InexactResultError(RoundingError): ...
class UnderflowResultError(RoundingError): ...
class OverflowResultError(RoundingError): ...
class InvalidOperationError(Gmpy2Error): ...
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

def get_cache() -> Tuple[int, int]:
    """Returns a tuple containing the current cache settings (size, limbs)."""
    ...

def set_cache(size: int, limbs: int = 1) -> Tuple[int, int]:
    """Sets the cache size and returns the old cache settings."""
    ...

def get_max_precision() -> int:
    """Returns the current maximum precision for mpfr operations."""
    ...

def set_max_precision(precision: int) -> int:
    """Sets the maximum precision for mpfr operations and returns the old value."""
    ...

def get_minprec() -> int:
    """Returns the minimum precision supported by mpfr."""
    ...

def get_maxprec() -> int:
    """Returns the maximum precision supported by mpfr."""
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
        trap_expbound: Optional[bool] = None,
        allow_complex: bool = False,
        allow_release_gil: bool = False,
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
    @property
    def trap_expbound(self) -> bool:
        """Trap exceptions for exceeding exponent bounds."""
        ...

    @trap_expbound.setter
    def trap_expbound(self, value: bool) -> None: ...
    @property
    def trap_divbyzero(self) -> bool:
        """Trap division by zero exceptions."""
        ...

    @trap_divbyzero.setter
    def trap_divbyzero(self, value: bool) -> None: ...
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
    # Context methods (mirror gmpy2 functions)
    def abs(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpz, mpfr, mpq]:
        """Computes the absolute value of x."""
        ...

    def acos(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the arccosine of x."""
        ...

    def acosh(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the inverse hyperbolic cosine of x."""
        ...

    def add(self, x: Union[int, float, mpz, mpfr, mpq, mpc], y: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes the sum of x and y."""
        ...

    def agm(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the arithmetic-geometric mean of x and y."""
        ...

    def ai(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the Airy function of x."""
        ...

    def asin(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the arcsine of x."""
        ...

    def asinh(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the inverse hyperbolic sine of x."""
        ...

    def atan(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the arctangent of x."""
        ...

    def atan2(self, y: Union[int, float, mpz, mpfr, mpq], x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the two-argument arctangent of y/x."""
        ...

    def atanh(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the inverse hyperbolic tangent of x."""
        ...

    def cbrt(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the cube root of x."""
        ...

    def ceil(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
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

    def cos(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the cosine of x."""
        ...

    def cosh(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the hyperbolic cosine of x."""
        ...

    def cot(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the cotangent of x."""
        ...

    def coth(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the hyperbolic cotangent of x."""
        ...

    def csc(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the cosecant of x."""
        ...

    def csch(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the hyperbolic cosecant of x."""
        ...

    def degrees(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Converts angle x from radians to degrees."""
        ...

    def digamma(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the digamma function of x."""
        ...

    def div(self, x: Union[int, float, mpz, mpfr, mpq, mpc], y: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpq, mpfr, mpc]:
        """Computes the division of x by y."""
        ...

    def div_2exp(self, x: Union[int, float, mpz, mpfr, mpq, mpc], n: int) -> Union[mpfr, mpc]:
        """Computes x divided by 2^n."""
        ...

    def divmod(self, x: Union[int, "mpz"], y: Union[int, "mpz"]) -> Tuple["mpz", "mpz"]:
        """Computes the quotient and remainder of x divided by y."""
        ...

    def eint(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the exponential integral of x."""
        ...

    def erf(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the error function of x."""
        ...

    def erfc(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the complementary error function of x."""
        ...

    def exp(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the exponential function e^x."""
        ...

    def exp10(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes 10^x."""
        ...

    def exp2(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes 2^x."""
        ...

    def expm1(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes exp(x) - 1."""
        ...

    def factorial(self, n: Union[int, mpz]) -> mpfr:
        """Computes the factorial of n."""
        ...

    def floor(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the floor of x."""
        ...

    def floor_div(self, x: Union[int, mpz, mpfr, mpq], y: Union[int, mpz, mpfr, mpq]) -> Union[mpz, mpfr]:
        """Computes the floor division of x by y."""
        ...

    def fma(
        self,
        x: Union[int, float, mpz, mpfr, mpq, mpc],
        y: Union[int, float, mpz, mpfr, mpq, mpc],
        z: Union[int, float, mpz, mpfr, mpq, mpc],
    ) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes (x * y) + z with a single rounding."""
        ...

    def fmma(
        self,
        x: Union[int, float, mpz, mpfr, mpq],
        y: Union[int, float, mpz, mpfr, mpq],
        z: Union[int, float, mpz, mpfr, mpq],
        t: Union[int, float, mpz, mpfr, mpq],
    ) -> mpfr:
        """Computes (x * y) + (z * t) with a single rounding."""
        ...

    def fmms(
        self,
        x: Union[int, float, mpz, mpfr, mpq],
        y: Union[int, float, mpz, mpfr, mpq],
        z: Union[int, float, mpz, mpfr, mpq],
        t: Union[int, float, mpz, mpfr, mpq],
    ) -> mpfr:
        """Computes (x * y) - (z * t) with a single rounding."""
        ...

    def fmod(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the floating-point remainder of x/y."""
        ...

    def fms(
        self,
        x: Union[int, float, mpz, mpfr, mpq, mpc],
        y: Union[int, float, mpz, mpfr, mpq, mpc],
        z: Union[int, float, mpz, mpfr, mpq, mpc],
    ) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes (x * y) - z with a single rounding."""
        ...

    def frac(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the fractional part of x."""
        ...

    def frexp(self, x: Union[int, float, mpz, mpfr, mpq]) -> Tuple[int, mpfr]:
        """Returns the mantissa and exponent of x."""
        ...

    def fsum(self, iterable: Iterator[Union[int, float, mpz, mpfr, mpq]]) -> mpfr:
        """Computes an accurate sum of the values in the iterable."""
        ...

    def gamma(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the gamma function of x."""
        ...

    def gamma_inc(self, a: Union[int, float, mpz, mpfr, mpq], x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the incomplete gamma function of a and x."""
        ...

    def hypot(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the square root of (x^2 + y^2)."""
        ...

    def j0(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the Bessel function of the first kind of order 0 of x."""
        ...

    def j1(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the Bessel function of the first kind of order 1 of x."""
        ...

    def jn(self, n: int, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the Bessel function of the first kind of order n of x."""
        ...

    def lgamma(self, x: Union[int, float, mpz, mpfr, mpq]) -> Tuple[mpfr, int]:
        """Computes the logarithm of the absolute value of gamma(x) and the sign of gamma(x)."""
        ...

    def li2(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the real part of the dilogarithm of x."""
        ...

    def lngamma(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the natural logarithm of the absolute value of gamma(x)."""
        ...

    @overload
    def log(self, x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpfr", "mpc"]:
        """Computes the natural logarithm of x."""
        ...

    @overload
    def log(self, x: Union[int, float, "mpz", "mpfr", "mpq"], base: Union[int, float, "mpz", "mpfr"]) -> "mpfr":
        """Computes the logarithm of x to the specified base.

        If base is None, returns the natural logarithm.

        Args:
            x: The value to compute logarithm for (must be > 0)
            base: The logarithm base (must be > 0 and != 1)

        Returns:
            The logarithm as an mpfr object

        Raises:
            ValueError: If x <= 0 or base <= 0 or base == 1
        """
        ...

    def log10(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the base-10 logarithm of x."""
        ...

    def log1p(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the natural logarithm of (1+x)."""
        ...

    def log2(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the base-2 logarithm of x."""
        ...

    def maxnum(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Returns the maximum of x and y."""
        ...

    def minnum(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Returns the minimum of x and y."""
        ...

    def mod(self, x: Union[int, "mpz"], y: Union[int, "mpz"]) -> "mpz":
        """Computes x mod y."""
        ...

    def modf(self, x: Union[int, float, mpz, mpfr, mpq]) -> Tuple[mpfr, mpfr]:
        """Returns the fractional and integer parts of x."""
        ...

    def mul(self, x: Union[int, float, mpz, mpfr, mpq, mpc], y: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes the product of x and y."""
        ...

    def mul_2exp(self, x: Union[int, float, mpz, mpfr, mpq, mpc], n: int) -> Union[mpfr, mpc]:
        """Computes x multiplied by 2^n."""
        ...

    def next_above(self, x: "mpfr") -> "mpfr":
        """Returns the next representable floating-point number above x."""
        ...

    def next_below(self, x: "mpfr") -> "mpfr":
        """Returns the next representable floating-point number below x."""
        ...

    def next_toward(self, x: "mpfr", y: "mpfr") -> "mpfr":
        """Returns the next representable floating-point number from x in the direction of y."""
        ...

    def norm(self, x: "mpc") -> "mpfr":
        """Computes the norm of the complex number x."""
        ...

    def phase(self, x: "mpc") -> "mpfr":
        """Computes the phase (argument) of the complex number x."""
        ...

    def polar(self, x: "mpc") -> Tuple["mpfr", "mpfr"]:
        """Converts a complex number from rectangular to polar coordinates."""
        ...

    def pow(self, x: Union[int, float, mpz, mpfr, mpq, mpc], y: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes x raised to the power of y."""
        ...

    def proj(self, x: "mpc") -> "mpc":
        """Computes the projection of a complex number onto the Riemann sphere."""
        ...

    def radians(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Converts angle x from degrees to radians."""
        ...

    def rec_sqrt(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the reciprocal of the square root of x."""
        ...

    def reldiff(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the relative difference between x and y."""
        ...

    def remainder(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the IEEE remainder of x/y."""
        ...

    def remquo(self, x: Union[int, float, mpz, mpfr, mpq], y: Union[int, float, mpz, mpfr, mpq]) -> Tuple[mpfr, int]:
        """Computes the remainder and low bits of the quotient."""
        ...

    def rint(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Rounds x to the nearest integer, using the current rounding mode."""
        ...

    def rint_ceil(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Rounds x to the nearest integer, rounding up."""
        ...

    def rint_floor(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Rounds x to the nearest integer, rounding down."""
        ...

    def rint_round(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Rounds x to the nearest integer, rounding to even for ties."""
        ...

    def rint_trunc(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Rounds x to the nearest integer, rounding towards zero."""
        ...

    def root(self, x: Union[int, float, mpz, mpfr, mpq], n: int) -> mpfr:
        """Computes the nth root of x."""
        ...

    def root_of_unity(self, n: int, k: int) -> mpc:
        """Computes the (n,k)-th root of unity."""
        ...

    def rootn(self, x: Union[int, float, mpz, mpfr, mpq], n: int) -> mpfr:
        """Computes the nth root of x."""
        ...

    def round2(self, x: Union[int, float, mpz, mpfr, mpq], n: int) -> mpfr:
        """Rounds x to the nearest multiple of 2^n."""
        ...

    def round_away(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Rounds x to the nearest integer, away from 0 in case of a tie."""
        ...

    def sec(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the secant of x."""
        ...

    def sech(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the hyperbolic secant of x."""
        ...

    def sin(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the sine of x."""
        ...

    def sin_cos(self, x: Union[int, float, mpz, mpfr, mpq]) -> Tuple[mpfr, mpfr]:
        """Computes the sine and cosine of x."""
        ...

    def sinh(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the hyperbolic sine of x."""
        ...

    def sinh_cosh(self, x: Union[int, float, mpz, mpfr, mpq]) -> Tuple[mpfr, mpfr]:
        """Computes the hyperbolic sine and cosine of x."""
        ...

    def sqrt(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the square root of x."""
        ...

    def square(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes the square of x."""
        ...

    def sub(self, x: Union[int, float, mpz, mpfr, mpq, mpc], y: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpz, mpq, mpfr, mpc]:
        """Computes the difference of x and y."""
        ...

    def tan(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the tangent of x."""
        ...

    def tanh(self, x: Union[int, float, mpz, mpfr, mpq, mpc]) -> Union[mpfr, mpc]:
        """Computes the hyperbolic tangent of x."""
        ...

    def trunc(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Truncates x towards zero."""
        ...

    def y0(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the Bessel function of the second kind of order 0 of x."""
        ...

    def y1(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the Bessel function of the second kind of order 1 of x."""
        ...

    def yn(self, n: int, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the Bessel function of the second kind of order n of x."""
        ...

    def zeta(self, x: Union[int, float, mpz, mpfr, mpq]) -> mpfr:
        """Computes the Riemann zeta function of x."""
        ...

    def clear_flags(self) -> None:
        """Clears all exception flags."""
        ...

    def copy(self) -> "context":
        """Returns a copy of the context."""
        ...

    def ieee(self, size: int, subnormalize: bool = True) -> "context":
        """Return a new context corresponding to a standard IEEE floating-point format."""
        ...

    def set_context(self, context: "context") -> None:
        """Activate a context object controlling gmpy2 arithmetic."""
        ...

    def local_context(self, **kwargs: Any) -> ContextManager["context"]:
        """Return a new context for controlling gmpy2 arithmetic, based either on the current context or on a ctx value."""
        ...

class const_context:
    """Context manager for constant creation with specific precision."""

    def __init__(self, precision: int) -> None: ...
    def __enter__(self) -> "const_context": ...
    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]
    ) -> None: ...

# Number theoretic functions
def powmod(x: Union[int, "mpz"], y: Union[int, "mpz"], m: Union[int, "mpz"]) -> "mpz":
    """Computes (x**y) mod m efficiently.

    Args:
        x: The base value
        y: The exponent value
        m: The modulus value

    Returns:
        (x**y) mod m as an mpz object

    Raises:
        ZeroDivisionError: If m is 0
        ValueError: If y < 0 and x has no inverse modulo m
    """
    ...

def invert(x: Union[int, "mpz"], m: Union[int, "mpz"]) -> "mpz":
    """Computes the multiplicative inverse of x modulo m.

    Args:
        x: The value to invert
        m: The modulus value

    Returns:
        y such that (x * y) mod m = 1, or 0 if no inverse exists.

    Raises:
        ZeroDivisionError: If m is 0
    """
    ...

def is_prime(x: Union[int, "mpz"], n: int = 25) -> bool:
    """Performs probabilistic primality test on x.

    Args:
        x: The value to test for primality
        n: Number of tests to perform (higher values increase confidence)

    Returns:
        True if x is probably prime, False if x is definitely composite
    """
    ...

def is_probab_prime(x: Union[int, "mpz"], n: int = 25) -> int:
    """Performs probabilistic primality test on x.

    Args:
        x: The value to test for primality
        n: Number of tests to perform

    Returns:
        0 if x is definitely composite, 1 if x is probably prime, 2 if x is definitely prime
    """
    ...

def gcd(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> "mpz":
    """Computes the greatest common divisor of x and y.

    Args:
        x: First value
        y: Second value

    Returns:
        The greatest common divisor of x and y as an mpz object
    """
    ...

def lcm(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> "mpz":
    """Computes the least common multiple of x and y."""
    ...

def gcdext(a: Union[int, "mpz"], b: Union[int, "mpz"]) -> Tuple["mpz", "mpz", "mpz"]:
    """Computes the extended GCD of a and b.

    Args:
        a: First value
        b: Second value

    Returns:
        A tuple (g, s, t) where g is the GCD of a and b, and s and t are
        coefficients satisfying g = a*s + b*t
    """
    ...

def divm(a: Union[int, "mpz"], b: Union[int, "mpz"], m: Union[int, "mpz"]) -> "mpz":
    """Computes (a/b) mod m, which is equivalent to (a * invert(b, m)) mod m.

    Args:
        a: Numerator
        b: Denominator
        m: Modulus

    Returns:
        (a/b) mod m as an mpz object

    Raises:
        ZeroDivisionError: If b has no inverse modulo m or if m is 0
    """
    ...

def fac(n: Union[int, "mpz"]) -> "mpz":
    """Computes the factorial of n.

    Args:
        n: The value to compute factorial for

    Returns:
        n! as an mpz object

    Raises:
        ValueError: If n is negative
    """
    ...

def fib(n: Union[int, "mpz"]) -> "mpz":
    """Computes the nth Fibonacci number F(n).

    Args:
        n: The index of the Fibonacci number to compute

    Returns:
        F(n) as an mpz object
    """
    ...

def fib2(n: Union[int, "mpz"]) -> Tuple["mpz", "mpz"]:
    """Computes a tuple of Fibonacci numbers (F(n), F(n-1)).

    Args:
        n: The index of the Fibonacci number to compute

    Returns:
        Tuple (F(n), F(n-1)) as mpz objects
    """
    ...

def lucas(n: Union[int, "mpz"]) -> "mpz":
    """Computes the nth Lucas number L(n).

    Args:
        n: The index of the Lucas number to compute

    Returns:
        L(n) as an mpz object
    """
    ...

def lucas2(n: Union[int, "mpz"]) -> Tuple["mpz", "mpz"]:
    """Computes a tuple of Lucas numbers (L(n), L(n-1)).

    Args:
        n: The index of the Lucas number to compute

    Returns:
        Tuple (L(n), L(n-1)) as mpz objects
    """
    ...

def jacobi(a: Union[int, "mpz"], b: Union[int, "mpz"]) -> int:
    """Computes the Jacobi symbol (a/b).

    Args:
        a: The numerator
        b: The denominator (must be odd and > 0)

    Returns:
        The Jacobi symbol value (-1, 0, or 1)

    Raises:
        ValueError: If b is even or <= 0
    """
    ...

def legendre(a: Union[int, "mpz"], p: Union[int, "mpz"]) -> int:
    """Computes the Legendre symbol (a/p).

    Args:
        a: The numerator
        p: The denominator (must be prime)

    Returns:
        The Legendre symbol value (-1, 0, or 1)

    Raises:
        ValueError: If p is not prime
    """
    ...

def kronecker(a: Union[int, "mpz"], b: Union[int, "mpz"]) -> int:
    """Computes the Kronecker symbol (a/b).

    Args:
        a: The numerator
        b: The denominator

    Returns:
        The Kronecker symbol value (-1, 0, or 1)
    """
    ...

def next_prime(x: Union[int, "mpz"]) -> "mpz":
    """Finds the next prime number greater than x.

    Args:
        x: The starting value

    Returns:
        The next prime number > x as an mpz object
    """
    ...

def prev_prime(x: Union[int, "mpz"]) -> "mpz":
    """Finds the previous prime number less than x.

    Args:
        x: The starting value

    Returns:
        The previous prime number < x as an mpz object

    Raises:
        ValueError: If no prime < x exists
    """
    ...

def bincoef(n: Union[int, "mpz"], k: Union[int, "mpz"]) -> "mpz":
    """Computes the binomial coefficient (n choose k)."""
    ...

def comb(n: Union[int, "mpz"], k: Union[int, "mpz"]) -> "mpz":
    """Return the number of combinations of n things, taking k at a time'. k >= 0. Same as bincoef(n, k)"""
    ...

def divexact(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> "mpz":
    """Return the quotient of x divided by y. Faster than standard division but requires the remainder is zero!"""
    ...

def double_fac(n: Union[int, "mpz"]) -> "mpz":
    """Return the exact double factorial (n!!) of n."""
    ...

def f2q(x: "mpfr", err: int = 0) -> Union["mpz", "mpq"]:
    """Return the 'best' mpq approximating x to within relative error err."""
    ...

def is_bpsw_prp(n: Union[int, "mpz"]) -> bool:
    """Return True if n is a Baillie-Pomerance-Selfridge-Wagstaff probable prime."""
    ...

def is_euler_prp(n: Union[int, "mpz"], a: Union[int, "mpz"]) -> bool:
    """Return True if n is an Euler (also known as Solovay-Strassen) probable prime to the base a."""
    ...

def is_extra_strong_lucas_prp(n: Union[int, "mpz"], p: Union[int, "mpz"]) -> bool:
    """Return True if n is an extra strong Lucas probable prime with parameters (p,1)."""
    ...

def is_fermat_prp(n: Union[int, "mpz"], a: Union[int, "mpz"]) -> bool:
    """Return True if n is a Fermat probable prime to the base a."""
    ...

def is_fibonacci_prp(n: Union[int, "mpz"], p: Union[int, "mpz"], q: Union[int, "mpz"]) -> bool:
    """Return True if n is a Fibonacci probable prime with parameters (p,q)."""
    ...

def is_lucas_prp(n: Union[int, "mpz"], p: Union[int, "mpz"], q: Union[int, "mpz"]) -> bool:
    """Return True if n is a Lucas probable prime with parameters (p,q)."""
    ...

def is_selfridge_prp(n: Union[int, "mpz"]) -> bool:
    """Return True if n is a Lucas probable prime with Selfidge parameters (p,q)."""
    ...

def is_strong_bpsw_prp(n: Union[int, "mpz"]) -> bool:
    """Return True if n is a strong Baillie-Pomerance-Selfridge-Wagstaff probable prime."""
    ...

def is_strong_lucas_prp(n: Union[int, "mpz"], p: Union[int, "mpz"], q: Union[int, "mpz"]) -> bool:
    """Return True if n is a strong Lucas probable prime with parameters (p,q)."""
    ...

def is_strong_prp(n: Union[int, "mpz"], a: Union[int, "mpz"]) -> bool:
    """Return True if n is a strong (also known as Miller-Rabin) probable prime to the base a."""
    ...

def is_strong_selfridge_prp(n: Union[int, "mpz"]) -> bool:
    """Return True if n is a strong Lucas probable prime with Selfidge parameters (p,q)."""
    ...

def lucasu(p: Union[int, "mpz"], q: Union[int, "mpz"], k: Union[int, "mpz"]) -> "mpz":
    """Return the k-th element of the Lucas U sequence defined by p,q."""
    ...

def lucasu_mod(p: Union[int, "mpz"], q: Union[int, "mpz"], k: Union[int, "mpz"], n: Union[int, "mpz"]) -> "mpz":
    """Return the k-th element of the Lucas U sequence defined by p,q (mod n)."""
    ...

def lucasv(p: Union[int, "mpz"], q: Union[int, "mpz"], k: Union[int, "mpz"]) -> "mpz":
    """Return the k-th element of the Lucas V sequence defined by p,q."""
    ...

def lucasv_mod(p: Union[int, "mpz"], q: Union[int, "mpz"], k: Union[int, "mpz"], n: Union[int, "mpz"]) -> "mpz":
    """Return the k-th element of the Lucas V sequence defined by p,q (mod n)."""
    ...

def multi_fac(n: Union[int, "mpz"], m: Union[int, "mpz"]) -> "mpz":
    """Return the exact m-multi factorial of n."""
    ...

def pack(lst: list[int], n: int) -> "mpz":
    """Pack a list of integers lst into a single mpz."""
    ...

def powmod_base_list(base_lst: list[Union[int, "mpz"]], exp: Union[int, "mpz"], mod: Union[int, "mpz"]) -> list["mpz"]:
    """Returns list(powmod(i, exp, mod) for i in base_lst)."""
    ...

def powmod_exp_list(base: Union[int, "mpz"], exp_lst: list[Union[int, "mpz"]], mod: Union[int, "mpz"]) -> list["mpz"]:
    """Returns list(powmod(base, i, mod) for i in exp_lst)."""
    ...

def powmod_sec(x: Union[int, "mpz"], y: Union[int, "mpz"], m: Union[int, "mpz"]) -> "mpz":
    """Return (x**y) mod m, using a more secure algorithm."""
    ...

def primorial(n: Union[int, "mpz"]) -> "mpz":
    """Return the product of all positive prime numbers less than or equal to n."""
    ...

def remove(x: Union[int, "mpz"], f: Union[int, "mpz"]) -> Tuple["mpz", int]:
    """Return a 2-element tuple (y,m) such that x=y*(f**m) and f does not divide y."""
    ...

def unpack(x: Union[int, "mpz"], n: int) -> list[int]:
    """Unpack an integer x into a list of n-bit values."""
    ...

# Core arithmetic functions
def add(x: Union[int, "mpz", "mpfr", "mpq", "mpc"], y: Union[int, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpz", "mpfr", "mpq", "mpc"]:
    """Adds two numbers.

    Returns a type based on the types of inputs: mpz, mpfr, or mpq.
    """
    ...

def sub(x: Union[int, "mpz", "mpfr", "mpq", "mpc"], y: Union[int, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpz", "mpfr", "mpq", "mpc"]:
    """Subtracts y from x.

    Returns a type based on the types of inputs: mpz, mpfr, or mpq.
    """
    ...

def mul(x: Union[int, "mpz", "mpfr", "mpq", "mpc"], y: Union[int, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpz", "mpfr", "mpq", "mpc"]:
    """Multiplies two numbers.

    Returns a type based on the types of inputs: mpz, mpfr, or mpq.
    """
    ...

def div(x: Union[int, "mpz", "mpfr", "mpq", "mpc"], y: Union[int, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpfr", "mpq", "mpc"]:
    """Divides x by y.

    Returns mpq if both inputs are integer-like, otherwise returns mpfr.

    Raises:
        ZeroDivisionError: If y is 0
    """
    ...

def divmod(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> Tuple["mpz", "mpz"]:
    """Computes quotient and remainder of x divided by y.

    Args:
        x: The dividend
        y: The divisor

    Returns:
        A tuple (q, r) where q is the quotient and r is the remainder

    Raises:
        ZeroDivisionError: If y is 0
    """
    ...

def mod(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> "mpz":
    """Computes x mod y.

    Args:
        x: The dividend
        y: The divisor

    Returns:
        x mod y as an mpz object

    Raises:
        ZeroDivisionError: If y is 0
    """
    ...

def sqrt(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpz", "mpfr", "mpc"]:
    """Computes the square root of x.

    Returns mpfr for most inputs. If x is a perfect square integer, it returns mpz. Returns mpc if allow_complex is True and x is negative

    Raises:
        ValueError: If x is negative and not complex
    """
    ...

def isqrt(x: Union[int, "mpz"]) -> "mpz":
    """Computes the integer square root of x (floor of sqrt(x)).

    Args:
        x: The value to compute the integer square root for

    Returns:
        The floor of the square root of x as an mpz object

    Raises:
        ValueError: If x is negative
    """
    ...

def isqrt_rem(x: Union[int, "mpz"]) -> Tuple["mpz", "mpz"]:
    """Computes the integer square root and remainder of x.

    Args:
        x: The value to compute the integer square root for

    Returns:
        A tuple (s, r) where s is the integer square root and r is the remainder
        such that x = s*s + r

    Raises:
        ValueError: If x is negative
    """
    ...

def square(x: Union[int, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpz", "mpfr", "mpq", "mpc"]:
    """Computes the square of x.

    Returns a type matching the input type.
    """
    ...

# Random number generators
def random_state(seed: Optional[Union[int, str, bytes, Any]] = None) -> Any:
    """Creates a random state object for use with the random number generators.

    Args:
        seed: Optional seed value (int, string, or bytes)

    Returns:
        A random state object that can be used with the mpz_random functions
    """
    ...

def mpz_random(state: Any, n: Union[int, "mpz"]) -> "mpz":
    """Generates a uniformly distributed random integer in the range [0, n-1].

    Args:
        state: Random state object from random_state()
        n: Upper bound (exclusive)

    Returns:
        A random mpz in the range [0, n-1]
    """
    ...

def mpz_rrandomb(state: Any, b: int) -> "mpz":
    """Generates a random integer with exactly b random bits.

    Args:
        state: Random state object
        b: Number of bits

    Returns:
        A random mpz with b random bits
    """
    ...

def mpz_urandomb(state: Any, b: int) -> "mpz":
    """Generates a uniformly distributed random integer in the range [0, 2^b-1].

    Args:
        state: Random state object
        b: Number of bits

    Returns:
        A random mpz in the range [0, 2^b-1]
    """
    ...

def mpfr_grandom(state: Any) -> Tuple["mpfr", "mpfr"]:
    """Generates two random numbers with gaussian distribution."""
    ...

def mpfr_nrandom(state: Any) -> "mpfr":
    """Return a random number with gaussian distribution."""
    ...

def mpfr_random(state: Any) -> "mpfr":
    """Return uniformly distributed number between [0,1]."""
    ...

def mpc_random(state: Any) -> "mpc":
    """Return uniformly distributed number in the unit square [0,1]x[0,1]."""
    ...

# Other utility functions

def hamdist(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> int:
    """Computes the Hamming distance between x and y.

    The Hamming distance is the number of bit positions where x and y differ.

    Args:
        x: First value
        y: Second value

    Returns:
        The Hamming distance as an integer
    """
    ...

def popcount(x: Union[int, "mpz"]) -> int:
    """Counts the number of 1-bits in the binary representation of x.

    Args:
        x: The value to count bits in

    Returns:
        The number of 1-bits in x
    """
    ...

def xmpz_popcount(x: Union[int, "mpz"]) -> int:
    """Counts the number of 1-bits in the binary representation of x.

    Args:
        x: The value to count bits in

    Returns:
        The number of 1-bits in x
    """
    ...

def bit_mask(n: int) -> "mpz":
    """Creates a bit mask with n 1-bits.

    Args:
        n: Number of bits (must be >= 0)

    Returns:
        mpz value with the n lowest bits set to 1

    Raises:
        ValueError: If n < 0
    """
    ...

# MPFR specific functions
def const_log2(precision: int = 0) -> "mpfr":
    """Returns the natural logarithm of 2 with specified precision."""
    ...

def const_pi(precision: int = 0) -> "mpfr":
    """Returns the value of pi with specified precision."""
    ...

def const_euler(precision: int = 0) -> "mpfr":
    """Returns Euler's constant with specified precision."""
    ...

def const_catalan(precision: int = 0) -> "mpfr":
    """Returns Catalan's constant with specified precision."""
    ...

@overload
def log(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpfr", "mpc"]:
    """Computes the natural logarithm of x."""
    ...

@overload
def log(x: Union[int, float, "mpz", "mpfr", "mpq"], base: Union[int, float, "mpz", "mpfr"]) -> "mpfr":
    """Computes the logarithm of x to the specified base.

    If base is None, returns the natural logarithm.

    Args:
        x: The value to compute logarithm for (must be > 0)
        base: The logarithm base (must be > 0 and != 1)

    Returns:
        The logarithm as an mpfr object

    Raises:
        ValueError: If x <= 0 or base <= 0 or base == 1
    """
    ...

def exp(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpfr", "mpc"]:
    """Computes the exponential function e^x.

    Args:
        x: The exponent

    Returns:
        e^x as an mpfr object
    """
    ...

def sin(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpfr", "mpc"]:
    """Computes the sine of x.

    Args:
        x: Angle in radians

    Returns:
        sin(x) as an mpfr object
    """
    ...

def cos(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpfr", "mpc"]:
    """Computes the cosine of x.

    Args:
        x: Angle in radians

    Returns:
        cos(x) as an mpfr object
    """
    ...

def tan(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpfr", "mpc"]:
    """Computes the tangent of x.

    Args:
        x: Angle in radians

    Returns:
        tan(x) as an mpfr object
    """
    ...

def atan(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpfr", "mpc"]:
    """Computes the arctangent of x.

    Args:
        x: Value to compute arctangent for

    Returns:
        atan(x) as an mpfr object
    """
    ...

def atan2(y: Union[int, float, "mpz", "mpfr", "mpq"], x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Computes the two-argument arctangent of y/x.

    Args:
        y: The y-coordinate
        x: The x-coordinate

    Returns:
        atan2(y, x) as an mpfr object
    """
    ...

def sinh(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpfr", "mpc"]:
    """Computes the hyperbolic sine of x.

    Args:
        x: Value to compute hyperbolic sine for

    Returns:
        sinh(x) as an mpfr object
    """
    ...

def cosh(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpfr", "mpc"]:
    """Computes the hyperbolic cosine of x.

    Args:
        x: Value to compute hyperbolic cosine for

    Returns:
        cosh(x) as an mpfr object
    """
    ...

def tanh(x: Union[int, float, "mpz", "mpfr", "mpq", "mpc"]) -> Union["mpfr", "mpc"]:
    """Computes the hyperbolic tangent of x.

    Args:
        x: Value to compute hyperbolic tangent for

    Returns:
        tanh(x) as an mpfr object
    """
    ...

def atanh(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Computes the inverse hyperbolic tangent of x.

    Args:
        x: Value to compute inverse hyperbolic tangent for (|x| < 1)

    Returns:
        atanh(x) as an mpfr object

    Raises:
        ValueError: If |x| >= 1
    """
    ...

def asin(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Computes the arcsine of x.

    Args:
        x: Value to compute arcsine for (|x| <= 1)

    Returns:
        asin(x) as an mpfr object

    Raises:
        ValueError: If |x| > 1
    """
    ...

def acos(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Computes the arccosine of x.

    Args:
        x: Value to compute arccosine for (|x| <= 1)

    Returns:
        acos(x) as an mpfr object

    Raises:
        ValueError: If |x| > 1
    """
    ...

def asinh(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Computes the inverse hyperbolic sine of x.

    Args:
        x: Value to compute inverse hyperbolic sine for

    Returns:
        asinh(x) as an mpfr object
    """
    ...

def acosh(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Computes the inverse hyperbolic cosine of x.

    Args:
        x: Value to compute inverse hyperbolic cosine for (x >= 1)

    Returns:
        acosh(x) as an mpfr object

    Raises:
        ValueError: If x < 1
    """
    ...

def floor(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> Union["mpz", "mpfr"]:
    """Computes the floor of x (largest integer not greater than x).

    Args:
        x: Value to compute floor for

    Returns:
        floor(x) as mpz if x is integer-like, otherwise as mpfr
    """
    ...

def ceil(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> Union["mpz", "mpfr"]:
    """Computes the ceiling of x (smallest integer not less than x).

    Args:
        x: Value to compute ceiling for

    Returns:
        ceil(x) as mpz if x is integer-like, otherwise as mpfr
    """
    ...

def trunc(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> Union["mpz", "mpfr"]:
    """Truncates x towards zero.

    Args:
        x: Value to truncate

    Returns:
        trunc(x) as mpz if x is integer-like, otherwise as mpfr
    """
    ...

def round2(x: Union[int, float, "mpz", "mpfr", "mpq"], n: int = 0) -> "mpfr":
    """Rounds x to the nearest multiple of 2^n.

    Args:
        x: Value to round
        n: Determines the precision of rounding (defaults to 0)

    Returns:
        Rounded value as mpfr
    """
    ...

def round_away(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> Union["mpz", "mpfr"]:
    """Rounds x to the nearest integer, away from 0 in case of a tie.

    Args:
        x: Value to round

    Returns:
        Rounded value as mpz if x is integer-like, otherwise as mpfr
    """
    ...

def fmod(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Computes the floating-point remainder of x/y with the same sign as x.

    Args:
        x: Dividend
        y: Divisor

    Returns:
        Floating-point remainder as mpfr

    Raises:
        ZeroDivisionError: If y is 0
    """
    ...

def remainder(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Computes the IEEE remainder of x/y.

    Args:
        x: Dividend
        y: Divisor

    Returns:
        IEEE remainder as mpfr

    Raises:
        ZeroDivisionError: If y is 0
    """
    ...

def remquo(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"]) -> Tuple["mpfr", int]:
    """Computes the remainder and low bits of the quotient."""
    ...

def rint(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Rounds x to the nearest integer, using current rounding mode."""
    ...

def rint_ceil(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Rounds x to the nearest integer, rounding up."""
    ...

def rint_floor(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Rounds x to the nearest integer, rounding down"""
    ...

def rint_round(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Rounds x to the nearest integer, rounding away from 0 for ties."""
    ...

def rint_trunc(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Rounds x to the nearest integer, rounding towards zero."""
    ...

def root_of_unity(n: int, k: int) -> "mpc":
    """Return the n-th root of mpc(1) raised to the k-th power."""
    ...

def c_div(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> "mpz":
    """Return the quotient of x divided by y, rounded towards +Inf (ceiling rounding)."""
    ...

def c_div_2exp(x: Union[int, "mpz"], n: int) -> "mpz":
    """Returns the quotient of x divided by 2**n, rounded towards +Inf (ceiling rounding)."""
    ...

def c_divmod(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by y, quotient rounded towards +Inf (ceiling rounding)."""
    ...

def c_divmod_2exp(x: Union[int, "mpz"], n: int) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by 2**n, quotient rounded towards +Inf (ceiling rounding)"""
    ...

def c_mod(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> "mpz":
    """Return the remainder of x divided by y. The remainder will have the opposite sign of y."""
    ...

def c_mod_2exp(x: Union[int, "mpz"], n: int) -> "mpz":
    """Return the remainder of x divided by 2**n. The remainder will be negative."""
    ...

def f_div(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> "mpz":
    """Return the quotient of x divided by y, rounded towards -Inf (floor rounding)."""
    ...

def f_div_2exp(x: Union[int, "mpz"], n: int) -> "mpz":
    """Return the quotient of x divided by 2**n, rounded towards -Inf (floor rounding)."""
    ...

def f_divmod(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by y, quotient rounded towards -Inf (floor rounding)."""
    ...

def f_divmod_2exp(x: Union[int, "mpz"], n: int) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by 2**n, quotient rounded towards -Inf (floor rounding)."""
    ...

def f_mod(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> "mpz":
    """Return the remainder of x divided by y. The remainder will have the same sign as y."""
    ...

def f_mod_2exp(x: Union[int, "mpz"], n: int) -> "mpz":
    """Return remainder of x divided by 2**n. The remainder will be positive."""
    ...

def t_div(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> "mpz":
    """Return the quotient of x divided by y, rounded towards 0."""
    ...

def t_div_2exp(x: Union[int, "mpz"], n: int) -> "mpz":
    """Return the quotient of x divided by 2**n, rounded towards zero (truncation)."""
    ...

def t_divmod(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by y, quotient rounded towards zero (truncation)"""
    ...

def t_divmod_2exp(x: Union[int, "mpz"], n: int) -> Tuple["mpz", "mpz"]:
    """Return the quotient and remainder of x divided by 2**n, quotient rounded towards zero (truncation)."""
    ...

def t_mod(x: Union[int, "mpz"], y: Union[int, "mpz"]) -> "mpz":
    """Return the remainder of x divided by y. The remainder will have the same sign as x."""
    ...

def t_mod_2exp(x: Union[int, "mpz"], n: int) -> "mpz":
    """Return the remainder of x divided by 2**n. The remainder will have the same sign as x."""
    ...

def cbrt(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return the cube root of x."""
    ...

def digamma(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return digamma of x."""
    ...

def eint(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return exponential integral of x."""
    ...

def erf(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return error function of x."""
    ...

def erfc(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return complementary error function of x."""
    ...

def exp10(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return 10**x."""
    ...

def exp2(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return 2**x."""
    ...

def expm1(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return exp(x) - 1."""
    ...

def fmma(
    x: Union[int, float, "mpz", "mpfr", "mpq"],
    y: Union[int, float, "mpz", "mpfr", "mpq"],
    z: Union[int, float, "mpz", "mpfr", "mpq"],
    t: Union[int, float, "mpz", "mpfr", "mpq"],
) -> "mpfr":
    """Return correctly rounded result of (x * y) + (z * t)."""
    ...

def fmms(
    x: Union[int, float, "mpz", "mpfr", "mpq"],
    y: Union[int, float, "mpz", "mpfr", "mpq"],
    z: Union[int, float, "mpz", "mpfr", "mpq"],
    t: Union[int, float, "mpz", "mpfr", "mpq"],
) -> "mpfr":
    """Return correctly rounded result of (x * y) - (z * t)."""
    ...

def frexp(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> Tuple[int, "mpfr"]:
    """Return a tuple containing the exponent and mantissa of x."""
    ...

def fsum(iterable: Iterator[Union[int, float, "mpz", "mpfr", "mpq"]]) -> "mpfr":
    """Return an accurate sum of the values in the iterable."""
    ...

def gamma(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return gamma of x."""
    ...

def gamma_inc(a: Union[int, float, "mpz", "mpfr", "mpq"], x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return (upper) incomplete gamma of a and x."""
    ...

def hypot(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return square root of (x**2 + y**2)."""
    ...

def j0(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return first kind Bessel function of order 0 of x."""
    ...

def j1(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return first kind Bessel function of order 1 of x."""
    ...

def jn(n: int, x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return the first kind Bessel function of order n of x."""
    ...

def lgamma(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> Tuple["mpfr", int]:
    """Return a tuple containing the logarithm of the absolute value of gamma(x) and the sign of gamma(x)"""
    ...

def li2(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return real part of dilogarithm of x."""
    ...

def lngamma(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return natural logarithm of gamma(x)."""
    ...

def log1p(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return natural logarithm of (1+x)."""
    ...

def maxnum(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return the maximum number of x and y."""
    ...

def minnum(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return the minimum number of x and y."""
    ...

def reldiff(x: Union[int, float, "mpz", "mpfr", "mpq"], y: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return the relative difference between x and y."""
    ...

def root(x: Union[int, float, "mpz", "mpfr", "mpq"], n: int) -> "mpfr":
    """Return n-th root of x."""
    ...

def rootn(x: Union[int, float, "mpz", "mpfr", "mpq"], n: int) -> "mpfr":
    """Return n-th root of x."""
    ...

def sec(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return secant of x; x in radians."""
    ...

def sech(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return hyperbolic secant of x."""
    ...

def sin_cos(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> Tuple["mpfr", "mpfr"]:
    """Return a tuple containing the sine and cosine of x; x in radians."""
    ...

def sinh_cosh(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> Tuple["mpfr", "mpfr"]:
    """Return a tuple containing the hyperbolic sine and cosine of x."""
    ...

def y0(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return second kind Bessel function of order 0 of x."""
    ...

def y1(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return second kind Bessel function of order 1 of x."""
    ...

def yn(n: int, x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return the second kind Bessel function of order n of x."""
    ...

def zeta(x: Union[int, float, "mpz", "mpfr", "mpq"]) -> "mpfr":
    """Return Riemann zeta of x."""
    ...

def qdiv(x: Union[int, "mpz", "mpq"], y: Union[int, "mpz", "mpq"] = 1) -> Union["mpz", "mpq"]:
    """Return x/y as mpz if possible, or as mpq if x is not exactly divisible by y."""
    ...

def ieee(size: int, subnormalize: bool = True) -> context:
    """Return a new context corresponding to a standard IEEE floating-point format."""
    ...

def local_context(**kwargs: Any) -> context:
    """Return a new context for controlling gmpy2 arithmetic, based either on the current context or
    on a ctx value."""
    ...

def set_context(context: context) -> None:
    """Activate a context object controlling gmpy2 arithmetic."""
    ...

# Constants (should be ALL_CAPS to follow convention)
#  (These are placeholders. In reality, they are likely implemented differently)
MACHINE_BITS: int = 64  # Example:  Set to a reasonable default, adjust in tests if needed.

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
    "context",
    "const_context",
    # Core arithmetic functions
    "add",
    "sub",
    "mul",
    "div",
    "divmod",
    "mod",
    "sqrt",
    "isqrt",
    "isqrt_rem",
    "square",
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
    "maxnum",
    "minnum",
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
    "xmpz_popcount",
    "bit_mask",
    # MPFR constants and functions
    "const_log2",
    "const_pi",
    "const_euler",
    "const_catalan",
    "log",
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
    # Library information
    "version",
    "mp_version",
    "get_cache",
    "set_cache",
    "get_max_precision",
    "set_max_precision",
    "get_minprec",
    "get_maxprec",
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
    "MACHINE_BITS",
]
