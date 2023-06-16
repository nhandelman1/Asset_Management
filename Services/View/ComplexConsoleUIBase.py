from abc import abstractmethod
from Services.View.SimpleConsoleUIBase import SimpleConsoleUIBase
from Services.View.ComplexServiceViewBase import ComplexServiceViewBase


class ComplexConsoleUIBase(SimpleConsoleUIBase, ComplexServiceViewBase):
    """ Abstract base view class for complex service data display and input through the console

    This is an intermediary base class that implements functions in ComplexServiceViewBase that are common to any
    subclasses of this class.
    """

    @abstractmethod
    def __init__(self):
        pass

    def input_values_for_notes(self, notes_list):
        el_dict = {}
        for d in notes_list:
            note_type = d["note_type"]
            print("\n" + note_type + "\n" + d["note"])
            inp = input("Input value for " + note_type + ": ")
            el_dict[note_type] = inp

        return el_dict