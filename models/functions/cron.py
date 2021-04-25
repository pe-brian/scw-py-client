from pydantic import BaseModel
from typing import Dict, Any
from enum import Enum

class Cron(BaseModel):

    class Ordering(BaseModel):

        class OrderBy(Enum):

            CreatedAtAsc="created_at_asc"
            CreatedAtDesc="created_at_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy=OrderBy.CreatedAtAsc

    id: str=None
    application_id: str
    schedule: str
    args: Dict[str, Any]=None
