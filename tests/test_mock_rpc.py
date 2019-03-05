import pytest

from conftest import MockRPCMatchException


class TestMockRPCSession(object):
    def test_existing_request(self, mock_rpc_session):
        resp = mock_rpc_session.post(
            'mock://localhost:7076/', json={"action": "version"}
        )
        assert resp.json() == {
            "rpc_version": "1",
            "store_version": "13",
            "protocol_version": "16",
            "node_vendor": "Nano 18.0",
        }

    def test_missing_request(self, mock_rpc_session):
        with pytest.raises(MockRPCMatchException):
            resp = mock_rpc_session.post(
                'mock://localhost:7076/', json={"action": "DOES NOT EXIST"}
            )
