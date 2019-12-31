from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = "static/"
    file_overwrite = False

class DefaultStorage(S3Boto3Storage):
    location = "default/"