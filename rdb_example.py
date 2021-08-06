from models.rdb.user import User
from models.rdb.database import Database
from sdk.scw_rdb_sdk import ScwRdbSDK

if __name__ == "__main__":

    rdb_sdk = ScwRdbSDK()

    instances = rdb_sdk.list_instances()
    print(instances)

    instance = instances[0]

    users = rdb_sdk.list_users(instance=instance)
    print(users)

    user = User(name="testuser")
    print(rdb_sdk.create_user(instance=instance, user=user, password=User.Password("!8Aa126dsds")))

    print(rdb_sdk.update_user(instance=instance, user=user, password=User.Password("@8Aa126dsds")))

    rdb_sdk.delete_user(instance=instances[0], user=user)

    # databases = rdb_sdk.list_databases(instance=instance)
    # print(databases)

    # database = Database(name="test_database")
    # print(rdb_sdk.create_database(instance=instance, database))

    # rdb_sdk.delete_database(instance=instance, database)
