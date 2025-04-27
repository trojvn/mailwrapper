import os

from mailwrapper import Bower

TOKEN = os.getenv("TOKEN", "")


def test_bower_get_mail():
    bower = Bower(TOKEN)
    print(bower.get_email("tg", "gmail.com"))
    # BowerResponse(id=11649209, email='MikeAbramson7039@gmail.com')


def test_bower_get_code():
    bower = Bower(TOKEN)
    print(bower.get_code("11649209"))
