from dataclasses import dataclass


@dataclass
class EmailOptions:
    anymessage_service: str
    bower_service: str
    yuharan_service: str

    anymessage_domain: str = ""
    bower_domain: str = ""
    yuharan_domain: str = ""

    anymessage_token: str = ""
    bower_token: str = ""
    yuharan_token: str = ""

    def __post_init__(self):
        if not self.anymessage_domain:
            self.anymessage_domain = "rambler,hotmail,outlook,gmail"
        if not self.bower_domain:
            self.bower_domain = "gmail.com"
        if not self.yuharan_domain:
            self.yuharan_domain = "rambler,hotmail,outlook,gmail"
