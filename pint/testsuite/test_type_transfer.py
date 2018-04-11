from pint import UnitRegistry
units = UnitRegistry()

from .target_type_transfer import is_pint_quantity
from .target_type_transfer import is_pint_quantity_by_string


def test_type_locally():
    """If I have a quantity foo, I can test its type in this module by the
    normal, expected method."""
    foo = units.Quantity(42, 'm/s')
    assert isinstance(foo, units.Quantity)


def test_type_other_module():
    """If I have a quantity foo and want to test its type in another module (
    say a target module for the tests I'm writing here), I can't test it by
    the normal method, the test inexplicably fails. Perhaps the reason is that
    types imported into this module are different in an invisible way from
    the same types imported into the other module. If that's the case,
    I need some way to test the types of Pint quantities inside and outside
    collections."""
    foo = units.Quantity(42, 'm/s')
    assert is_pint_quantity(foo)


def test_type_other_module_workaround():
    """If I have a quantity foo and want to test its type in another module
    (say a target module for the tests I'm writing here), I can't test it by
    the normal method, the test inexplicably fails. A workaround is to convert
    the type into a string and test that string in the other module. It's not a
    robust workaround, however, as it depends on changeable details of the
    implementation."""
    foo = units.Quantity(42, 'm/s')
    assert is_pint_quantity_by_string(foo)

