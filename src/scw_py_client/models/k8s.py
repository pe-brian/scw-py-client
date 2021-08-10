from pydantic import BaseModel
from enum import Enum


class Cluster(BaseModel):

    class Status(Enum):

        Unknow = "unknown"
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

    status: Status = Status.Unknow
    name: str = None
    id: str = None
