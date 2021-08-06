# Scaleway-SDK

## Rdb :

- list_instances
- create_database
- create_user
- set_user_privileges
- update_user
- delete_user
- delete_database

```python
from scw_sdk.models.rdb import Privileges, User, Database
from scw_sdk.core import RdbSDK

rdb = sdk.Rdb()

instances = rdb.list_instances()
instance = instances[0]

test_database = rdb.create_database(instance=instance, database=Database(name="test_database"))
test_user = rdb.create_user(
    instance=instance, user=User(name="test_user"), password=User.Password("!8Aa126dsds"))
rdb.set_user_privileges(instance=instance, privileges=Privileges(
    database_name=test_database.name, user_name=test_user.name, permission=Privileges.Permission.ReadWrite))
test_user = rdb.update_user(instance=instance, user=test_user, password=User.Password("@8Aa126dsds"))
rdb.delete_user(instance=instances[0], user=test_user)
rdb.delete_database(instance=instance, database=test_database)
```

## Registry :

- list_images
- get_image
- update_image
- delete_image

```python
from scw_sdk.core import RegistrySDK

registry = RegistrySDK()
images = registry.list_images()
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
from scw_sdk.core import FunctionSDK

functions = FunctionSDK()
containers = functions.list_containers()
```

## Object Storage :

- list buckets
- create a bucket

```python
from scw_sdk.core import ObjectStorageSDK

object_storage = sdk.ObjectStorage()
buckets = object_storage.list_buckets()
bucket = object_storage.create_bucket("shoptero")
```