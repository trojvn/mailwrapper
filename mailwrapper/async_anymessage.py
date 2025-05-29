from mailwrapper.base import BaseAnyMessage


class AsyncAnyMessage(BaseAnyMessage):
    def __init__(self, token: str):
        super().__init__("https://api.anymessage.shop", token)
