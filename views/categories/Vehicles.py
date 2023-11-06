from abc import ABC, abstractmethod
from datetime import datetime, timedelta


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
    def booking_limit(self, booking_date) -> bool:
        """
        This function is used to check if booking date is still within allowed limit

        :limit: parameter represents the limit of booking as in days (default: days)
        """
        pass

    @abstractmethod
    def get_passengers(self) -> int:
        pass

    @abstractmethod
    def get_booking_duration(self, limit: str = "day") -> int:
        pass


class SmallCars(Vehicle):
    __passengers: int = 4
    __booking_duration_in_days: int = 7

    def passenger_limits(self, people: int) -> bool:
        return people <= self.__passengers

    def get_passengers(self) -> int:
        return self.__passengers

    def get_booking_duration(self, limit: str = "day") -> int:
        if limit == "day":
            return self.__booking_duration_in_days

    def booking_limit(self, booking_date) -> bool:
        date_from_now: datetime = datetime.now() + timedelta(
            days=self.__booking_duration_in_days
        )
        return date_from_now >= booking_date


class FamilyCars(Vehicle):
    __passengers: int = 7
    __booking_duration_in_days: int = 7

    def passenger_limits(self, people: int) -> bool:
        return people <= self.__passengers

    def get_passengers(self) -> int:
        return self.__passengers

    def get_booking_duration(self, limit: str = "day") -> int:
        if limit == "day":
            return self.__booking_duration_in_days

    def booking_limit(self, booking_date) -> bool:
        date_from_now: datetime = datetime.now() + timedelta(
            days=self.__booking_duration_in_days
        )
        return date_from_now >= booking_date


class Vans(Vehicle):
    __passengers: int = 2
    __booking_duration_in_days: int = 7

    def passenger_limits(self, people: int) -> bool:
        return people <= self.__passengers

    def get_passengers(self) -> int:
        return self.__passengers

    def get_booking_duration(self, limit: str = "day") -> int:
        if limit == "day":
            return self.__booking_duration_in_days

    def booking_limit(self, booking_date) -> bool:
        date_from_now: datetime = datetime.now() + timedelta(
            days=self.__booking_duration_in_days
        )
        return date_from_now >= booking_date
