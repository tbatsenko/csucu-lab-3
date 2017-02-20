# File: deals.py
from apartment import Apartment
from house import House
from purchase import Purchase
from rental import Rental


class HouseRental(Rental, House):
    @staticmethod
    def prompt_init():
        """
        This method calls the parent methods prompt_init(), which
        asks user to initialize appropriate instances of classes House
        and Rental.
        :return: an instance which represents house for rent - inherits
        from House and Rental.
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init


class ApartmentRental(Rental, Apartment):
    @staticmethod
    def prompt_init():
        """
        This method calls the parent methods prompt_init(), which
        asks user to initialize appropriate instances of classes Apartment
        and Rental.
        :return: an instance which represents apartment for rent - inherits
        from Apartment and Rental.
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init


class ApartmentPurchase(Purchase, Apartment):
    @staticmethod
    def prompt_init():
        """
        This method calls the parent methods prompt_init(), which
        asks user to initialize appropriate instances of classes Apartment
        and Purchase.
        :return: an instance which represents an apartment for purchasing -
        inherits from Apartment and Purchase.
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class HousePurchase(Purchase, House):
    @staticmethod
    def prompt_init():
        """
        This method calls the parent methods prompt_init(), which
        asks user to initialize appropriate instances of classes House
        and Purchase.
        :return: an instance which represents house for rent - inherits
        from House and Purchase.
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
