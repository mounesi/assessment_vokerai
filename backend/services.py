import openai
from uuid import uuid4
from fastapi import HTTPException
from .models import Order
from .dependencies import get_tenant_storage
from .config import OPENAI_API_KEY
import json

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set or invalid.")

openai.api_key = OPENAI_API_KEY

def parse_user_input(message: str):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful AI that processes drive-thru orders."},
                {"role": "user", "content": message}
            ],
            functions=[
                {
                    "name": "place_order",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "burgers": {"type": "integer", "default": 0},
                            "fries": {"type": "integer", "default": 0},
                            "drinks": {"type": "integer", "default": 0}
                        }
                    }
                },
                {
                    "name": "cancel_order",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "order_id": {"type": "string"}
                        },
                        "required": ["order_id"]
                    }
                }
            ],
            function_call="auto"
        )

        if response.choices and response.choices[0].message.function_call:
            function_call = response.choices[0].message.function_call
            action = function_call.name
            params = json.loads(function_call.arguments)
            return action, params

        raise HTTPException(status_code=400, detail="Invalid AI function call")

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"AI processing error: {e}")

def cancel_order(message: str, tenant_id: str):
    action, params = parse_user_input(message)
    if action == "cancel_order":
        order_id = params.get("order_id")
        storage = get_tenant_storage(tenant_id)
        for order in storage:
            if order.id == order_id:
                storage.remove(order)
                return {"message": f"Order #{order_id} canceled"}
        raise HTTPException(status_code=404, detail="Order not found")
    raise HTTPException(status_code=400, detail="Invalid cancel request")


def place_order(message: str, tenant_id: str):
    action, params = parse_user_input(message)
    if action == "place_order":
        order = Order(
            id=str(uuid4()),
            tenant_id=tenant_id,
            burgers=params.get("burgers", 0),
            fries=params.get("fries", 0),
            drinks=params.get("drinks", 0)
        )
        storage = get_tenant_storage(tenant_id)
        storage.append(order)
        return {
            "message": "Order placed",
            "order": order.model_dump()  # ✅ Replaced .dict() with .model_dump()
        }
    raise HTTPException(status_code=400, detail="Invalid order format")
