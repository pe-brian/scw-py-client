from models.rdb.database import Database
from sdk.scw_rdb_sdk import ScwRdbSDK

if __name__ == "__main__":

    rdb_sdk = ScwRdbSDK()
    instances = rdb_sdk.list_instances()

    print(instances)

    rdb_sdk = ScwRdbSDK()
    databases = rdb_sdk.list_databases(instance=instances[0])

    print(databases)

    database = Database(name="test_database")
    print(rdb_sdk.create_database(instances[0], database))

    rdb_sdk.delete_database(instances[0], database)
