# File: rental.py
from funcs import get_valid_input


class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        """
        This method initializes a new Rental instance, which inherits from
        object when calls super().__init__(*kwargs) method.
        :param furnished: represents furnished state of instance.
        :param utilities: represents utilities of instance.
        :param rent: represents amount of rent to pay for instance.
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        (self) -> (None)
        This method calls a parent class method display and then
        prints out a Rental instance details specific for the Rental class.
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    @staticmethod
    def prompt_init():
        """
        This method asks user to enter appropriate info for Rental instance,
        which characterizes it - rent, utilities and furnished state.
        :return: (dict{(str): (str)})
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))
