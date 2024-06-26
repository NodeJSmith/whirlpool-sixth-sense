import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest

from .aiohttp import AiohttpClientMocker
from .mock_backendselector import BackendSelectorMock


@pytest.fixture
def http_client_mock(mocker, backend_selector_mock):
    """Set up aiohttp ClientSession mock."""
    http_client_mocker = AiohttpClientMocker()
    mocker.patch(
        "aiohttp.ClientSession",
        side_effect=lambda *args, **kwargs: http_client_mocker.create_session(
            asyncio.get_event_loop()
        ),
    )
    return http_client_mocker


@pytest.fixture
def appliance_http_client_mock(
    http_client_mock, backend_selector_mock: BackendSelectorMock
):
    http_client_mock.get(
        backend_selector_mock.websocket_url, json={"url": "wss://something"}
    )

    return http_client_mock


@pytest.fixture
def backend_selector_mock():
    return BackendSelectorMock()


@pytest.fixture
def auth_mock():
    return MagicMock()


@pytest.fixture(autouse=True)
def event_socket_mock(mocker):
    event_socket = mocker.patch("whirlpool.appliance.EventSocket").return_value
    event_socket.stop = AsyncMock()
    return event_socket
