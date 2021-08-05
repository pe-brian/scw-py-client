from pydantic import BaseModel
from enum import Enum


class Log(BaseModel):

    class Ordering(BaseModel):

        class OrderBy(Enum):

            TimestampAsc = "timestamp_asc"
            TimestampDesc = "timestamp_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy = OrderBy.TimestampAsc

    id: str = None
    application_id: str = None
    timestamp: str = None
    message: str = None
