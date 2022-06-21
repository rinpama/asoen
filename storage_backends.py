from storages.backends.s3boto3 import S3Boto3Storage

# 画像ファイルの同名保存禁止
class MediaStorage(S3Boto3Storage):
    location ='media'
    file_overwrite=False