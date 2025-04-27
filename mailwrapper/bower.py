from httpwrapper import BaseClient, ClientConfig

from .models.bower import BowerResponse


class Bower(BaseClient):
    def __init__(self, token: str):
        self.__token = token
        super().__init__("https://smsbower.com/api/mail")
        self.__config = ClientConfig(1, 10, 0, 0)

    def get_mail(self, service: str, domain: str) -> BowerResponse | None:
        params = {"api_key": self.__token, "service": service, "domain": domain}
        r = self._get("/getActivation", params, self.__config)
        if r.status_code == 200:
            if json_data := r.json():
                if json_data.get("status", 0) != 1:
                    return
                _id = json_data.get("mailId", "")
                email = json_data.get("mail", "")
                if _id and email:
                    return BowerResponse(_id, email)

    def get_code(self, _id: str) -> str:
        params = {"api_key": self.__token, "mailId": _id}
        r = self._get("/getCode", params, self.__config)
        if r.status_code == 200:
            if json_data := r.json():
                if json_data.get("status", 0) != 1:
                    return ""
                return json_data.get("code", "")
        return ""
