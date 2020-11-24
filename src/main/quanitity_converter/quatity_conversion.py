import logging
from src.main.quanitity_converter.IQuantityConverter import IQuantityConverter

logging.basicConfig(filename='quantity_convert.log', level=logging.DEBUG,
                    format='%(name)s | %(levelname)s | %(message)s')


class QuantityMeasurementSystem(IQuantityConverter):

    def __init__(self):
        self.M_TO_CM = 100
        self.M_TO_KM = .001
        self.G_TO_KG = .001

    def meter_to_cm_length(self, length_input):
        """

        :param length_input:  length in meters
        :return: length in centimeters or exception
        """
        try:
            if not isinstance(length_input, (float, int)):
                logging.debug("here!")
                logging.exception('Exception: wrong input type')
                raise TypeError("Exception: wlrong input type")
            centimeter_length = length_input * self.M_TO_CM
            logging.debug('meter to centimeter: {}'.format(centimeter_length))
            return centimeter_length
        except TypeError:
            logging.exception('Exception: wrong input type')
            print("enter a number")
        except ValueError:
            logging.exception('Exception: there is a problem with the content of the object you tried to assign the '
                              'value to. ')
            print("enter a number")

    def meter_to_km_length(self, length_input):
        """

        :param length_input:  length in meters
        :return: length in kilometers or exception
        """
        try:
            kilometer_length = length_input * self.M_TO_KM
            logging.debug('meter to kilometer: {}'.format(kilometer_length))
            return kilometer_length
        except TypeError:
            logging.exception('Exception: wrong input type')
            print("enter a number")
        except ValueError:
            logging.exception('Exception: there is a problem with the content of the object you tried to assign the '
                              'value to. ')
            print("enter a number")

    def gram_to_kg_weight(self, weight_input):
        """

        :param weight_input: weight in grams
        :return: weight in kilograms or exception
        """
        try:
            kilogram_weight = weight_input * self.G_TO_KG
            logging.debug('gram to kilogram: {}'.format(kilogram_weight))
            return kilogram_weight
        except TypeError:
            logging.exception('Exception:wrong input type')
            print("enter a number")
        except ValueError:
            logging.exception('Exception: there is a problem with the content of the object you tried to assign the '
                              'value to. ')
            print("enter a number")
