import logging

from httpwrapper import BaseClient, ClientConfig

from mailwrapper.models.bower import BowerResponse

logger = logging.getLogger("mailwrapper")


class Bower(BaseClient):
    def __init__(self, token: str):
        self.__token = token
        self.__config = ClientConfig(1, 10, 0, 0)
        super().__init__("https://smsbower.com/api/mail")

    def get_email(self, service: str, domain: str) -> BowerResponse | None:
        params = {
            "api_key": self.__token,
            "service": service,
            "domain": domain,
        }
        r = self._get("/getActivation", params, self.__config)
        if r.status_code == 200:
            if json_data := r.json():
                logger.info(f"get_email: {json_data}")
                if json_data.get("status", 0) != 1:
                    return
                _id = json_data.get("mailId", "")
                email = json_data.get("mail", "")
                if _id and email:
                    return BowerResponse(email=email, id=_id)

    def get_code(self, _id: str) -> str:
        """Сразу отправляет код (без текста)"""
        params = {"api_key": self.__token, "mailId": _id}
        r = self._get("/getCode", params, self.__config)
        if r.status_code == 200:
            if json_data := r.json():
                logger.info(f"get_code: {json_data}")
                if json_data.get("status", 0) != 1:
                    return ""
                return json_data.get("code", "")
        return ""
