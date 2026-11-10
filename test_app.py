import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_health_returns_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_sum_two_numbers(client):
    response = client.post(
        "/api/sum",
        json={"a": 10, "b": 20}
    )

    assert response.status_code == 200
    assert response.json == {"result": 30}


def test_sum_missing_parameters(client):
    response = client.post(
        "/api/sum",
        json={"a": 10}
    )

    assert response.status_code == 400
    assert "error" in response.json


def test_sum_invalid_types(client):
    response = client.post(
        "/api/sum",
        json={"a": "diez", "b": 20}
    )

    assert response.status_code == 400
    assert "error" in response.json


def test_sum_boolean_values(client):
    response = client.post(
        "/api/sum",
        json={"a": True, "b": 20}
    )

    assert response.status_code == 400
    assert "error" in response.json
