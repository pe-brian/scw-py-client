from pydantic import BaseModel
from typing import Dict, Any
from enum import Enum

class Namespace(BaseModel):

    class Ordering(BaseModel):

        class OrderBy(Enum):

            CreatedAtAsc="created_at_asc"
            CreatedAtDesc="created_at_desc"
            NameAsc="name_asc"
            NameDesc="name_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy=OrderBy.CreatedAtAsc

    id: str=None
    name: str=None
    organization_id: str
    description: str=None
    environment_variables: Dict[str, Any]=None
    error_message: str=None
    region: str="fr-par"
    registry_endpoint: str=None
    registry_namespace_id: str=None
    status: str="ready"
