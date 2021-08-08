from pydantic import BaseModel
from typing import Dict, Any
from enum import Enum
from .region import Region


class Namespace(BaseModel):

    class Ordering(BaseModel):

        class OrderBy(Enum):

            CreatedAtAsc = "created_at_asc"
            CreatedAtDesc = "created_at_desc"
            NameAsc = "name_asc"
            NameDesc = "name_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy = OrderBy.CreatedAtAsc

    id: str = None
    name: str = None
    organization_id: str
    description: str = None
    environment_variables: Dict[str, Any] = None
    error_message: str = None
    region: Region = Region.FrPar
    registry_endpoint: str = None
    registry_namespace_id: str = None
    status: str = "ready"


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


class Function(BaseModel):

    class Privacy(Enum):

        Unknown = "unknown"
        Public = "public"
        Private = "private"

    class Runtime(Enum):

        Golang = "golang"
        Python = "python"
        Python3 = "python3"
        Node8 = "node8"
        Node10 = "node10"
        Node14 = "node14"

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

    id: str = None
    name: str = None
    status: str = None
    organization_id: str
    namespace_id: str
    description: str = None
    environment_variables: Dict[str, Any] = None
    error_message: str = None
    region: str = Region.FrPar
    registry_endpoint: str = None
    registry_namespace_id: str = None
    min_scale: int = 1
    max_scale: int = 20
    runtime: Runtime = Runtime.Golang
    handler: str = None
    memory_limit: int = None
    cpu_limit: int = None
    privacy: Privacy = Privacy.Unknown


class Cron(BaseModel):

    class Ordering(BaseModel):

        class OrderBy(Enum):

            CreatedAtAsc = "created_at_asc"
            CreatedAtDesc = "created_at_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy = OrderBy.CreatedAtAsc

    id: str = None
    application_id: str
    schedule: str
    args: Dict[str, Any] = None


class Container(BaseModel):

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

    id: str = None
    namespace_id: str
    name: str
    timeout: int
    environment_variables: dict = None
    min_scale: int = None
    max_scale: int = None
    memory_limit: int = None
    cpu_limit: int = None
    privacy: Privacy = Privacy.Unknown
    description: str = None
    registry_image: str = None
    max_concurrency: int = None
    domain_name: str = None
