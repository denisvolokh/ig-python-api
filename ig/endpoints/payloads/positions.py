from ig.endpoints.payloads.basepayload import BasePayload
from ig.definitions.positions import *

class Position(BasePayload):
    def __init__(
        self, epic: str, direction: str, size: str, order_type: str, currency_code: str, expiry: str = "-", time_in_force: str = None, 
        level: str = None, guaranteedStop: str = None, stop_level: str = None, 
        stop_distance: str = None, trailing_stop: str = None, trailing_stop_incriment: str = None,
        force_open: str = None, limit_level: str = None, limit_distance: str = None, quoted_id: str = None, 
         deal_reference: str = None
    ):
        super(Position, self).__init__()

        if order_type not in [OrderType.Market, OrderType.Limit, OrderType.Quote]:
            raise ValueError("Wrong order type.")

        if order_type == OrderType.Market:
            self._data.update({"level": None})
            self._data.update({"quoteId": None})

    @property
    def data(self):
        """
            Data propery
        :return:
        """
        return super(Position, self).data


# class MarketPosition(Position):
#     def __init__(
#         self, epic: str, 
#     ):
#         super(MarketPosition, self).__init__()

#         self._data.update({"orderType": OrderType.Market})

#     @property
#     def data(self):
#         """
#             Data propery
#         :return:
#         """
#         return super(MarketPosition, self).data
