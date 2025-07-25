import asyncio
import logging
from datetime import datetime, timedelta

from aiohttp import ClientTimeout
from httpwrapper import AsyncClientConfig, BaseAsyncClient

from mailwrapper.models.bower import BowerResponse

logger = logging.getLogger("mailwrapper")


class AsyncBower(BaseAsyncClient):
    def __init__(self, token: str, proxy: str | None = None):
        self.__token = token
        timeout = ClientTimeout(total=10, connect=10)
        self.__config = AsyncClientConfig(3, timeout, 0, 0, proxy=proxy)
        super().__init__("https://smsbower.com/api/mail", config=self.__config)

    async def get_email(self, service: str, domain: str) -> BowerResponse | None:
        params = {
            "api_key": self.__token,
            "service": service,
            "domain": domain,
        }
        r = await self._get("/getActivation", params)
        if r.status == 200:
            if json_data := await r.json():
                logger.info(f"get_email: {json_data}")
                if json_data.get("status", 0) != 1:
                    return
                _id = json_data.get("mailId", "")
                email = json_data.get("mail", "")
                if _id and email:
                    return BowerResponse(email=email, id=_id)

    async def get_email_loop(
        self,
        service: str,
        domain: str,
        *,
        wait_time: int = 60,
    ) -> BowerResponse | None:
        future = datetime.now() + timedelta(seconds=wait_time)
        while future > datetime.now():
            if response := await self.get_email(service, domain):
                return response
            await asyncio.sleep(1)

    async def get_code(self, _id: str) -> str:
        """Сразу отправляет код (без текста)"""
        params = {"api_key": self.__token, "mailId": _id}
        r = await self._get("/getCode", params)
        if r.status == 200:
            if json_data := await r.json():
                logger.info(f"get_code: {json_data}")
                if json_data.get("status", 0) != 1:
                    return ""
                return json_data.get("code", "")
        return ""

    async def get_code_loop(self, _id: str, *, wait_time: int = 60) -> str:
        """Сразу отправляет код (без текста)"""
        future = datetime.now() + timedelta(seconds=wait_time)
        while future > datetime.now():
            if code := await self.get_code(_id):
                return code
            await asyncio.sleep(1)
        return ""
