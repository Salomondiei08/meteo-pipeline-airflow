import boto3
from secret_key import LINODE_ACCESS_KEY_ID, LINODE_SECRET_ACCESS_KEY, LINODE_S3_ENDPOINT_URL


def upload_file_to_server(filename):
    s3 = boto3.client('s3',
                      region_name='us-southeast-1',
                      endpoint_url=LINODE_S3_ENDPOINT_URL,
                      aws_access_key_id=LINODE_ACCESS_KEY_ID,
                      aws_secret_access_key=LINODE_SECRET_ACCESS_KEY,
                      )
    # Filename - File to upload
    # Bucket - Bucket to upload to (the top level directory under AWS S3)
    # Key - S3 object name (can contain subdirectories). If not specified then file_name is used
    s3.upload_file(Filename=filename, Bucket='airflow-project',
                   Key=filename)
