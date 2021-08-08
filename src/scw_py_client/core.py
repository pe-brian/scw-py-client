from .models.region import Region
from .models.pagination import Pagination
from .models.functions import Container, Namespace, Function, Cron, Log
from .models.registry import Image
from .models.rdb import Privileges, User, Database, Instance
from .client_api import ClientAPI

from pydantic import validate_arguments
import boto3
import requests

import json
import os


class FunctionsClient(ClientAPI):

    def __init__(self, region: Region = Region.FrPar):
        super().__init__(name="functions", version="v1alpha2", region=region)

    # CONTAINERS

    @validate_arguments
    def list_containers(
        self,
        namespace_id: str = None,
        pagination: Pagination = Pagination(),
        ordering: Container.Ordering = Container.Ordering(),
        name: str = None,
        organization_id: str = None
    ): return [Container(**data) for data in json.loads(
            self.request("/containers", data={
                "name": name,
                "namespace_id": namespace_id,
                "organization_id": organization_id} | pagination.dict() | ordering.dict()))["containers"]]

    @validate_arguments
    def get_container(self, id: str):
        return Container(**json.loads(self.request(f"/containers/{id}")))

    @validate_arguments
    def create_container(self, container: Container):
        return Container(**json.loads(self.request("/containers", ClientAPI.Method.POST, data=container.dict())))

    @validate_arguments
    def deploy_container(self, id: str):
        return Container(**json.loads(self.request(f"/containers/{id}/deploy", ClientAPI.Method.POST)))

    @validate_arguments
    def update_container(self, id, container: Container):
        return Container(**json.loads(self.request(f"/containers/{id}", ClientAPI.Method.PATCH, data=container.dict())))

    @validate_arguments
    def delete_container(self, container: Container):
        return Container(**json.loads(self.request(
            f"/containers/{container.id}", ClientAPI.Method.DELETE, data=container.dict())))

    # NAMESPACES

    @validate_arguments
    def list_namespaces(
        self,
        pagination: Pagination = Pagination(),
        ordering: Namespace.Ordering = Namespace.Ordering(),
        name: str = None,
        organization_id: str = None
    ): return [Namespace(**data) for data in json.loads(
            self.request("/namespaces", data={
                "name": name, "organization_id": organization_id} | pagination.dict() | ordering.dict()))["namespaces"]]

    @validate_arguments
    def get_namespace(self, id: str):
        return Namespace(**json.loads(self.request(f"/namespaces/{id}")))

    @validate_arguments
    def create_namespace(self, namespace: Namespace):
        return Namespace(**json.loads(self.request("/namespaces", ClientAPI.Method.POST, data=namespace.dict())))

    @validate_arguments
    def update_namespace(self, namespace: Namespace):
        return Namespace(**json.loads(
            self.request(f"/namespaces/{namespace.id}", ClientAPI.Method.PATCH, data=namespace.dict())))

    @validate_arguments
    def delete_namespace(self, namespace: Namespace):
        return Namespace(**json.loads(
            self.request(f"/namespaces/{namespace.id}", ClientAPI.Method.DELETE, data=namespace.dict())))

    # FUNCTIONS

    @validate_arguments
    def list_functions(
        self,
        pagination: Pagination = Pagination(),
        ordering: Function.Ordering = Function.Ordering(),
        name: str = None,
        namespace_id: str = None,
        organization_id: str = None
    ): return [Function(**data) for data in json.loads(
            self.request("/functions", data={
                "name": name, "namespace_id": namespace_id, "organization_id": organization_id
                    } | pagination.dict() | ordering.dict()))["functions"]]

    @validate_arguments
    def get_function(self, id: str):
        return Function(**json.loads(self.request(f"/functions/{id}")))

    @validate_arguments
    def create_function(self, function: Function):
        return Function(**json.loads(self.request("/functions", ClientAPI.Method.POST, data=function.dict())))

    @validate_arguments
    def deploy_function(self, function: Function):
        return Function(**json.loads(self.request(
            f"/functions/{function.id}/deploy", ClientAPI.Method.POST, data=function.dict())))

    @validate_arguments
    def update_function(self, function: Function):
        return Function(**json.loads(
            self.request(f"/functions/{function.id}", ClientAPI.Method.PATCH, data=function.dict())))

    @validate_arguments
    def delete_function(self, function: Function):
        return Function(**json.loads(
            self.request(f"/functions/{function.id}", ClientAPI.Method.DELETE, data=function.dict())))

    # CRONS

    @validate_arguments
    def list_crons(
        self,
        pagination: Pagination = Pagination(),
        ordering: Cron.Ordering = Cron.Ordering(),
        application_id: str = None
    ): return [Cron(**data) for data in json.loads(
            self.request("/crons", data={
                "application_id": application_id} | pagination.dict() | ordering.dict()))["crons"]]

    @validate_arguments
    def get_cron(self, id: str):
        return Cron(**json.loads(self.request(f"/crons/{id}")))

    @validate_arguments
    def create_cron(self, cron: Cron):
        return Cron(**json.loads(self.request("/crons", ClientAPI.Method.POST, data=cron.dict())))

    @validate_arguments
    def update_cron(self, cron: Cron):
        return Cron(**json.loads(self.request(f"/crons/{cron.id}", ClientAPI.Method.PATCH, data=cron.dict())))

    @validate_arguments
    def delete_cron(self, cron: Cron):
        return Cron(**json.loads(self.request(f"/crons/{cron.id}", ClientAPI.Method.DELETE, data=cron.dict())))

    # LOGS

    @validate_arguments
    def list_logs(
        self,
        pagination: Pagination = Pagination(),
        ordering: Log.Ordering = Log.Ordering(),
        application_id: str = None
    ): return [Log(**data) for data in json.loads(
            self.request("/logs", data={
                "application_id": application_id} | pagination.dict() | ordering.dict()))["logs"]]


