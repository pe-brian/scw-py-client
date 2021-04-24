from scaleway_api import ScalewayAPI

if __name__ == "__main__":

    api = ScalewayAPI()
    print(api.list_containers())
