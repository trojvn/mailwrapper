import logging

from httpwrapper import BaseClient, ClientConfig

from .models.anymessage import AnyMessageResponse

logger = logging.getLogger("mailwrapper")


class AnyMessage(BaseClient):
    def __init__(self, token: str):
        self.__token = token
        self.__config = ClientConfig(1, 10, 0, 0)
        super().__init__("https://api.anymessage.shop")

    def get_email(
        self,
        site: str,
        domain: str,
        regex: str = "",
    ) -> AnyMessageResponse | None:
        params = {"token": self.__token, "domain": domain, "site": site}
        if regex:
            params["regex"] = regex
        r = self._get("/email/order", params, self.__config)
        if r.status_code == 200:
            if json_data := r.json():
                logger.info(f"get_email: {json_data}")
                status = json_data.get("status")
                if status == "success":
                    email = json_data.get("email", "")
                    _id = json_data.get("id", "")
                    if email and _id:
                        return AnyMessageResponse(email=email, id=_id)

    def get_code(self, _id: str) -> str:
        params = {"token": self.__token, "id": _id}
        r = self._get("/email/getmessage", params, self.__config)
        if r.status_code == 200:
            if json_data := r.json():
                logger.info(f"get_code: {json_data}")
                if json_data.get("status", "") == "success":
                    if value := json_data.get("value", ""):
                        return value
                    if message := json_data.get("message", ""):
                        return message
        return ""
