from dataclasses import dataclass

from ..types import EmailService
from .anymessage import AnyMessageResponse
from .bower import BowerResponse

EmailResponses = AnyMessageResponse | BowerResponse


@dataclass
class EmailResponse:
    instance: EmailService
    response: EmailResponses
