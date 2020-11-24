from abc import ABC , abstractmethod


class IQuantityConverter(ABC):
    @abstractmethod
    def meter_to_cm_length(self, input_length):
        pass

    @abstractmethod
    def meter_to_km_length(self, input_length):
        pass

    @abstractmethod
    def gram_to_kg_weight(self, input_weight):
        pass