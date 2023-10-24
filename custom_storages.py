from django.conf import settings
from storages.backends.s3boto3 import S3BotoStorage


class CustomS3BotoStorage(S3BotoStorage):
    location = settings.AWS_MEDIA_LOCATION
