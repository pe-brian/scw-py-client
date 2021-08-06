from models.rdb.privileges import Privileges
from models.rdb.user import User
from models.rdb.database import Database
from sdk.scw_rdb_sdk import ScwRdbSDK

if __name__ == "__main__":

    rdb_sdk = ScwRdbSDK()

    instances = rdb_sdk.list_instances()
    instance = instances[0]

    test_database = rdb_sdk.create_database(instance=instance, database=Database(name="test_database"))

    test_user = rdb_sdk.create_user(
        instance=instance, user=User(name="test_user"), password=User.Password("!8Aa126dsds"))

    print(rdb_sdk.set_user_privileges(instance=instance, privileges=Privileges(
        database_name=test_database.name, user_name=test_user.name, permission=Privileges.Permission.ReadWrite)))

    print(rdb_sdk.update_user(instance=instance, user=test_user, password=User.Password("@8Aa126dsds")))

    rdb_sdk.delete_user(instance=instances[0], user=test_user)

    rdb_sdk.delete_database(instance=instance, database=test_database)
