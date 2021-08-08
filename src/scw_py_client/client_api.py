from .models.region import Region

from typing import Any, Dict

import requests
import json
import os
from enum import Enum


class ClientAPI:

    class Method(Enum):
        GET = "GET"
        POST = "POST"
        PATCH = "PATCH"
        DELETE = "DELETE"
        PUT = "PUT"

    class Error(Exception):

        def __init__(self, *args: object):
            super().__init__(*args)

    def __init__(self, name: str, version: str, region: Region = Region.FrPar):
        token = os.getenv("SCW_API_KEY")
        if not token:
            raise Exception("SCW_API_KEY must be defined as environment variable")
        self.API_url = f"https://api.scaleway.com/{name}/{version}/regions/{region.value}"
        self.headers = {
            "accept": "application/json",
            "X-Auth-Token": token,
            "Content-Type": "application/json"
        }

    def request(self, url: str, method: Method = Method.GET, data: Dict[str, Any] = {}):
        print(json.dumps(ClientAPI._clean_dict(data)))
        if method == ClientAPI.Method.GET:
            res = requests.get(self.API_url + url, headers=self.headers, params=data)
        elif method == ClientAPI.Method.POST:
            res = requests.post(self.API_url + url, headers=self.headers, data=json.dumps(ClientAPI._clean_dict(data)))
        elif method == ClientAPI.Method.PATCH:
            res = requests.patch(self.API_url + url, headers=self.headers, data=json.dumps(ClientAPI._clean_dict(data)))
        elif method == ClientAPI.Method.DELETE:
            res = requests.delete(self.API_url + url, headers=self.headers)
        elif method == ClientAPI.Method.PUT:
            res = requests.put(self.API_url + url, headers=self.headers, data=json.dumps(ClientAPI._clean_dict(data)))
        else:
            raise Exception(f"Unhandled method: {method}")
        if not res.ok:
            raise ClientAPI.Error(res.json()["message"])
        if method != ClientAPI.Method.DELETE:
            return json.dumps(res.json(), indent=4, sort_keys=True)

    @classmethod
    def _clean_dict(cls, d):
        if not isinstance(d, dict):
            return d
        return dict((k, cls._clean_dict(v)) for k, v in d.items() if v is not None)
