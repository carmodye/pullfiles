import hashlib
import os
import platform
import shutil
import time

import boto3
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError
from botocore.exceptions import ParamValidationError
from botocore.exceptions import NoCredentialsError

import file_transfer

MB = 1024 * 1024
# These configuration attributes affect both uploads and downloads.
CONFIG_ATTRS = ('multipart_threshold', 'multipart_chunksize', 'max_concurrency',
                'use_threads')
# These configuration attributes affect only downloads.
DOWNLOAD_CONFIG_ATTRS = ('max_io_queue', 'io_chunksize', 'num_download_attempts')

#s3 = boto3.resource('s3')
s3 = boto3.client('s3')

def main():
    """
    Run the demonstration script for s3_file_transfer.
    """
#    file_transfer.download_with_default_configuration
def list_all(bucket, dir):
  #bucket = 'sftpdemo'
  resp = s3.list_objects(Bucket=bucket, Prefix=dir)
  #print("s3.list_objects returns", resp)
  for i in resp:
    print ( i, resp[i])
  
  

if __name__ == '__main__':
    try:
        list_all('sftpdemo','automate')

    except NoCredentialsError as error:
        print(error)
        print("To run this example, you must have valid credentials in "
              "a shared credential file or set in environment variables.")
