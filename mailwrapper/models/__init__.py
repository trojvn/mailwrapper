from dataclasses import dataclass

from .anymessage import AnyMessageResponse
from .bower import BowerResponse
from .types import EmailService

EmailResponses = AnyMessageResponse | BowerResponse


@dataclass
class EmailResponse:
    instance: EmailService
    response: EmailResponses
