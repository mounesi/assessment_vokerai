from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_place_order():
    response = client.post(
        "/place_order/?tenant_id=test",
        json={"message": "I want 2 burgers and 1 fries"}
    )
    
    assert response.status_code == 200
    assert "order" in response.json()
    assert response.json()["order"]["burgers"] == 2
    assert response.json()["order"]["fries"] == 1

def test_cancel_order():
    order_response = client.post(
        "/place_order/?tenant_id=test",
        json={"message": "I want a burger"}
    )

    assert order_response.status_code == 200
    order_id = order_response.json()["order"]["id"]

    cancel_response = client.post(
        "/cancel_order/?tenant_id=test",
        json={"message": f"Cancel order #{order_id}"}
    )

    assert cancel_response.status_code == 200
    assert cancel_response.json()["message"] == f"Order #{order_id} canceled"
