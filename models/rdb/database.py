from pydantic import BaseModel
from enum import Enum


class Database(BaseModel):

    class Ordering(BaseModel):

        class OrderBy(Enum):

            NameAsc = "name_asc"
            NameDesc = "name_desc"
            SizeAsc = "size_asc"
            SizeDesc = "size_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy = OrderBy.NameAsc

    class Config:
        use_enum_values = True

    id: str
    name: str = None
    owner: str = None
    status: str
    size: int
