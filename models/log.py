from pydantic import BaseModel
from typing import Dict, Any
from enum import Enum

class Log(BaseModel):

    class Ordering(BaseModel):

        class OrderBy(Enum):

            TimestampAsc="timestamp_asc"
            TimestampDesc="timestamp_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy=OrderBy.TimestampAsc

    id: str
    application_id: str
    timestamp: str=None
