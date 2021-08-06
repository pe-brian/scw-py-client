from sdk.scw_registry_sdk import ScwRegistrySDK

if __name__ == "__main__":

    registry_api = ScwRegistrySDK()
    print(registry_api.list_images())
