import logging
import enum

logging.basicConfig(filename='quantity_convert.log', level=logging.DEBUG,
                    format='%(name)s | %(levelname)s | %(message)s')


class QuantityMeasurer:
    """
    Methods:
        add
        compare
    """

    def __init__(self, unit, value):
        self.__value = value
        self.__unit = unit

    def __eq__(self, other_class_to_compare):
        if isinstance(other_class_to_compare, QuantityMeasurer):
            return self.__value == other_class_to_compare.__value
        return False

    def compare(self, other_class_to_compare):
        """
        comparing units

        :param other_class_to_compare: class/Enum to compare with
        :return: True if the class types are same else False
        :rtype: bool
        """
        logging.DEBUG("compare method")
        if self.__unit.__class__ == other_class_to_compare.__unit.__class__:
            if self.__unit.__class__.convert(self.__unit,
                                             self.__value) == other_class_to_compare.__unit.__class__.convert(
                other_class_to_compare.__unit,
                other_class_to_compare.__value):
                return True
        return False


def add(self, other_unit_to_add):
    """
    adding units

    :param other_unit_to_add: class/Enum to add with
    :return: sum of values if both are from the same class
    :rtype: float
    """
    logging.DEBUG("add method")
    if self.__unit.__class__ == other_unit_to_add.__unit.__class__:
        return self.__unit.__class__.convert(self.__unit,
                                             self.__value) + other_unit_to_add.__unit.__class__.convert(
            other_unit_to_add.__unit, other_unit_to_add.__value)
    return 0


class Lengths(enum.Enum):
    """

    Enum: for lengths
    """
    FEET = 12.0
    INCH = 1.0
    YARD = 36.0
    CM = 0.4
    M = 39.4

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        """
        converting into units of lengths

        :param value: value to convert
        :return: converted value
        """
        return self.unit * value


class Volumes(enum.Enum):
    """

    Enum: for Volumes
    """
    LITRE = 1.0
    GALLON = 3.78
    ML = 0.001

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        """

        :param value: value to convert
        :return: converted value
        """
        return self.unit * value


class Weights(enum.Enum):
    """

    Enum: for Volumes
    """
    KG = 1.0
    GRAMS = 0.001
    TONNE = 1000

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        """

        :param value: value to convert
        :return: converted value
        """
        logging.DEBUG("convert method")
        return self.unit * value


class Temperature(enum.Enum):
    celsius = 1.8
    fahrenheit = 1

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        if self == Temperature.celsius:
            return self.unit * value + 32
        else:
            return self.unit * value
