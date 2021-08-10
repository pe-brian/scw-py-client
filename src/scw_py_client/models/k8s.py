from typing import Dict
from pydantic import BaseModel
from enum import Enum


class Node(BaseModel):

    class Status(Enum):

        Unknown = "unknown"
        Creating = "creating"
        NotReady = "not_ready"
        Ready = "ready"
        Deleting = "deleting"
        Deleted = "deleted"
        Locked = "locked"
        Rebooting = "rebooting"
        CreationError = "creation_error"
        Upgrading = "upgrading"

    class Ordering(BaseModel):

        class OrderBy(Enum):
            CreatedAtAsc = "created_at_asc"
            CreatedAtDesc = "created_at_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy = OrderBy.CreatedAtAsc

    class Config:
        use_enum_values = True

    id: str = None
    pool_id: str = None
    cluster_id: str = None
    region: str = None
    name: str = None
    public_ip_v4: str = None
    public_ip_v6: str = None
    conditions: Dict[str, str] = None
    status: str = None
    created_at: str = None
    updated_at: str = None


class Cluster(BaseModel):

    class Status(Enum):

        Unknown = "unknown"
        Creating = "creating"
        Ready = "ready"
        Deleting = "deleting"
        Deleted = "deleted"
        Updating = "updating"
        Locked = "locked"
        PoolRequired = "pool_required"

    class Ordering(BaseModel):

        class OrderBy(Enum):

            CreatedAtAsc = "created_at_asc"
            CreatedAtDesc = "created_at_desc"
            UpdatedAtAsc = "updated_at_asc"
            UpdatedAtDesc = "updated_at_desc"
            NameAsc = "name_asc"
            NameDesc = "name_desc"
            StatusAsc = "status_asc"
            StatusDesc = "status_desc"
            VersionAsc = "version_asc"
            VersionDesc = "version_desc"

        class Config:
            use_enum_values = True

        order_by: OrderBy = OrderBy.CreatedAtAsc

    class Config:
        use_enum_values = True

    status: Status = Status.Unknown
    name: str = None
    id: str = None
