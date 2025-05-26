import asyncio
import logging
from datetime import datetime, timedelta

from aiohttp import ClientTimeout
from httpwrapper import AsyncClientConfig, BaseAsyncClient

from mailwrapper.models.anymessage import AnyMessageResponse

logger = logging.getLogger("mailwrapper")


class AsyncAnyMessage(BaseAsyncClient):
    def __init__(self, token: str):
        self.__token = token
        timeout = ClientTimeout(total=10, connect=10)
        self.__config = AsyncClientConfig(1, timeout, 0, 0)
        super().__init__("https://api.anymessage.shop")

    async def get_email(
        self,
        site: str,
        domain: str,
        regex: str = "",
    ) -> AnyMessageResponse | None:
        params = {"token": self.__token, "domain": domain, "site": site}
        if regex:
            params["regex"] = regex
        r = await self._get("/email/order", params, self.__config)
        if r.status == 200:
            if json_data := await r.json():
                logger.info(f"get_email: {json_data}")
                status = json_data.get("status")
                if status == "success":
                    email = json_data.get("email", "")
                    _id = json_data.get("id", "")
                    if email and _id:
                        return AnyMessageResponse(email=email, id=_id)

    async def get_code(self, _id: str) -> str:
        params = {"token": self.__token, "id": _id}
        r = await self._get("/email/getmessage", params, self.__config)
        if r.status == 200:
            if json_data := await r.json():
                logger.info(f"get_code: {json_data}")
                if json_data.get("status", "") == "success":
                    if value := json_data.get("value", ""):
                        return value
                    if message := json_data.get("message", ""):
                        return message
        return ""

    async def get_code_loop(self, _id: str, *, wait_time: int = 60) -> str:
        future = datetime.now() + timedelta(seconds=wait_time)
        while future > datetime.now():
            if code := await self.get_code(_id):
                return code
            await asyncio.sleep(1)
        return ""
