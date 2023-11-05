from abc import ABC, abstractmethod


# Vehicle Class represents an interface to enforce rules upon certain vehicle categories to better organize code.
class Vehicle(ABC):
    passengers: int

    # method that checks if passengers does not cross limit, using decorated enforces the method to be implemented to subclasses.
    @abstractmethod
    def passenger_limits(self, people: int) -> bool:
        """
        This function is used to check input with limits of the Vehicle type

        :passengers: Is number of passengers input

        :return: returns True if checks are passed or False if fails a check
        """
        pass

class SmallCars(Vehicle):
    passengers: int = 4

    def passenger_limits(self, people: int) -> bool:
        return people <= self.passengers

class FamilyCars(Vehicle):
    passengers: int = 7

    def passenger_limits(self, people: int) -> bool:
        return people <= self.passengers

class Vans(Vehicle):
    passengers: int = 2

    def passenger_limits(self, people: int) -> bool:
        return people <= self.passengers