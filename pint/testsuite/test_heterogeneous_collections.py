import numpy as np

from pint import UnitRegistry
units = UnitRegistry()
Q = units.Quantity

from .target_type_transfer import is_rank_one_tensor


def test_heterogenous_units():
    """Trying to write a test in another file that a list of quantities with
    heterogenous types has rank 1 as a tensor, that is, is not nested. The
    obvious test against the 'shape' tuple works locally but not remotely"""
    mags = [42., 17., 77., -19]
    uoms = ['joule second', 'kg m^2 / s', 'm / s', 'candela']

    assert (len(mags) == len(uoms))
    assert (len(mags) == 4)
    assert np.shape(mags) == (4,)
    assert np.shape(uoms) == (4,)

    hetero = list(map(units.Quantity, mags, uoms))
    assert type(hetero) is list
    assert type(hetero[0]) is units.Quantity

    # Local test for rank one as a tensor
    assert len(np.shape(hetero)) == 1

    # Transferred test for rank one tensor; comment this out to get a pass.
    # Fails with AttributeError: 'list' object has no attribute 'shape'
    assert is_rank_one_tensor(hetero)
