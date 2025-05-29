from mailwrapper.base import BaseAnyMessage


class AsyncYuharan(BaseAnyMessage):
    def __init__(self, token: str):
        super().__init__("https://inboxifyapi.yuharan.ru", token)
