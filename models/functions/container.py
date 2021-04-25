from typing import Callable
from pydantic import BaseModel
from enum import Enum

class Container(BaseModel):

    class Privacy(Enum):

        Unknown="unknow"
        Public="public"
        Private="private"

    class Ordering(BaseModel):

        class OrderBy(Enum):

            CreatedAtAsc="created_at_asc"
            CreatedAtDesc="created_at_desc"
            NameAsc="name_asc"
            NameDesc="name_desc"

        class Config:
            use_enum_values=True

        order_by: OrderBy=OrderBy.CreatedAtAsc

    class Config:  
        use_enum_values=True

    id: str=None
    namespace_id: str
    name: str
    timeout: int
    environment_variables: dict=None
    min_scale: int=None
    max_scale: int=None
    memory_limit: int=None
    cpu_limit: int=None
    privacy: Privacy=Privacy.Unknown
    description: str=None
    registry_image: str=None
    max_concurrency: int=None
    domain_name: str=None