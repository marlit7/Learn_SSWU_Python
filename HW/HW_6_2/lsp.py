# Liskov
#
# class Vehicle:
#    def engine(self) -> None:
#        pass
#
#    def start_engine(self) -> None:
#        self.engine()
#
# class Car(Vehicle):
#    """A demo Car Vehicle class"""
#    def start_engine(self) -> None:
#        print("Let's go")
#
#
# class Bicycle(Vehicle):
#    """A demo Bicycle Vehicle class"""
#    def start_engine(self) -> None:
#        print("I don't have an engine")


from abc import ABC, abstractmethod

class Vehicle(ABC):
    pass

class EngineVehicle(Vehicle):
    @abstractmethod
    def start_engine(self) -> None:
        pass

class Car(EngineVehicle):
    def start_engine(self) -> None:
        print("Let's go")

class Bicycle(Vehicle):
    def ride(self) -> None:
        print("Pedaling the bicycle")