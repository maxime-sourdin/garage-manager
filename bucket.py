import garage_admin_sdk
import time
from garage_admin_sdk.api import bucket_api
from garage_admin_sdk.model.create_bucket_request import CreateBucketRequest
from garage_admin_sdk.model.create_bucket_request_local_alias_allow import CreateBucketRequestLocalAliasAllow
from garage_admin_sdk.model.create_bucket_request_local_alias import CreateBucketRequestLocalAlias

def create_bucket(bucket_name, alias, key_id, api_client):
    # Create an instance of the API class
    api_instance = bucket_api.BucketApi(api_client)
    create_bucket_request = CreateBucketRequest(
        global_alias=bucket_name,
        local_alias=CreateBucketRequestLocalAlias(
            access_key_id=key_id,
            alias=bucket_name,
            allow=CreateBucketRequestLocalAliasAllow(
                read=True,
                write=True,
                owner=True,
            ),
        ),
    )
    try:
        # Create a bucket
        api_response = api_instance.create_bucket(create_bucket_request)
        bucket_id = api_response['id']
        print(
            time.strftime("%H:%M:%S"),
            "- Creating bucket - ",
            bucket_name,
            " - ",
            bucket_id)
    except:
        print(
            time.strftime("%H:%M:%S"),
            "- Unable to create bucket - ",
            bucket_name,
            " - ",
            bucket_id)


def delete_bucket(bucket_id, api_client):
    # # Create an instance of the API class
    api_instance = bucket_api.BucketApi(api_client)
    try:
        api_instance.delete_bucket(bucket_id)
        print(time.strftime("%H:%M:%S"), "- Deleting bucket - ", bucket_id)
    except:
        print(
            time.strftime("%H:%M:%S"),
            "- Unable to delete bucket - ",
            bucket_id)


def list_bucket(api_client):
    # # Create an instance of the API class
    api_instance = bucket_api.BucketApi(api_client)

    try:
        # Create a bucket
        api_response = api_instance.list_buckets()
        for i in range(len(api_response)):
            bucket_id = api_response[i]['id']
            global_aliases = api_response[i]['global_aliases']
            bucket_name = global_aliases[0]
            print(
                time.strftime("%H:%M:%S"),
                "- Bucket - ",
                bucket_name,
                " - ",
                bucket_id)
            return bucket_id, bucket_name
    except:
        print(time.strftime("%H:%M:%S"), "- Unable to list bucket ")


def inspect_bucket(search, api_client):
    # # Create an instance of the API class
    api_instance = bucket_api.BucketApi(api_client)
    try:
        # Create a bucket
        api_response = api_instance.get_bucket_info(alias=search)
        bucket_id = api_response['id']
        print(time.strftime("%H:%M:%S"), "- Bucket - ", bucket_id)
        return bucket_id
    except:
        print(
            time.strftime("%H:%M:%S"),
            "- Unable to inspect bucket - ",
            bucket_id)


def bucket_exist(search, api_client):
    # Enter a context with an instance of the API client
    # # Create an instance of the API class
    api_instance = bucket_api.BucketApi(api_client)
    api_response = api_instance.list_buckets()
    for i in range(len(api_response)):
        bucket_id = api_response[i]['id']
        global_aliases = api_response[i]['global_aliases']
        bucket_name = global_aliases[0]
        if search == bucket_name:
            print(
                time.strftime("%H:%M:%S"),
                "- Bucket - ",
                bucket_name,
                " - ",
                bucket_id,
                " - ",
                global_aliases)
            return True
        else:
            print(
                time.strftime("%H:%M:%S"),
                "- Unable to find bucket - ",
                search)
            return False