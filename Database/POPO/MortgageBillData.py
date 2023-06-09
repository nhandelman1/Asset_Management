from decimal import Decimal
from Database.POPO.SimpleServiceBillDataBase import SimpleServiceBillDataBase


class MortgageBillData(SimpleServiceBillDataBase):
    """ Mortgage implementation of SimpleServiceBillDataBase

    Attributes:
        see init docstring for attributes (db_dict is not kept as an attribute)
    """
    def __init__(self, real_estate, service_provider, start_date, end_date, total_cost, outs_prin, esc_bal, prin_pmt,
                 int_pmt, esc_pmt, other_pmt, paid_date=None, notes=None, db_dict=None):
        """ init function

        Args:
            see superclass docstring
            outs_prin (Decimal): outstanding principal before principal payment is applied
            esc_bal (Decimal): escrow balance
            prin_pmt (Decimal): principal payment
            int_pmt (Decimal): interest payment
            esc_pmt (Decimal): escrow payment
            other_pmt (Decimal): other payment
        """
        super().__init__(real_estate, service_provider, start_date, end_date, total_cost, paid_date=paid_date,
                         notes=notes)

        self.outs_prin = outs_prin
        self.esc_bal = esc_bal
        self.prin_pmt = prin_pmt
        self.int_pmt = int_pmt
        self.esc_pmt = esc_pmt
        self.other_pmt = other_pmt

        self.db_dict_update(db_dict)
