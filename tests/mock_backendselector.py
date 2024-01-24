from enum import Enum
from typing import Dict, List


class DummyBrand(Enum):
    DUMMY_BRAND = "dummy_brand"


class DummyRegion(Enum):
    DUMMY_REGION = "dummy_region"


class BackendSelectorMock:
    @property
    def brand(self):
        return DummyBrand.DUMMY_BRAND

    @property
    def region(self):
        return DummyRegion.DUMMY_REGION

    @property
    def base_url(self):
        return "http://dummy_base_url.com"

    @property
    def auth_url(self):
        return f"{self.base_url}/oauth/token"

    @property
    def client_credentials(self) -> List[Dict[str, str]]:
        return [
            {
                "client_id": "dummy_client_id1",
                "client_secret": "dummy_client_secret1",
            },
        ]


class BackendSelectorMockMultipleCreds(BackendSelectorMock):
    @property
    def client_credentials(self) -> List[Dict[str, str]]:
        return [
            {
                "client_id": "dummy_client_id1",
                "client_secret": "dummy_client_secret1",
            },
            {
                "client_id": "dummy_client_id2",
                "client_secret": "dummy_client_secret2",
            },
        ]
