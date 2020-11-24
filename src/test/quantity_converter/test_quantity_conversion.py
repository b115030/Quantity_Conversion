import pytest


@pytest.mark.parametrize("input, output", [(20, 2000), (2, 200), (3, 300), (45, 4500), (35, 3500)])
def test_length_meter_to_centimeter_conversion(input, output, quality_converter):
    result = quality_converter.meter_to_cm_length(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(10, .01), (2456, 2.456), (6000, 6), (5000, 5)])
def test_length_meter_to_kilometer_conversion(input, output, quality_converter):
    result = quality_converter.meter_to_km_length(input)
    assert result == output


def test_given_wrong_input_in_meter_to_kilometer_should_raise_exception(quality_converter):
    quality_converter.meter_to_cm_length('sdijjkl')
    assert pytest.raises(TypeError)


@pytest.mark.parametrize("input, output", [(5000, 5), (2000, 2), (56000, 56), (8658, 8.658)])
def test_weight_grams_to_kilograms_conversion(input, output, quality_converter):
    result = quality_converter.gram_to_kg_weight(input)
    assert result == output


def test_given_wrong_input_in_meter_to_kilometer_should_raise_exception(quality_converter):
    quality_converter.meter_to_cm_length('dgfhjfjhshj')
    assert pytest.raises(TypeError)


def test_given_wrong_input_in_grams_to_kilograms_should_raise_exception(quality_converter):
    quality_converter.meter_to_cm_length('848921748948795542456245^%&%&^%%%')
    assert pytest.raises(TypeError)