class RdbClient(ClientAPI):

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
            f"/instances/{instance.id}/databases", ClientAPI.Method.POST, data=database.dict())))

    @validate_arguments
    def delete_database(self, instance: Instance, database: Database):
        self.request(
            f"/instances/{instance.id}/databases/{database.name}", ClientAPI.Method.DELETE, data=database.dict())

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
                f"/instances/{instance.id}/users", ClientAPI.Method.POST, data=user.dict() | {"password": password})))
        except requests.exceptions.HTTPError:
            raise ValueError("Unable to create user")

    @validate_arguments
    def update_user(
        self,
        instance: Instance,
        user: User,
        password: User.Password = None
    ): return User(**json.loads(self.request(
            f"/instances/{instance.id}/users/{user.name}", ClientAPI.Method.PATCH, data=user.dict() | {
                "password": password})))

    @validate_arguments
    def delete_user(self, instance: Instance, user: Database):
        self.request(
            f"/instances/{instance.id}/users/{user.name}", ClientAPI.Method.DELETE, data=user.dict())

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
            f"/instances/{instance.id}/privileges", method=ClientAPI.Method.PUT, data=privileges.dict())))


class RegistryClient(ClientAPI):

    def __init__(self, region: Region = Region.FrPar):
        super().__init__(name="registry", version="v1", region=region)

    # IMAGES

    @validate_arguments
    def list_images(
        self,
        name: str = None,
        pagination: Pagination = Pagination(),
        ordering: Image.Ordering = Image.Ordering(),
        application_id: str = None,
        organization_id: str = None,
        project_id: str = None
    ): return [Image(**data) for data in json.loads(
            self.request("/images", data={
                "application_id": application_id,
                "organization_id": organization_id,
                "project_id": project_id, "name": name} | pagination.dict() | ordering.dict()))["images"]]

    @validate_arguments
    def get_image(self, id: str):
        return Image(**json.loads(self.request(f"/image/{id}")))

    @validate_arguments
    def update_image(self, image: Image):
        return Image(**json.loads(self.request(f"/image/{image.id}", ClientAPI.Method.PATCH, data=image.dict())))

    @validate_arguments
    def delete_image(self, image: Image):
        return Image(**json.loads(self.request(f"/images/{image.id}", ClientAPI.Method.DELETE, data=image.dict())))


class ObjectStorageClient:

    def __init__(self, region: Region = Region.FrPar):
        session = boto3.session.Session()
        endpoint_url = f'http://s3.{region.value}.scw.cloud'
        self.s3 = session.client(
            service_name='s3',
            region_name=region.value,
            use_ssl=True,
            endpoint_url=endpoint_url,
            aws_access_key_id=os.getenv("SCW_API_KEY_ID"),
            aws_secret_access_key=os.getenv("SCW_API_KEY")
        )

    def list_buckets(self):
        response = self.s3.list_buckets()
        return response['Buckets']

    def create_bucket(self, name: str):
        self.s3.create_bucket(Bucket=name)

    def enable_bucket_website(self, name: str):
        self.s3.put_bucket_website(
            Bucket=name,
            WebsiteConfiguration={
                'ErrorDocument': {'Key': 'error.html'},
                'IndexDocument': {'Suffix': 'index.html'},
            }
        )

    def upload_file_to_bucket(self, file_path: str, bucket_name: str, file_name: str):
        self.s3.upload_file(file_path, bucket_name, file_name)
