import datetime
import pandas as pd
from decimal import Decimal
from typing import Optional
from Database.POPO.SimpleServiceBillDataBase import SimpleServiceBillDataBase
from Database.POPO.RealPropertyValues import RealPropertyValues


class DepreciationBillData(SimpleServiceBillDataBase):
    """ Actual bill data for depreciation items

    Attributes:
        see init docstring for attributes (db_dict is not kept as an attribute)
    """
    def __init__(self, real_estate, service_provider, real_property_value, start_date, end_date, period_usage_pct,
                 total_cost, paid_date=None, notes=None, db_dict=None):
        """ init function

        Args:
            see superclass docstring
            start_date (datetime.date): must be first day of the year (i.e. YYYY-01-01). also enforced by database
            end_date (datetime.date): must be last day of the year (i.e. YYYY-12-31). also enforced by database
            real_property_value (RealPropertyValues): depreciation item associated with this bill
            period_usage_pct (Decimal): should be percent value between 000.00 and 100.00 (inclusive).
                also enforced by database. percent of period item used for business purposes (active or idle). period
                might not be a full year due to purchase date or disposal date probably aren't on Jan 1st
            paid_date (Optional[datetime.date]): must be None or last day of the year (i.e. YYYY-12-31).
                also enforced by database
        """
        super().__init__(real_estate, service_provider, start_date, end_date, total_cost, paid_date=paid_date,
                         notes=notes)
        self.real_property_value = real_property_value
        self.period_usage_pct = period_usage_pct

        self.db_dict_update(db_dict)

    @SimpleServiceBillDataBase.start_date.setter
    def start_date(self, start_date):
        """ This subclass limits possible start_date values

        Args:
            see __init__ docstring

        Raises:
            ValueError: if start_date is not the first day of the year
        """
        if (start_date.month, start_date.day) != (1, 1):
            raise ValueError("start_date " + str(start_date) + " is invalid. Must have format YYYY-01-01.")

        SimpleServiceBillDataBase.start_date.fset(self, start_date)

    @SimpleServiceBillDataBase.end_date.setter
    def end_date(self, end_date):
        """ This subclass limits possible end_date values

        Args:
            see __init__ docstring

        Raises:
            ValueError: if end_date is not the last day of the year
        """
        if (end_date.month, end_date.day) != (12, 31):
            raise ValueError("end_date " + str(end_date) + " is invalid. Must have format YYYY-12-31.")

        SimpleServiceBillDataBase.end_date.fset(self, end_date)

    @property
    def period_usage_pct(self):
        return self._period_usage_pct

    @period_usage_pct.setter
    def period_usage_pct(self, period_usage_pct):
        """ Enforce percent value limitation

        Args:
            see __init__ docstring period_usage_pct

        Raises:
            ValueError: if period_usage_pct is not between 000.00 and 100.00 (inclusive)
        """
        if period_usage_pct < Decimal(000.00) or period_usage_pct > Decimal(100.00):
            raise ValueError("period_usage_pct " + str(period_usage_pct) +
                             " is invalid. Must be between 000.00 and 100.00 (inclusive)")

        self._period_usage_pct = period_usage_pct

    @SimpleServiceBillDataBase.paid_date.setter
    def paid_date(self, paid_date):
        """ This subclass limits possible paid_date values

        Args:
            see __init__ docstring

        Raises:
            ValueError: if paid_date is not None or the last day of the year
        """
        if paid_date is not None and (paid_date.month, paid_date.day) != (12, 31):
            raise ValueError("paid_date " + str(paid_date) + " is invalid. Must be None or have format YYYY-12-31.")

        SimpleServiceBillDataBase.paid_date.fset(self, paid_date)

    def to_insert_dict(self):
        """ Convert class attributes to MySQL insertable dict

        see overridden function docstring
        "real_property_value" attribute is not included in returned dict
        "real_property_values_id" key is added with value = self.real_property_value.id
        private (single leading underscore) variables will have the leading underscore removed in this function

        Returns:
            dict: copy of self.__dict__ with changes described above
        """
        d = super().to_insert_dict()
        d.pop("real_property_value", None)
        d["real_property_values_id"] = self.real_property_value.id
        d["period_usage_pct"] = d.pop("_period_usage_pct")
        return d

    def to_pd_df(self, deprivatize=True, **kwargs):
        """ see superclass docstring

        Args:
            deprivatize (Optional[boolean]): see superclass docstring
            **kwargs: rpv_prepend (boolean): True to prepend 'rpv_' to self.real_property_value.real_estate instance
                attributes and self.real_property_value.notes attribute. If this is not prepended, there will be columns
                with the same names since self also has real_estate and notes attribute

        Returns:
            pd.DataFrame: see superclass docstring and **kwargs in this docstring
                self.real_property_value.to_pd_df() with 'id' renamed to 'real_property_value_id' and
                    real_property_value column dropped
        """
        do_rpv_prepend = kwargs.get("rpv_prepend", False)

        df = super().to_pd_df(deprivatize=deprivatize, **kwargs)
        rpv_df = self.real_property_value.to_pd_df()

        rpv_df = rpv_df.rename(columns={"id": "real_property_value_id"})
        if do_rpv_prepend:
            rpv_df = rpv_df.rename(columns={col: "rpv_" + col for col in
                ["real_estate_id", "address", "street_num", "street_name", "city", "state", "zip_code", "apt","notes"]})

        df = pd.concat([df, rpv_df], axis=1)
        df = df.drop(columns=["real_property_value"])
        if deprivatize:
            df = df.rename(columns={"_period_usage_pct": "period_usage_pct"})

        return df