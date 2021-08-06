# from api.scw_registry_api import ScwRegistryAPI
# from api.scw_functions_api import ScwFunctionsAPI
from api.scw_database_sdk import ScwDataBaseSDK

if __name__ == "__main__":

    # registry_api = ScwRegistryAPI()
    # print(registry_api.list_images())

    # functions_api = ScwFunctionsAPI()
    # containers = functions_api.list_containers()
    # print(containers)
    # container.timeout = 20000
    # container.environment_variables["SECRET_KEY"] = "azertyuiop123_"
    # print(container)
    # functions_api.update_container("f32701bc-3627-4bb8-8117-32487448b5bc", environment_variables=container.environment_variables, timeout=container.timeout)
    # functions_api.deploy_container(container.id)
    # logs = functions_api.list_logs(application_id="f32701bc-3627-4bb8-8117-32487448b5bc", pagination=Pagination(page_size=3000))
    # for log in logs:
    #     print(f"{log.message}")

    database_api = ScwDataBaseSDK()
    print(database_api.list_instances())
