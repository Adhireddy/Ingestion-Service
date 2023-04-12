
import os
from minio import Minio

# Initialize minIO client
client = Minio(
    "localhost:9000",  # Replace with your minIO server address
    access_key="minioadmin",  # Replace with your access key
    secret_key="minioadmin",  # Replace with your secret key
    secure=False,  # Set to True for SSL/TLS encrypted connections
)

# Set the path of the local folder to upload
local_folder_path = "C:\\MyLocalFolder"

# Set the name of the minIO bucket to upload to
bucket_name = "mybucket"

# Create the bucket if it doesn't exist
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

# Iterate over the files in the local folder and upload them to the minIO bucket
for root, dirs, files in os.walk(local_folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        object_name = os.path.relpath(file_path, local_folder_path).replace("\\", "/")
        client.fput_object(bucket_name, object_name, file_path)

print("Folder uploaded successfully!")


