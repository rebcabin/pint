import numpy as np

from pint import UnitRegistry
units = UnitRegistry()


def is_pint_quantity(some_object):
    inspect_in_debugger = isinstance(some_object, units.Quantity)
    return isinstance(some_object, units.Quantity)


def is_pint_quantity_by_string(some_object):
    return str(type(some_object)) == \
           "<class 'pint.quantity.build_quantity_class.<locals>.Quantity'>"


def is_rank_one_tensor(some_collection):
    return len(np.shape(some_collection)) == 1
