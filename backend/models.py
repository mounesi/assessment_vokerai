from pydantic import BaseModel, conint
from typing import Optional

class Order(BaseModel):
    id: str
    tenant_id: str
    burgers: conint(ge=0) = 0
    fries: conint(ge=0) = 0
    drinks: conint(ge=0) = 0
