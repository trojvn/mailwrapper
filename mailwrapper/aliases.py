from .anymessage import AnyMessage
from .bower import Bower
from .models.anymessage import AnyMessageResponse
from .models.bower import BowerResponse

EmailService = AnyMessage | Bower
EmailResponses = AnyMessageResponse | BowerResponse
