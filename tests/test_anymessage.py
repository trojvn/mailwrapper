import os

from mailwrapper import AnyMessage

TOKEN = os.getenv("TOKEN", "")


def test_anymessage():
    anymessage = AnyMessage(TOKEN)
    print(anymessage.get_email("telegram.org", "gmail.com", r"\d{5,6}"))
    # AnyMessageResponse(email='vanjacksonlaella@gmail.com', id='11539027006')


def test_anymessage_get_code():
    anymessage = AnyMessage(TOKEN)
    print(anymessage.get_code("1539027006"))
