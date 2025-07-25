from mailwrapper.base import BaseAnyMessage


class AsyncYuharan(BaseAnyMessage):
    def __init__(self, token: str, proxy: str | None = None):
        super().__init__("https://inboxifyapi.yuharan.ru", token, proxy)
