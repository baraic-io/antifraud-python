import aiohttp
import json

from .models import Transaction, SyncResolution, AsyncResolution, ServiceResolution, AFTransaction
from .exceptions import ErrRequestFailed, ErrInternalError

class ClientConfig:
    def __init__(self, hostname: str, api_key: str):
        self.hostname: str = hostname
        self.api_key: str = api_key

class Client:
    def __init__(self, config: ClientConfig):
        self.config: ClientConfig = config

    async def __do_request(self, url: str, data: dict) -> dict:
        headers = {"X-API-Key": self.config.api_key}

        async with aiohttp.ClientSession() as httpsession:
            async with httpsession.post(url=url, headers=headers, json=data) as response:
                if response.status != 200:
                    text = await response.text()
                    raise ErrRequestFailed(url=url, code=response.status, message=text)
                
                return await response.json()

    async def validate_transaction_sync(self, transaction: Transaction) -> SyncResolution:
        url = f"{self.config.hostname}/api/gtwsvc/sync/transaction"
        data = transaction.model_dump(by_alias=True)

        try:
            response = await self.__do_request(url=url, data=data)
            return SyncResolution.model_validate(response)
        except ErrRequestFailed as e:
            raise e
        except Exception as e:
            raise ErrInternalError(message=f"internal error: {e}")

    async def validate_transaction_async(self, transaction: Transaction) -> AsyncResolution:
        url = f"{self.config.hostname}/api/gtwsvc/async/transaction"
        data = transaction.model_dump(by_alias=True)

        try:
            response = await self.__do_request(url=url, data=data)
            return AsyncResolution.model_validate(response)
        except ErrRequestFailed as e:
            raise e
        except Exception as e:
            raise ErrInternalError(message=f"internal error: {e}")
        
    async def validate_transaction_by_aml(self, af_transaction: AFTransaction) -> ServiceResolution:
        url = f"{self.config.hostname}/api/amlsvc/validate"
        data = af_transaction.model_dump(by_alias=True)

        try:
            response = await self.__do_request(url=url, data=data)
            return ServiceResolution.model_validate(response)
        except ErrRequestFailed as e:
            raise e
        except Exception as e:
            raise ErrInternalError(message=f"internal error: {e}")