import pytest
from src.main.quanitity_converter.quatity_conversion import QuantityMeasurementSystem


@pytest.fixture
def quality_converter():
    quantity_measurement_system = QuantityMeasurementSystem()
    return quantity_measurement_system