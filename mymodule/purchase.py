# File: purchase.py


class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        """
        This method initializes a new Purchase instance, which inherits from
        object when calls super().__init__(*kwargs) method.
        :param price: represents price of instance.
        :param utilities: represents taxes of instance.
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        (self) -> (None)
        This method calls a parent class method display and then
        prints out a Purchase instance details specific for the Purchase class.
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    @staticmethod
    def prompt_init():
        """
        This method asks user to enter appropriate info for Purchase instance,
        which characterizes it - price and taxes.
        :return: (dict{(str): (str)})
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))
