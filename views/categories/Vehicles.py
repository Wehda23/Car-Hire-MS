from abc import ABC, abstractmethod


# Vehicle Class represents an interface to enforce rules upon certain vehicle categories to better organize code.
class Vehicle(ABC):
    __passengers: int
    __booking_duration_in_days: int

    # method that checks if passengers does not cross limit, using decorated enforces the method to be implemented to subclasses.
    @abstractmethod
    def passenger_limits(self, people: int) -> bool:
        """
        This function is used to check input with limits of the Vehicle type

        :passengers: Is number of passengers input

        :return: returns True if checks are passed or False if fails a check
        """
        pass

    @abstractmethod
    def get_passengers(self):
        pass
    
    @abstractmethod
    def get_booking_duration(self,limit: str = 'day'):
        pass
        

class SmallCars(Vehicle):
    __passengers: int = 4
    __booking_duration_in_days: int = 7

    def passenger_limits(self, people: int) -> bool:
        return people <= self.__passengers
    
    def get_passengers(self):
        return self.__passengers
    
    def get_booking_duration(self,limit: str = 'day'):
        if limit == 'day':
            return self.__booking_duration_in_days
        

class FamilyCars(Vehicle):
    __passengers: int = 7
    __booking_duration_in_days: int = 7

    def passenger_limits(self, people: int) -> bool:
        return people <= self.__passengers

    def get_passengers(self):
        return self.__passengers
    
    def get_booking_duration(self,limit: str = 'day'):
        if limit == 'day':
            return self.__booking_duration_in_days
        
class Vans(Vehicle):
    __passengers: int = 2
    __booking_duration_in_days: int = 7

    def passenger_limits(self, people: int) -> bool:
        return people <= self.__passengers
    
    def get_passengers(self):
        return self.__passengers
    
    def get_booking_duration(self,limit: str = 'day'):
        if limit == 'day':
            return self.__booking_duration_in_days