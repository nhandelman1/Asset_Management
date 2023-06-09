import os
from Services.View.SimpleConsoleUIBase import SimpleConsoleUIBase
from Services.Mortgage.View.MortgageViewBase import MortgageViewBase


class MSConsoleUI(SimpleConsoleUIBase, MortgageViewBase):
    """ Implementation of SimpleServiceViewBase for use with Morgan Stanley mortgage console UI """

    def __init__(self):
        super().__init__()

    def input_read_new_bill(self):
        print("\nSave mortgage bill to " + str(os.getenv("FI_MORGANSTANLEY_DIR")) + " directory.")
        filename = input("Enter mortgage bill file name (include extension): ")

        return filename