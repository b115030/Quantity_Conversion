import pytest
from src.main.quanitity_converter.quatity_conversion import *


@pytest.mark.parametrize("input_from, from_value, input_to, to_value, expected",
                         [(Lengths.FEET, 3.0, Lengths.YARD, 1.0, True), (Lengths.FEET, 1.0, Lengths.YARD, 1.0, False),
                          (Lengths.INCH, 1.0, Lengths.YARD, 1.0, False), (Lengths.CM, 1.0, Lengths.M, 1.0, False),
                          (Lengths.FEET, 1.0, Lengths.CM, 30.0, True), (Lengths.YARD, 1.0, Lengths.CM, 90.0, True)])
def test_given_lengths_in_different_units_of_length_if_equal_in_value_should_return_true(input_from, from_value,
                                                                                         input_to,
                                                                                         to_value, expected):
    first_unit = QuantityMeasurer(input_from, from_value)
    second_unit = QuantityMeasurer(input_to, to_value)
    assert first_unit.compare(second_unit) == expected


@pytest.mark.parametrize("input_from, from_value, input_to, to_value, expected",
                         [(Lengths.INCH, 3.0, Lengths.INCH, 1.0, 4.0), (Lengths.INCH, 2.0, Lengths.FEET, 1.0, 14.0),
                          (Lengths.INCH, 2.0, Lengths.CM, 2.5, 3.0)])
def test_given_lengths_in_different_units_of_length_should_return_sum(input_from, from_value, input_to,
                                                                      to_value, expected):
    first_unit = QuantityMeasurer(input_from, from_value)
    second_unit = QuantityMeasurer(input_to, to_value)
    assert first_unit.add(second_unit) == expected


@pytest.mark.parametrize("input_from, from_value, input_to, to_value, expected",
                         [(Volumes.GALLON, 1.0, Volumes.LITRE, 3.78, True),
                          (Volumes.LITRE, 1.0, Volumes.ML, 1000.0, True),
                          (Volumes.LITRE, 1.0, Volumes.LITRE, 1.0, True)])
def test_given_lengths_in_different_units_of_volume_if_equal_in_value_should_return_true(input_from, from_value,
                                                                                         input_to,
                                                                                         to_value, expected):
    first_unit = QuantityMeasurer(input_from, from_value)
    second_unit = QuantityMeasurer(input_to, to_value)
    assert first_unit.compare(second_unit) == expected


@pytest.mark.parametrize("input_from, from_value, input_to, to_value, expected",
                         [(Volumes.LITRE, 3.78, Volumes.GALLON, 1.0, 7.56),
                          (Volumes.LITRE, 1.0, Volumes.ML, 1000.0, 2.0),
                          (Volumes.LITRE, 6.5, Volumes.ML, 5000.0, 11.5)])
def test_given_lengths_in_different_units_of_volume_should_return_sum(input_from, from_value, input_to,
                                                                      to_value, expected):
    first_unit = QuantityMeasurer(input_from, from_value)
    second_unit = QuantityMeasurer(input_to, to_value)
    assert first_unit.add(second_unit) == expected


@pytest.mark.parametrize("input_from, from_value, input_to, to_value, expected",
                         [(Weights.KG, 1.0, Weights.KG, 1.0, True),
                          (Weights.KG, 1.0, Weights.GRAMS, 1000.0, True),
                          (Weights.TONNE, 1.0, Weights.KG, 1000.0, True)])
def test_given_lengths_in_different_units_of_weight_if_equal_in_value_should_return_true(input_from, from_value,
                                                                                         input_to,
                                                                                         to_value, expected):
    first_unit = QuantityMeasurer(input_from, from_value)
    second_unit = QuantityMeasurer(input_to, to_value)
    assert first_unit.compare(second_unit) == expected
