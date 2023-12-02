import time
from garage_admin_sdk.api import key_api
from garage_admin_sdk.model.add_key_request import AddKeyRequest


def create_key(key_name,api_client):
    # # Create an instance of the API class
    api_instance = key_api.KeyApi(api_client)
    try:
        # List AK
        add_key_request = AddKeyRequest(name=key_name) 
        api_response = api_instance.list_keys()
        api_response = api_instance.add_key(add_key_request)
        key_id =  api_response['access_key_id']
        key_name = api_response['name']
        key_secret = api_response['secret_access_key']
        permissions= api_response['permissions']
        buckets = api_response['buckets']
        print(time.strftime("%H:%M:%S"), "- Creating key - ", key_id, " - ", key_name, " - ", key_secret)
        return key_id, key_name, key_secret
    except:
        print(time.strftime("%H:%M:%S"), "- Unable to create key - ", key_id, " - ", key_name)

def list_keys(s3_config,api_client):
    api_instance = key_api.KeyApi(api_client)
    try:
        # List AK
        api_response = api_instance.list_keys()
        for i in range(len(api_response)):
            key_id = api_response[i]['id']
            key_name = api_response[i]['name']
            print(time.strftime("%H:%M:%S"), "- Key - ", key_id, " - ", key_name)
        return key_id
    except:
        print(time.strftime("%H:%M:%S"), "- Unable to list key")


def inspect_key(key_id,api_client):
    # # Create an instance of the API class
    api_instance = key_api.KeyApi(api_client)
    try:
        # List AK
        api_response = api_instance.get_key(id=key_id)
        key_id =  api_response['access_key_id']
        key_name = api_response['name']
        key_secret = api_response['secret_access_key']
        create_bucket= api_response['permissions']['create_bucket']
        buckets = api_response['buckets']
        for i in range(len(buckets)):
            bucket_name = buckets[i]['global_aliases'][0]
            bucket_id = buckets[i]['id']
            aliases = buckets[i]['local_aliases']
            bucket_perms = buckets[i]['permissions']
        print(time.strftime("%H:%M:%S"), "- Key inspection - ", key_id, " - ", key_name, " - ", bucket_name)
        return(bucket_id, key_id, key_name)
    except:
        print(time.strftime("%H:%M:%S"), "- Unable to inspect key - ", key_id)

def search_key(search,api_client):
    # # Create an instance of the API class
    api_instance = key_api.KeyApi(api_client)
    try:
        # List AK
        api_response = api_instance.get_key(search=search)
        key_id =  api_response['access_key_id']
        key_name = api_response['name']
        key_secret = api_response['secret_access_key']
        create_bucket= api_response['permissions']['create_bucket']
        buckets = api_response['buckets']
        for i in range(len(buckets)):
            bucket_name = buckets[i]['global_aliases'][0]
            bucket_id = buckets[i]['id']
            aliases = buckets[i]['local_aliases']
            bucket_perms = buckets[i]['permissions']
        print(time.strftime("%H:%M:%S"), "- Key found - ", search, " - ", key_id)
        return(key_id, key_name)
    except:
        print(time.strftime("%H:%M:%S"), "- Unable to find key - ", key_id)

def key_exist(search,api_client):
    # # Create an instance of the API class
    api_instance = key_api.KeyApi(api_client)
    try:
        api_response = api_instance.get_key(search=search)
        print(time.strftime("%H:%M:%S"), "- Key exist - ", search)
        return True
    except:
        print(time.strftime("%H:%M:%S"), "- Key doesn't exist - ", search)
        return False

def delete_key(key_id,api_client):
    # # Create an instance of the API class
    api_instance = key_api.KeyApi(api_client)
    try:
        # List AK
        api_instance.delete_key(id=key_id)
        print(time.strftime("%H:%M:%S"), "- Deleting key - ", key_id)
    except:
        print(time.strftime("%H:%M:%S"), "- Unable to delete key - ", key_id)