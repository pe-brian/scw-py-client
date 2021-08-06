from pydantic import BaseModel, validator
from enum import Enum
from typing import List
from datetime import datetime
import re


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


class User(BaseModel):

    class Ordering(BaseModel):

        class OrderBy(Enum):

            NameAsc = "name_asc"
            NameDesc = "name_desc"
            IsAdminAsc = "is_admin_asc"
            IsAdminDec = "is_admin_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy = OrderBy.NameAsc

    class Config:
        use_enum_values = True

    class Password(str):

        def __new__(cls, v):
            if not re.match(r"^(?=\S*[a-z])(?=\S*[A-Z])(?=\S*\d)(?=\S*[^\w\s])\S{8,}$", v):
                raise ValueError(
                    "Password must have at least one upper character, one lower character, "
                    "one special character, one number and length must be 8 or more")
            return str.__new__(cls, v)

    @validator("name")
    def check_name(cls, v):
        if not re.match(r"^[\w\$\-]{1,63}$", v) or not v[0].isalpha() or v.startswith("_rdb"):
            raise ValueError(
                f"User name ({v}) length must be between 1 and 63 characters, first character must be an alphabet "
                "character (a-zA-Z), and cannot start with '_rdb', only a-zA-Z0-9_$- characters are accepted")
        return v

    name: str
    is_admin: bool = False


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
    name: str = None
    status: str
    status_message: str = None
    created_at: datetime
    tags: List[str]


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

    name: str = None
    owner: str = None
    status: str = None
    size: int = None
