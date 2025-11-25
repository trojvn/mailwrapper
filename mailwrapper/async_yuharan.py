from mailwrapper.base import BaseAnyMessage


class AsyncYuharan(BaseAnyMessage):
    def __init__(self, token: str, proxy: str | None = None):
        super().__init__("http://yuharan.ru:4545", token, proxy)
