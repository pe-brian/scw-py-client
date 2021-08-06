from sdk.scw_rdb_sdk import ScwRdbSDK

if __name__ == "__main__":

    database_sdk = ScwRdbSDK()
    print(database_sdk.list_instances())
