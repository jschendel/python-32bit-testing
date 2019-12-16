import numbers

# for i in range(-2, 2):
#     val = 2**61 + i
#     val_str = f"2**61 {'+' if i >= 0 else '-'} {abs(i)}"
#     print(val_str, val, hash(val))

low = 0
high = 2 ** 61
while high - low > 1:
    mid = (high + low) // 2
    if mid == hash(mid):
        low = mid
    else:
        high = mid

print(low, high)


# -----------------------------------------------------------------------------
# Implementation of NA singleton


def _create_binary_propagating_op(name, divmod=False):

    def method(self, other):
        if (other is C_NA or isinstance(other, str)
                or isinstance(other, numbers.Number)):
            if divmod:
                return NA, NA
            else:
                return NA

        return NotImplemented

    method.__name__ = name
    return method


def _create_unary_propagating_op(name):
    def method(self):
        return NA

    method.__name__ = name
    return method


class C_NAType:
    pass


class NAType(C_NAType):
    """
    NA ("not available") missing value indicator.

    .. warning::

       Experimental: the behaviour of NA can still change without warning.

    .. versionadded:: 1.0.0

    The NA singleton is a missing value indicator defined by pandas. It is
    used in certain new extension dtypes (currently the "string" dtype).
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if NAType._instance is None:
            NAType._instance = C_NAType.__new__(cls, *args, **kwargs)
        return NAType._instance

    def __repr__(self) -> str:
        return "NA"

    def __str__(self) -> str:
        return "NA"

    def __bool__(self):
        raise TypeError("boolean value of NA is ambiguous")

    def __hash__(self):
        return 2 ** 61 - 1

    # Binary arithmetic and comparison ops -> propagate

    __add__ = _create_binary_propagating_op("__add__")
    __radd__ = _create_binary_propagating_op("__radd__")
    __sub__ = _create_binary_propagating_op("__sub__")
    __rsub__ = _create_binary_propagating_op("__rsub__")
    __mul__ = _create_binary_propagating_op("__mul__")
    __rmul__ = _create_binary_propagating_op("__rmul__")
    __matmul__ = _create_binary_propagating_op("__matmul__")
    __rmatmul__ = _create_binary_propagating_op("__rmatmul__")
    __truediv__ = _create_binary_propagating_op("__truediv__")
    __rtruediv__ = _create_binary_propagating_op("__rtruediv__")
    __floordiv__ = _create_binary_propagating_op("__floordiv__")
    __rfloordiv__ = _create_binary_propagating_op("__rfloordiv__")
    __mod__ = _create_binary_propagating_op("__mod__")
    __rmod__ = _create_binary_propagating_op("__rmod__")
    __divmod__ = _create_binary_propagating_op("__divmod__", divmod=True)
    __rdivmod__ = _create_binary_propagating_op("__rdivmod__", divmod=True)
    # __lshift__ and __rshift__ are not implemented

    __eq__ = _create_binary_propagating_op("__eq__")
    __ne__ = _create_binary_propagating_op("__ne__")
    __le__ = _create_binary_propagating_op("__le__")
    __lt__ = _create_binary_propagating_op("__lt__")
    __gt__ = _create_binary_propagating_op("__gt__")
    __ge__ = _create_binary_propagating_op("__ge__")

    # Unary ops

    __neg__ = _create_unary_propagating_op("__neg__")
    __pos__ = _create_unary_propagating_op("__pos__")
    __abs__ = _create_unary_propagating_op("__abs__")
    __invert__ = _create_unary_propagating_op("__invert__")

    # pow has special
    def __pow__(self, other):
        if other is C_NA:
            return NA
        elif isinstance(other, numbers.Number):
            if other == 0:
                # returning positive is correct for +/- 0.
                return type(other)(1)
            else:
                return NA

        return NotImplemented

    def __rpow__(self, other):
        if other is C_NA:
            return NA
        elif isinstance(other, numbers.Number):
            if other == 1 or other == -1:
                return other
            else:
                return NA

        return NotImplemented

    # Logical ops using Kleene logic

    def __and__(self, other):
        if other is False:
            return False
        elif other is True or other is C_NA:
            return NA
        else:
            return NotImplemented

    __rand__ = __and__

    def __or__(self, other):
        if other is True:
            return True
        elif other is False or other is C_NA:
            return NA
        else:
            return NotImplemented

    __ror__ = __or__

    def __xor__(self, other):
        if other is False or other is True or other is C_NA:
            return NA
        return NotImplemented

    __rxor__ = __xor__


C_NA = NAType()   # C-visible
NA = C_NA         # Python-visible

print("-" * 50)
print("2 ** 61 - 1", hash(2 ** 61 - 1))
print(str(NA), hash(NA))
print({NA, hash(NA)})
