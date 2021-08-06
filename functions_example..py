from sdk.scw_functions_sdk import ScwFunctionsSDK

if __name__ == "__main__":

    functions_api = ScwFunctionsSDK()
    containers = functions_api.list_containers()
