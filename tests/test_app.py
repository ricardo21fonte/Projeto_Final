import app as service
from fastapi.testclient import TestClient


def test_health():
    with TestClient(service.app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert "service" in response.json()


def test_visits_persistence(tmp_path, monkeypatch):
    monkeypatch.setattr(service, "COUNTER_FILE", tmp_path / "visitas.txt")
    with TestClient(service.app) as client:
        assert client.get("/visits").json() == {"visits": 0}
        assert client.post("/visits").json() == {"visits": 1}
        assert client.post("/visits").json() == {"visits": 2}
        assert client.get("/visits").json() == {"visits": 2}
