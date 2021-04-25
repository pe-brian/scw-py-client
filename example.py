from api.scaleway_registry_api import ScalewayRegistryAPI
from api.scaleway_functions_api import ScalewayFunctionsAPI

if __name__ == "__main__":

    registry_api = ScalewayRegistryAPI()
    print(registry_api.list_images())

    functions_api = ScalewayFunctionsAPI()
    print(functions_api.list_containers())
