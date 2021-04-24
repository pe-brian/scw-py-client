from pydantic import BaseModel
from typing import Dict, Any
from enum import Enum

class Function(BaseModel):

    class Privacy(Enum):

        Unknown="unknown"
        Public="public"
        Private="private"

    class Runtime(Enum):

        Golang="golang"
        Python="python"
        Python3="python3"
        Node8="node8"
        Node10="node10"
        Node14="node14"

    class Ordering(BaseModel):

        class OrderBy(Enum):

            CreatedAtAsc="created_at_asc"
            CreatedAtDesc="created_at_desc"
            NameAsc="name_asc"
            NameDesc="name_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy=OrderBy.CreatedAtAsc
    
    class Config:
        use_enum_values = True

    id: str
    name: str=None
    status: str=None
    organization_id: str
    namespace_id: str
    description: str=None
    environment_variables: Dict[str, Any]=None
    error_message: str=None
    region: str="fr-par"
    registry_endpoint: str=None
    registry_namespace_id: str=None
    min_scale: int=1
    max_scale: int=20
    runtime: Runtime=Runtime.Golang
    handler: str=None
    memory_limit: int=None
    cpu_limit: int=None
    privacy: Privacy=Privacy.Unknown
