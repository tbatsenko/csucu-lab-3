# File: testing.py


from agent import Agent
from funcs import get_valid_input


def if_display():
    """
    This function asks user if they want to see current properties.
    :return: (bool) - True if user response is positive, else - False
    """
    resp = get_valid_input("Do you want to see current properties?",
                           ("yes", "no"))
    if resp == "yes":
        agent.display_properties()
    else:
        resp = get_valid_input("To quit enter 'exit',"
                               " otherwise you'll start from the beginning",
                               "exit")
        if resp == "exit":
            return False
    return True


agent = Agent()
print("============   Welcome to the world of real estate!   ============")
while True:
    print()
    resp = get_valid_input("Do you want to add a new property?", ("yes", "no"))
    if resp == "yes":
        agent.add_property()
    else:
        if not if_display():
            break
