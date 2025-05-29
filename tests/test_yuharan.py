import pytest

from mailwrapper.async_yuharan import AsyncYuharan

# @pytest.mark.asyncio
# async def test_yuharan():
#     instance = AsyncYuharan("vova")
#     if r := await instance.get_email_loop("telegram.com", "rambler,hotmail"):
#         print(r)


@pytest.mark.asyncio
async def test_yuharan_get_code():
    instance = AsyncYuharan("vova")
    code = await instance.get_code_loop("marta_m19596899@rambler.ru")
    print(code)
