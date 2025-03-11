from typing import Dict, List
from .models import Order

orders: Dict[str, List[Order]] = {}

def get_tenant_storage(tenant_id: str):
    if tenant_id not in orders:
        orders[tenant_id] = []
    return orders[tenant_id]
