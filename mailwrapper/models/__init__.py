from dataclasses import dataclass

from mailwrapper.anymessage import AnyMessage
from mailwrapper.bower import Bower
from mailwrapper.models.anymessage import AnyMessageResponse
from mailwrapper.models.bower import BowerResponse

EmailService = AnyMessage | Bower
EmailResponses = AnyMessageResponse | BowerResponse


@dataclass
class EmailResponse:
    instance: EmailService
    response: EmailResponses


__all__ = ["EmailResponse", "EmailService", "EmailResponses"]
