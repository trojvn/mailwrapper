from dataclasses import dataclass

from mailwrapper.aliases import EmailResponses, EmailService


@dataclass
class EmailResponse:
    instance: EmailService
    response: EmailResponses
