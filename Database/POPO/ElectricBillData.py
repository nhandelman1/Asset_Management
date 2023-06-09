from decimal import Decimal
from typing import Optional
from Database.POPO.ComplexServiceBillDataBase import ComplexServiceBillDataBase


class ElectricBillData(ComplexServiceBillDataBase):
    """ Actual or estimated data provided on monthly electric bill or relevant to monthly bill

    Attributes:
        see super class docstring
        see init docstring for attributes (db_dict is not kept as an attribute)
    """

    def __init__(self, real_estate, service_provider, start_date, end_date, total_kwh, eh_kwh, bank_kwh, total_cost,
                 bs_rate, bs_cost, dsc_total_cost, toc_total_cost, is_actual, first_kwh=None, first_rate=None,
                 first_cost=None,  next_kwh=None, next_rate=None, next_cost=None, cbc_rate=None, cbc_cost=None,
                 mfc_rate=None, mfc_cost=None, psc_rate=None, psc_cost=None, psc_total_cost=None, der_rate=None,
                 der_cost=None, dsa_rate=None, dsa_cost=None, rda_rate=None, rda_cost=None, nysa_rate=None,
                 nysa_cost=None, rbp_rate=None, rbp_cost=None, spta_rate=None, spta_cost=None, st_rate=None,
                 st_cost=None, paid_date=None, notes=None, db_dict=None):
        """ init function

        Args:
            see super class init docstring
            total_kwh (int): nonnegative total kwh used from provider
            eh_kwh (int): electric heater kwh usage
            bank_kwh (int): nonnegative banked kwh
            bs_rate (Decimal): basic service charge rate
            bs_cost (Decimal): basic service charge cost
            dsc_total_cost (Decimal): delivery and service charge total cost
            toc_total_cost (Decimal): taxes and other charges total cost
            first_kwh (Optional[int]): kwh used at first rate. will not be in bill if none used. Default None
            first_rate (Optional[Decimal]): first rate. will not be in bill if none used. Default None
            first_cost (Optional[Decimal]): first cost. will not be in bill if none used. Default None
            next_kwh (Optional[int]): kwh used at next rate. will not be in bill if none used. Default None
            next_rate (Optional[Decimal]): next rate. will not be in bill if none used. Default None
            next_cost (Optional[Decimal]): next cost. will not be in bill if none used. Default None
            cbc_rate (Optional[Decimal]): customer benefit contribution charge rate. Default None
            cbc_cost (Optional[Decimal]): customer benefit contribution charge cost. Default None
            mfc_rate (Optional[Decimal]): merchant function charge rate. Default None
            mfc_cost (Optional[Decimal]): merchant function charge cost. Default None
            psc_rate (Optional[Decimal]): power supply charge rate. Default None
            psc_cost (Optional[Decimal]): power supply charge cost. Default None
            psc_total_cost (Optional[Decimal]): power supply charge total cost. Default None
            der_rate (Optional[Decimal]): distributed energy resources charge rate. Default None
            der_cost (Optional[Decimal]): distributed energy resources charge cost. Default None
            dsa_rate (Optional[Decimal]): delivery service adjustment rate. Default None
            dsa_cost (Optional[Decimal]): delivery service adjustment cost. Default None
            rda_rate (Optional[Decimal]): revenue decoupling adjustment rate. Default None
            rda_cost (Optional[Decimal]): revenue decoupling adjustment cost. Default None
            nysa_rate (Optional[Decimal]): new york state assessment rate. Default None
            nysa_cost (Optional[Decimal]): new york state assessment cost. Default None
            rbp_rate (Optional[Decimal]): revenue based pilots rate. Default None
            rbp_cost (Optional[Decimal]): revenue based pilots cost. Default None
            spta_rate (Optional[Decimal]): revenue decoupling adjustment rate. Default None
            spta_cost (Optional[Decimal]): suffolk property tax adjustment cost. Default None
            st_rate (Optional[Decimal]): sales tax rate. Default None
            st_cost (Optional[Decimal]): sales tax cost. Default None
            db_dict (Optional[dict]): dictionary holding arguments. if an argument is in the dictionary, it will
                overwrite an argument provided explicitly through the argument variable
        """
        super().__init__(real_estate, service_provider, start_date, end_date, total_cost, is_actual,
                         paid_date=paid_date, notes=notes)

        self.total_kwh = total_kwh
        self.eh_kwh = eh_kwh
        self.bank_kwh = bank_kwh
        self.bs_rate = bs_rate
        self.bs_cost = bs_cost
        self.first_kwh = first_kwh
        self.first_rate = first_rate
        self.first_cost = first_cost
        self.next_kwh = next_kwh
        self.next_rate = next_rate
        self.next_cost = next_cost
        self.cbc_rate = cbc_rate
        self.cbc_cost = cbc_cost
        self.mfc_rate = mfc_rate
        self.mfc_cost = mfc_cost
        self.dsc_total_cost = dsc_total_cost
        self.psc_rate = psc_rate
        self.psc_cost = psc_cost
        self.psc_total_cost = psc_total_cost
        self.der_rate = der_rate
        self.der_cost = der_cost
        self.dsa_rate = dsa_rate
        self.dsa_cost = dsa_cost
        self.rda_rate = rda_rate
        self.rda_cost = rda_cost
        self.nysa_rate = nysa_rate
        self.nysa_cost = nysa_cost
        self.rbp_rate = rbp_rate
        self.rbp_cost = rbp_cost
        self.spta_rate = spta_rate
        self.spta_cost = spta_cost
        self.st_rate = st_rate
        self.st_cost = st_cost
        self.toc_total_cost = toc_total_cost

        self.db_dict_update(db_dict)