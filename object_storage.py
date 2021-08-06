from models.region import Region
import boto3
import os


class ObjectStorage:

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
        return self.s3.create_bucket(Bucket=name)
