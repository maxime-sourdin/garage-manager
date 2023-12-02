import os
import garage_admin_sdk
import time
from garage_admin_sdk import Configuration
from dotenv import load_dotenv
from bucket import bucket_exist,inspect_bucket,delete_bucket,create_bucket
from keys import create_key,search_key,delete_key,key_exist

load_dotenv()

s3_config = Configuration(
    host = os.getenv('S3_ADMIN_HOST'),
    access_token=os.getenv('S3_ADMIN_TOKEN')
)

s3_project_name = os.getenv('S3_PROJECT_NAME')
s3_bucket_name = os.getenv('S3_BUCKET_NAME').lower()
if os.getenv('S3_PROJECT_ENV') is not None:
   s3_project_env = os.getenv('S3_PROJECT_ENV')
   s3_project_name = s3_project_name + "-" + s3_project_env
   s3_bucket_name = s3_bucket_name + "-"+ s3_project_name 


def create_project(project_name, bucket_name,s3_config):
   key_name = project_name
   alias = bucket_name
   try:
    with garage_admin_sdk.ApiClient(s3_config) as api_client:
        if key_exist(key_name,api_client) is False:
            key_id, key_name, key_secret = create_key(key_name,api_client)
        if bucket_exist(bucket_name,api_client) is False:
            create_bucket(bucket_name,alias,key_id,api_client)        
   except garage_admin_sdk.ApiException as e:
        print(time.strftime("%H:%M:%S"), "- Unable to create project - ", project_name)
        print(e)
      
def delete_project(project_name,s3_config):
   bucket_name = project_name
   try:
    with garage_admin_sdk.ApiClient(s3_config) as api_client:
        key_id, key_name = search_key(project_name,api_client)
        bucket_id = inspect_bucket(bucket_name,api_client)
        delete_key(key_id,api_client)
        delete_bucket(bucket_id,api_client)
        print(time.strftime("%H:%M:%S"), "- ", project_name, "deleted ")
   except garage_admin_sdk.ApiException as e:
        print(time.strftime("%H:%M:%S"), "- Unable to delete project - ", project_name)
        print(e)

create_project(s3_project_name, s3_bucket_name,s3_config)
#delete_project(s3_project_name)