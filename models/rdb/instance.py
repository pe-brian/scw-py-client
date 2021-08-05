from models.region import Region
from typing import List
from pydantic import BaseModel
from enum import Enum


class Instance(BaseModel):

    class Ordering(BaseModel):

        class OrderBy(Enum):

            CreatedAtAsc = "created_at_asc"
            CreatedAtDesc = "created_at_desc"
            NameAsc = "name_asc"
            NameDesc = "name_desc"
            Region = "region"
            StatusAsc = "status_asc"
            StatusDec = "status_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy = OrderBy.CreatedAtAsc

    class Config:
        use_enum_values = True

    id: str
    region: Region = Region.FrPar
    name: str = None
    status: str
    status_message: str = None
    created_at: str
    tags: List[str]
