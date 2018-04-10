import numpy as np

from pint import UnitRegistry
units = UnitRegistry()


def is_pint_quantity(some_type):
    return some_type is units.Quantity


def is_pint_quantity_by_string(some_type):
    return str(some_type) == "<class " \
                             "'pint.quantity.build_quantity_class.<locals" \
                             ">.Quantity'>"


def is_rank_one_tensor(some_collection):
    return len(np.shape(some_collection)) == 1