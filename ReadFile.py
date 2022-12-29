
# Imports:
import boto3
import os
from Constants import FILENAME, FILE_PATH, BUCKET_NAME


class LinksFile:
    '''
    A class to read and download the file with the links that is on AWS cloud.
    '''
    def __init__(self):
        # use Amazon S3
        self.s3 = boto3.resource("s3")

    def download_file(self):
        '''
        A function to download the file from the cloud.
        :return: None
        '''
        try:
            self.s3.download_file(Bucket=BUCKET_NAME, Key=FILENAME, Filename=FILE_PATH)
        except:
            print("Could not download file")

    def read_file(self):
        '''
        A function to read the file from the cloud.
        :return: A list of the rows in the file.
        '''
        bucket = BUCKET_NAME
        self.s3 = boto3.client("s3")
        result = self.s3.list_objects(Bucket=bucket)
        file_data = list()
        for o in result.get('Contents'):
            data = self.s3.get_object(Bucket=bucket, Key=o.get('Key'))
            contents = data['Body'].read()
            rows = contents.decode("utf-8").split('\r\n')
            file_data = rows
        return file_data

    def delete_file(self, path):
        '''
        A function to delete file from current service.
        :param path: A path to the file to delete.
        :return: None.
        '''
        os.remove(path)


