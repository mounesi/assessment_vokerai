from fastapi import FastAPI, Depends
from pydantic import BaseModel
from .services import place_order, cancel_order
from .dependencies import get_tenant_storage
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# ✅ Allow CORS from localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (POST, GET, OPTIONS)
    allow_headers=["*"],  # Allow all headers
)

class OrderRequest(BaseModel):
    message: str

@app.post("/place_order/")
def create_order(request: OrderRequest, tenant_id: str):
    return place_order(request.message, tenant_id)

@app.post("/cancel_order/")
def remove_order(request: OrderRequest, tenant_id: str):
    return cancel_order(request.message, tenant_id)

@app.get("/orders/")
def get_orders(tenant_id: str):
    return {"orders": get_tenant_storage(tenant_id)}

@app.get("/summary/")
def get_summary(tenant_id: str):
    storage = get_tenant_storage(tenant_id)
    total_burgers = sum(order.burgers for order in storage)
    total_fries = sum(order.fries for order in storage)
    total_drinks = sum(order.drinks for order in storage)
    return {
        "total_burgers": total_burgers,
        "total_fries": total_fries,
        "total_drinks": total_drinks
    }
