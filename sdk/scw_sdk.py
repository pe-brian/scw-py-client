from models.region import Region
import requests
import json
import os


class ScwSDK:

    def __init__(self, name: str, version: str, region: Region = Region.FrPar):
        token = os.getenv("SCW_API_SECRET_KEY")
        if not token:
            raise Exception("SCW_API_SECRET_KEY must be defined as environment variable")
        self.API_url = f"https://api.scaleway.com/{name}/{version}/regions/{region.value}"
        self.headers = {
            "accept": "application/json",
            "X-Auth-Token": token,
            "Content-Type": "application/json"
        }

    def request(self, url, method="GET", data={}):
        if method == "GET":
            res = requests.get(self.API_url + url, headers=self.headers, params=data)
        elif method == "POST":
            res = requests.post(self.API_url + url, headers=self.headers, data=json.dumps(ScwSDK._clean_dict(data)))
        elif method == "PATCH":
            res = requests.patch(self.API_url + url, headers=self.headers, data=json.dumps(ScwSDK._clean_dict(data)))
        elif method == "DELETE":
            res = requests.delete(self.API_url + url, headers=self.headers)
        else:
            raise Exception(f"Unhandled method: {method}")
        if not res.ok:
            print(res.text)
        res.raise_for_status()
        if method != "DELETE":
            return json.dumps(res.json(), indent=4, sort_keys=True)

    @classmethod
    def _clean_dict(cls, d):
        if not isinstance(d, dict):
            return d
        return dict((k, cls._clean_dict(v)) for k, v in d.items() if v is not None)
