from pydantic import BaseModel
from enum import Enum


class Privileges(BaseModel):

    class Permission(Enum):

        ReadOnly = "readonly"
        ReadWrite = "readwrite"
        All = "all"
        Custom = "custom"
        _None = "none"

    class Ordering(BaseModel):

        class OrderBy(Enum):

            UserNameAsc = "user_name_asc"
            UserNameDesc = "user_name_desc"
            DatabaseNameAsc = "database_name_asc"
            DatabaseNameDesc = "database_name_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy = OrderBy.UserNameAsc

    class Config:
        use_enum_values = True

    permission: Permission = Permission.ReadOnly
    database_name: str
    user_name: str
