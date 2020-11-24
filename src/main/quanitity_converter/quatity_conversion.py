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

        :param other_class_to_compare: class/Enum to compare with
        :return: True if the class types are same else False
        :rtype: bool
        """
        if self.__unit.__class__ == other_class_to_compare.__unit.__class__:
            if self.__unit.__class__.convert(self.__unit,
                                             self.__value) == other_class_to_compare.__unit.__class__.convert(
                other_class_to_compare.__unit,
                other_class_to_compare.__value):
                return True
        return False

    def add(self, other_class_to_compare):
        """

        :param other_class_to_compare: class/Enum to add with
        :return: sum of values if both are from the same class
        :rtype: float
        """
        if self.__unit.__class__ == other_class_to_compare.__unit.__class__:
            return self.__unit.__class__.convert(self.__unit,
                                                 self.__value) + other_class_to_compare.__unit.__class__.convert(
                other_class_to_compare.__unit, other_class_to_compare.__value)
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

        :param value:
        :return: converted value
        """
        return self.unit * value
