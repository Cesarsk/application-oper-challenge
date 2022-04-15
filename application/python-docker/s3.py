import boto3


def upload_file(file_name, bucket, object_name=None):
    session = boto3.Session()
    s3_client = session.client('s3')

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    try:
        return s3_client.upload_file(file_name, bucket, object_name)
    except Exception as e:
        raise e
