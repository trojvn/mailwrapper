from httpwrapper import BaseClient, ClientConfig

from .models.anymessage import AnyMessageEmailResponse


class AnyMessage(BaseClient):
    def __init__(self, token: str):
        super().__init__("https://api.anymessage.shop")
        self.__token = token
        self.__config = ClientConfig(1, 10, 0, 0)

    def get_mail(
        self,
        site: str,
        domain: str,
        regex: str = "",
    ) -> AnyMessageEmailResponse | None:
        params = {"token": self.__token, "domain": domain, "site": site}
        if regex:
            params["regex"] = regex
        r = self._get("/email/order", params, self.__config)
        if r.status_code == 200:
            if json_data := r.json():
                status = json_data.get("status")
                if status == "success":
                    email = json_data.get("email", "")
                    _id = json_data.get("id", "")
                    if email and _id:
                        return AnyMessageEmailResponse(email, _id)

    def get_code(self, _id: str) -> str:
        params = {"token": self.__token, "id": _id}
        r = self._get("/email/getmessage", params, self.__config)
        if r.status_code == 200:
            if json_data := r.json():
                if json_data.get("status", "") == "success":
                    if value := json_data.get("value", ""):
                        return value
                    if message := json_data.get("message", ""):
                        return message
        return ""
