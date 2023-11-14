import json
import boto3
from botocore.client import Config
from app.core.config import settings

"""
    Boto3 Doc : https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
    Boto3 S3 Doc : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html
"""

class AwsBucketApi:

    def __init__(self, bucket_name = None):
        """
            Creating instance constructor method.
            bucket_name         : AWS Bucket name. If sets as None, bucket name will be pulled from settings file.
            self.bucket_name    : AWS Bucket name for using other functions
            self.bucket         : Boto3 S3 client object for using other functions.
        """
        #settings = self.get_settings()
        self.bucket_name = "boiler-smarti" #bucket_name or settings.S3_BUCKET
        self.bucket  = boto3.client("s3", 
            aws_access_key_id = settings.S3_KEY,
            aws_secret_access_key = settings.S3_SECRET,
            region_name = settings.S3_REGION,
            config = Config(signature_version='s3v4', s3 = {"addressing_style" : "path"})
        )

    def get_settings(self):
        """
            Read settings file. 
            Return : dict -> Look at the RETURN-0 on bottom.
        """
        with open("settings.json") as f:
            return json.load(f)

    def generate_presigned_url(self, filename, expires = 3600):
        """
            Create pre-signed url for file download.
            filename    : AWS Bucket object full path name. Exp : "img/example.jpg"
            expires     : Expiration time for created url in seconds.
            Return : str -> "<pre-signed url>"
        """
        return self.bucket.generate_presigned_url(
            ClientMethod = "get_object",
            ExpiresIn = expires,
            Params = {
                "Bucket" : self.bucket_name,
                "Key" : filename
            }
        )

    def generate_presigned_post_fields(self, content_type = None, path_prefix = "", expires = 3600):
        """
            Create pre-signed action link for uploading file to AWS Bucket.
            content_type    : File content mime type. Exp : "image/jpg"
            path_prefix     : Path name or file prefix. Exp : "img/"
            expires         : Expiration time for created url in seconds.
            Return : dict -> Look at the RETURN-1 on bottom.
        """
        if content_type:
            return self.bucket.generate_presigned_post(
                self.bucket_name,
                path_prefix + "${filename}",
                ExpiresIn = expires,
                Conditions = [
                    ["starts-with", "$Content-Type", ""]
                ],
                Fields = {
                    "Content-Type" : content_type
                }
            )
        else:
            return self.bucket.generate_presigned_post(
                self.bucket_name,
                path_prefix + "${filename}",
                ExpiresIn = expires,
            )

    def get_files(self, path_prefix = ""):
        """
            Get filenames and pre-signed urls of bucket object in given path.
            path_prefix : Path name or file prefix. Exp : "img/"
            
            .list_object() return RETURN-2 (look at the bottom)
            Return  : list -> [
                {"url": "<pre-signed url>", "filename" : "<filename of object>"},...
            ]
        """
        object_list = self.bucket.list_objects(
            Bucket = self.bucket_name,
            Prefix = path_prefix
        )

        if "Contents" not in object_list:
            return []

        return [{"url": self.generate_presigned_url(file.get("Key")), "filename" : file.get("Key")} \
            for file in object_list.get("Contents")]

    def delete_file(self, filename):
        """
            Delete object from AWS Bucket with given filename.
            filename    : AWS Bucket object full path name. Exp : "img/example.jpg"
            Return  : bool -> True or False
        """
        response = self.bucket.delete_object(
            Bucket = self.bucket_name,
            Key = filename
        )
        return response.get("DeleteMarker")