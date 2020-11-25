import pytest
from src.main.quantity_converter.quantity_conversion import QuantityMeasurer


@pytest.fixture
def quantity_converter_object():
    quantity_converter = QuantityMeasurer()
    return quantity_converter
