# Scaleway-Py-Client

## Rdb :

- list_instances
- create_database
- create_user
- set_user_privileges
- update_user
- delete_user
- delete_database

```python
from scw_py_client.models.rdb import Privileges, User, Database
from scw_py_client.core import RdbClient

rdbClient = RdbClient()

instances = rdbClient.list_instances()
instance = instances[0]

test_database = rdbClient.create_database(instance=instance, database=Database(name="test_database"))
test_user = rdbClient.create_user(
    instance=instance, user=User(name="test_user"), password=User.Password("password1"))
rdbClient.set_user_privileges(instance=instance, privileges=Privileges(
    database_name=test_database.name, user_name=test_user.name, permission=Privileges.Permission.ReadWrite))
test_user = rdbClient.update_user(instance=instance, user=test_user, password=User.Password("password2"))
rdbClient.delete_user(instance=instances[0], user=test_user)
rdbClient.delete_database(instance=instance, database=test_database)
```

## Registry :

- list_images
- get_image
- update_image
- delete_image

```python
from scw_py_client.core import RegistryClient

registryClient = RegistryClient()
images = registryClient.list_images()
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
from scw_py_client.core import FunctionsClient

functions_client = FunctionsClient()
containers = functions.list_containers()
```

## Object Storage :

- list buckets
- create a bucket

```python
from scw_py_client.core import ObjectStorageClient

object_storage_client = ObjectStorageClient.ObjectStorage()
buckets = object_storage_client.list_buckets()
bucket = object_storage_client.create_bucket("my_bucket_name")
```
