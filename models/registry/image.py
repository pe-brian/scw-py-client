from datetime import datetime
from typing import List
from pydantic import BaseModel
from enum import Enum


class Image(BaseModel):

    class Privacy(Enum):

        Unknown = "unknow"
        Public = "public"
        Private = "private"

    class Ordering(BaseModel):

        class OrderBy(Enum):

            CreatedAtAsc = "created_at_asc"
            CreatedAtDesc = "created_at_desc"
            NameAsc = "name_asc"
            NameDesc = "name_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy = OrderBy.CreatedAtAsc

    class Config:
        use_enum_values = True

    id: str
    namespace_id: str
    name: str
    status: str
    status_message: str = None
    visibility: str
    size: int
    created_at: datetime
    updated_at: datetime
    tags: List[str]
