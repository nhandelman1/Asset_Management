from abc import ABC, abstractmethod
from Utilities.View.UtilityViewBase import UtilityViewBase


class PSEGViewBase(UtilityViewBase, ABC):
    """ Abstract base view class for PSEG data display and input """

    @abstractmethod
    def __init__(self):
        super().__init__()

    @staticmethod
    @abstractmethod
    def input_estimation_data(start_date, end_date):
        """ Input estimation data that isn't available elsewhere for electric bill estimation

        Args:
            start_date (datetime.date): start date for estimation data
            end_date (datetime.date): end date for estimation data

        Returns:
            dict with keys "eh_kwh"
        """
        raise NotImplementedError("input_estimation_data() not implemented by subclass")