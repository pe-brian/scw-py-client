# scaleway-SDK

## Databases (Rdb) :

- list_instances
- create_database
- create_user
- set_user_privileges
- update_user
- delete_user
- delete_database

```python
from models.rdb.privileges import Privileges
from models.rdb.user import User
from models.rdb.database import Database
from scw_rdb_sdk import ScwRdbSDK

rdb_sdk = ScwRdbSDK()

instances = rdb_sdk.list_instances()
instance = instances[0]

test_database = rdb_sdk.create_database(instance=instance, database=Database(name="test_database"))
test_user = rdb_sdk.create_user(
    instance=instance, user=User(name="test_user"), password=User.Password("!8Aa126dsds"))
rdb_sdk.set_user_privileges(instance=instance, privileges=Privileges(
    database_name=test_database.name, user_name=test_user.name, permission=Privileges.Permission.ReadWrite))
test_user = rdb_sdk.update_user(instance=instance, user=test_user, password=User.Password("@8Aa126dsds"))
rdb_sdk.delete_user(instance=instances[0], user=test_user)
rdb_sdk.delete_database(instance=instance, database=test_database)
```

## Registry :

- list_images
- get_image
- update_image
- delete_image

```python
from scw_registry_sdk import ScwRegistrySDK

registry_api = ScwRegistrySDK()
images = registry_api.list_images()
```

## Functions :

- list_containers
- get_container
- create_container
- deploy_container
- update_container
- delete_container
- list_namespaces
- get_namespace
- create_namespace
- update_namespace
- delete_namespace
- list_functions
- get_function
- create_function
- deploy_function
- update_function
- delete_function
- list_crons
- get_cron
- create_cron
- update_cron
- delete_cron
- list_logs

```python
from scw_functions_sdk import ScwFunctionsSDK

functions_api = ScwFunctionsSDK()
containers = functions_api.list_containers()
```

## Object Storage :

- list buckets
- create a bucket

```python
from object_storage import ObjectStorage

object_storage = ObjectStorage()
buckets = object_storage.list_buckets()
bucket = object_storage.create_bucket("shoptero")
```