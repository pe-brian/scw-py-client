from .models.rdb.privileges import Privileges
from .models.rdb.user import User
from .models.region import Region
from .models.rdb.database import Database
from .models.rdb.instance import Instance
from .models.pagination import Pagination
from .scw_api import ScwAPI

from pydantic import validate_arguments

import requests
import json


class Rdb(ScwAPI):

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
            f"/instances/{instance.id}/databases", ScwAPI.Method.POST, data=database.dict())))

    @validate_arguments
    def delete_database(self, instance: Instance, database: Database):
        self.request(
            f"/instances/{instance.id}/databases/{database.name}", ScwAPI.Method.DELETE, data=database.dict())

    # USERS

    @validate_arguments
    def list_users(
        self,
        instance: Instance,
        name: str = None,
        ordering: User.Ordering = User.Ordering(),
        pagination: Pagination = Pagination()
    ): return [User(**data) for data in json.loads(
            self.request(f"/instances/{instance.id}/users", data={
                "name": name} | pagination.dict() | ordering.dict()))["users"]]

    @validate_arguments
    def create_user(
        self,
        instance: Instance,
        user: User,
        password: User.Password
    ):
        try:
            return User(**json.loads(self.request(
                f"/instances/{instance.id}/users", ScwAPI.Method.POST, data=user.dict() | {"password": password})))
        except requests.exceptions.HTTPError:
            raise ValueError("Unable to create user")

    @validate_arguments
    def update_user(
        self,
        instance: Instance,
        user: User,
        password: User.Password = None
    ): return User(**json.loads(self.request(
            f"/instances/{instance.id}/users/{user.name}", ScwAPI.Method.PATCH, data=user.dict() | {
                "password": password})))

    @validate_arguments
    def delete_user(self, instance: Instance, user: Database):
        self.request(
            f"/instances/{instance.id}/users/{user.name}", ScwAPI.Method.DELETE, data=user.dict())

    # PRIVILEGES

    @validate_arguments
    def list_privileges(
        self,
        instance: Instance,
        database_name: str = None,
        user_name: str = None,
        ordering: Privileges.Ordering = Privileges.Ordering(),
        pagination: Pagination = Pagination()
    ): return [Privileges(**data) for data in json.loads(
            self.request(f"/instances/{instance.id}/privileges", data={
                "database_name": database_name, "user_name": user_name
            } | pagination.dict() | ordering.dict()))["privileges"]]

    @validate_arguments
    def set_user_privileges(self, instance: Instance, privileges: Privileges):
        return Privileges(**json.loads(self.request(
            f"/instances/{instance.id}/privileges", method=ScwAPI.Method.PUT, data=privileges.dict())))
