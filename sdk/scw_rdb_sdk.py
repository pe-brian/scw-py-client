import json
from models.region import Region
from models.rdb.database import Database
from models.rdb.instance import Instance
from models.pagination import Pagination
from .scw_sdk import ScwSDK
from pydantic import validate_arguments


class ScwRdbSDK(ScwSDK):

    def __init__(self, region: Region = Region.FrPar):
        super().__init__(name="rdb", version="v1", region=region)

    # INSTANCES

    @validate_arguments
    def list_instances(
        self,
        name: str = None,
        project_id: str = None,
        organization_id: str = None,
        pagination: Pagination = Pagination(),
        ordering: Instance.Ordering = Instance.Ordering()
    ): return [Instance(**data) for data in json.loads(
            self.request("/instances", data={
                "organization_id": organization_id,
                "project_id": project_id,
                "name": name} | pagination.dict() | ordering.dict()))["instances"]]

    # DATABASES

    @validate_arguments
    def list_databases(
        self,
        instance: Instance,
        name: str = None,
        managed: bool = None,
        owner: str = None,
        ordering: Database.Ordering = Database.Ordering(),
        pagination: Pagination = Pagination()
    ): return [Database(**data) for data in json.loads(
            self.request(f"/instances/{instance.id}/databases", data={
                "owner": owner,
                "managed": managed,
                "name": name} | pagination.dict() | ordering.dict()))["databases"]]

    @validate_arguments
    def create_database(self, instance: Instance, database: Database):
        return Database(**json.loads(self.request(
            f"/instances/{instance.id}/databases", method="POST", data=database.dict())))

    @validate_arguments
    def delete_database(self, instance: Instance, database: Database):
        self.request(
            f"/instances/{instance.id}/databases/{database.name}", method="DELETE", data=database.dict())
