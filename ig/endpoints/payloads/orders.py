from exante.endpoints.payloads.basepayload import BasePayload
from exante.definitions.orders import OrderSide, OrderType, OrderDuration


class MarketOrder(BasePayload):
    def __init__(
        self, account: str, instrument: str, side: str, quantity: str, duration: str
    ):
        super(MarketOrder, self).__init__()

        self._data.update({"orderType": OrderType.Market})

        if account is None:
            raise ValueError("Account ID is not specified")

        self._data.update({"account": account})

        if instrument is None:
            raise ValueError("Instrument is not defined")

        self._data.update({"instrument": instrument})

        if side not in [OrderSide.Buy, OrderSide.Sell]:
            raise ValueError("Wrong order side")

        self._data.update({"side": side})

        if quantity is None:
            raise ValueError("Order quantity is not defined")

        self._data.update({"quantity": quantity})

        if duration not in [
            OrderDuration.Day,
            OrderDuration.FillOrKill,
            OrderDuration.ImmediateOrCancel,
        ]:
            raise ValueError("Wrong order duration")

        self._data.update({"duration": duration})

    @property
    def data(self):
        """
            Data propery
        :return:
        """
        return super(MarketOrder, self).data
