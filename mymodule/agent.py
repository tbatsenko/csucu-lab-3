# File: agent.py
from funcs import get_valid_input
from deals import *


class Agent:
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        """
        This method initializes an instance of Agent Class.
        Is called automatically.
        """
        self.property_list = []

    def display_properties(self):
        """
        This calls a method display() for each item in self.property_list.
        """
        for prop in self.property_list:
            prop.display()

    def add_property(self):
        """
        This method adds a new item to attribute self.property_list.
        """
        property_type = get_valid_input("What type of property? ",
                                        ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ",
                                       ("purchase", "rental")).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
