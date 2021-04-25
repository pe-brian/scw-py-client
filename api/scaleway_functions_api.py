import requests
import json
import os
from models.pagination import Pagination
from models.functions.container import Container
from models.functions.namespace import Namespace
from models.functions.function import Function
from models.functions.cron import Cron
from models.functions.log import Log
from .scaleway_api import ScalewayAPI
from pydantic import validate_arguments, ValidationError


class ScalewayFunctionsAPI(ScalewayAPI):

    def __init__(self, version: str, region: str="fr-par"):
        super().__init__(name="functions", version=version, region=region)

    ### CONTAINERS ###

    @validate_arguments
    def list_containers(
        self,
        namespace_id: str=None,
        pagination: Pagination=Pagination(),
        ordering: Container.Ordering=Container.Ordering(),
        name: str=None,
        organization_id: str=None):
        return [ Container(**data) for data in json.loads(
            self.request(f"/containers", data={
                "name": name, "namespace_id": namespace_id, "organization_id": organization_id} | pagination.dict() | ordering.dict()))["containers"] ]

    @validate_arguments
    def get_container(self, id: str):
        return Container(**json.loads(self.request(f"/containers/{id}")))

    @validate_arguments
    def create_container(self, container: Container):
        return Container(**json.loads(self.request(f"/containers", method="POST", data=container.dict())))

    @validate_arguments
    def deploy_container(self, id: str):
        return Container(**json.loads(self.request(f"/containers/{id}/deploy", method="POST")))

    @validate_arguments
    def update_container(self, container: Container):
        return Container(**json.loads(self.request(f"/containers/{container.id}", method="PATCH", data=container.dict())))

    @validate_arguments
    def delete_container(self, container: Container):
        return Container(**json.loads(self.request(f"/containers/{container.id}", method="DELETE", data=container.dict())))

    ### NAMESPACES ###

    @validate_arguments
    def list_namespaces(
        self,
        pagination: Pagination=Pagination(),
        ordering: Namespace.Ordering=Namespace.Ordering(),
        name: str=None,
        organization_id: str=None):
        return [ Namespace(**data) for data in json.loads(
            self.request(f"/namespaces", data={
                "name": name, "organization_id": organization_id} | pagination.dict() | ordering.dict()))["namespaces"] ]

    @validate_arguments
    def get_namespace(self, id: str):
        return Namespace(**json.loads(self.request(f"/namespaces/{id}")))

    @validate_arguments
    def create_namespace(self, namespace: Namespace):
        return Namespace(**json.loads(self.request(f"/namespaces", method="POST", data=namespace.dict())))

    @validate_arguments
    def update_namespace(self, namespace: Namespace):
        return Namespace(**json.loads(self.request(f"/namespaces/{namespace.id}", method="PATCH", data=namespace.dict())))

    @validate_arguments
    def delete_namespace(self, namespace: Namespace):
        return Namespace(**json.loads(self.request(f"/namespaces/{namespace.id}", method="DELETE", data=namespace.dict())))

    ### FUNCTIONS ###

    @validate_arguments
    def list_functions(
        self,
        pagination: Pagination=Pagination(),
        ordering: Function.Ordering=Function.Ordering(),
        name: str=None,
        namespace_id: str=None,
        organization_id: str=None):
        return [ Function(**data) for data in json.loads(
            self.request(f"/functions", data={
                "name": name, "namespace_id": namespace_id, "organization_id": organization_id} | pagination.dict() | ordering.dict()))["functions"] ]

    @validate_arguments
    def get_function(self, id: str):
        return Function(**json.loads(self.request(f"/functions/{id}")))

    @validate_arguments
    def create_function(self, function: Function):
        return Function(**json.loads(self.request(f"/functions", method="POST", data=function.dict())))

    @validate_arguments
    def deploy_function(self, function: Function):
        return Function(**json.loads(self.request(f"/functions/{function.id}/deploy", method="POST", data=function.dict())))

    @validate_arguments
    def update_function(self, function: Function):
        return Function(**json.loads(self.request(f"/functions/{function.id}", method="PATCH", data=function.dict())))

    @validate_arguments
    def delete_function(self, function: Function):
        return Function(**json.loads(self.request(f"/functions/{function.id}", method="DELETE", data=function.dict())))

    ### CRONS ###

    @validate_arguments
    def list_crons(
        self,
        pagination: Pagination=Pagination(),
        ordering: Cron.Ordering=Cron.Ordering(),
        application_id: str=None):
        return [ Cron(**data) for data in json.loads(
            self.request(f"/crons", data={
                "application_id": application_id} | pagination.dict() | ordering.dict()))["crons"] ]

    @validate_arguments
    def get_cron(self, id: str):
        return Cron(**json.loads(self.request(f"/crons/{id}")))

    @validate_arguments
    def create_cron(self, cron: Cron):
        return Cron(**json.loads(self.request(f"/crons", method="POST", data=cron.dict())))

    @validate_arguments
    def update_cron(self, cron: Cron):
        return Cron(**json.loads(self.request(f"/crons/{cron.id}", method="PATCH", data=cron.dict())))

    @validate_arguments
    def delete_cron(self, cron: Cron):
        return Cron(**json.loads(self.request(f"/crons/{cron.id}", method="DELETE", data=cron.dict())))

    ### LOGS ###

    @validate_arguments
    def list_logs(
        self,
        pagination: Pagination=Pagination(),
        ordering: Log.Ordering=Log.Ordering(),
        application_id: str=None):
        return [ Log(**data) for data in json.loads(
            self.request(f"/logs", data={
                "application_id": application_id} | pagination.dict() | ordering.dict()))["logs"] ]
