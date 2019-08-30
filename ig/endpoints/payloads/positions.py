from ig.definitions.positions import OrderType
from ig.endpoints.payloads.basepayload import BasePayload


class Position(BasePayload):
    def __init__(
        self,
        epic: str,
        direction: str,
        size: float,
        order_type: str,
        currency_code: str,
        expiry: str = "-",
        time_in_force: str = None,
        level: str = None,
        guaranteed_stop: bool = None,
        stop_level: float = None,
        stop_distance: str = None,
        trailing_stop: bool = None,
        trailing_stop_increment: float = None,
        force_open: bool = None,
        limit_level: float = None,
        limit_distance: float = None,
        quoted_id: str = None,
        deal_reference: str = None,
    ):
        super(Position, self).__init__()

        self._data.update({"epic": epic})
        self._data.update({"direction": direction})
        self._data.update({"size": size})

        if order_type not in [OrderType.Market, OrderType.Limit, OrderType.Quote]:
            raise ValueError("Wrong order type.")

        self._data.update({"orderType": order_type})
        self._data.update({"currencyCode": currency_code})
        self._data.update({"expiry": expiry})
        self._data.update({"timeInForce": time_in_force})
        self._data.update({"level": level})
        self._data.update({"guaranteedStop": guaranteed_stop})
        self._data.update({"stopLevel": stop_level})
        self._data.update({"stopDistance": stop_distance})
        self._data.update({"trailingStop": trailing_stop})
        self._data.update({"trailingStopIncrement": trailing_stop_increment})
        self._data.update({"forceOpen": force_open})
        self._data.update({"limitLevel": limit_level})
        self._data.update({"limitDistance": limit_distance})
        self._data.update({"quoteId": quoted_id})
        self._data.update({"dealReference": deal_reference})

        if order_type == OrderType.Market:
            self._data.update({"level": None})
            self._data.update({"quoteId": None})

        if order_type == OrderType.Limit:
            if level is None:
                raise ValueError("Order Type LIMIT requires a level")

        if order_type == OrderType.Quote:
            if level is None:
                raise ValueError("Order Type QUOTE requires a level")

            if quoted_id is None:
                raise ValueError("Order Type QUOTE requires a quoted_id")

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
