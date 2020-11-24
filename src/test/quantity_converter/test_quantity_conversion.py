import pytest
from src.main.quanitity_converter.quatity_conversion import *


@pytest.mark.parametrize("input_from, from_value, input_to, to_value, expected",
                         [(Lengths.FEET, 3.0, Lengths.YARD, 1.0, True), (Lengths.FEET, 1.0, Lengths.YARD, 1.0, False),
                          (Lengths.INCH, 1.0, Lengths.YARD, 1.0, False), (Lengths.CM, 1.0, Lengths.M, 1.0, False)])
def test_given_lengths_in_different_units_(input_from, from_value, input_to, to_value, expected):
    feet = QuantityMeasurer(input_from, from_value)
    yard = QuantityMeasurer(input_to, to_value)
    assert feet.compare(yard) == expected
