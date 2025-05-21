from dataclasses import dataclass

from mailwrapper.models.anymessage import AnyMessageResponse
from mailwrapper.models.bower import BowerResponse
from mailwrapper.models.types import EmailService

EmailResponses = AnyMessageResponse | BowerResponse


@dataclass
class EmailResponse:
    instance: EmailService
    response: EmailResponses
