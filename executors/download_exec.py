import shutil
import requests
import zipfile
import io
import os
from ..connections import s3_connection
import json

class DownloaderExecutor:
    def __init__(self, requests_arguments: dict, landing_directory: str, unzip: str = None) -> None:
        self.requests_arguments = requests_arguments ##A dictionary such as: {"url": URL, "params": PARAMS, ...}
        self.landing_directory = landing_directory
        self.unzip = unzip
        self.res = None
        ## this atribute should be set up by the DataLake/DataWarehouse class
        with open(r'../keys/connex.json', 'r') as f:
            connex = json.load(f)
        self.s3 = s3_connection.S3Connection(bucket_name = 'lake-s3-dev', key = connex['DEV']['s3']['key'], secret = connex['DEV']['s3']['secret'])
        
        
    def download(self):
        self.res = requests.get(**self.requests_arguments)
        
        if self.unzip == "unzip":
            print('Will have to unzip')
            temp = zipfile.ZipFile(io.BytesIO(self.res.content))
            temp.extractall('../data/temp/' + self.landing_directory.split("/")[-2] + '/')
            extracted_files = os.listdir('../data/temp/' + self.landing_directory.split("/")[-2] + '/')
            for file in extracted_files:
                with open('../data/temp/' + self.landing_directory.split("/")[-2] + '/' + file, 'rb') as data:
                    self.s3.upload(data.read(), self.landing_directory)
            shutil.rmtree('../data/temp/' + self.landing_directory.split("/")[-2])
            
        elif not self.unzip:
            print('Does not unzip')
            self.s3.upload(self.res.content, self.landing_directory)