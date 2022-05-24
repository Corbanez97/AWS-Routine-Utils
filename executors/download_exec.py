import requests, zipfile, io
import boto3

class DownloaderExecutor:
    '''
    This class creates a downloading object and transports it to a landing folder.
    '''
    def __init__(self, bucket_name: str, requests_arguments: dict, landing_directory: str, file_name: str = None, unzip: str = None) -> None:
        self.requests_arguments = requests_arguments ##A dictionary such as: {"url": URL, "params": PARAMS, ...}
        self.bucket_name = bucket_name
        self.landing_directory = landing_directory ##With file name in case of unzipped, without in case of zipped
        self.file_name = file_name
        self.unzip = unzip

        self.res = requests.get(**self.requests_arguments)
        print(self.res)
        
        # self.py_exec_path = py_exec_path
        # self.py_exec_args = py_exec_args

    def get_client(self):
        return boto3.client('s3')

    def download(self) -> None:
        
        if self.unzip == 'unzip':
            print('Will have to unzip')
            temp = zipfile.ZipFile(io.BytesIO(self.res.content))
            for info in temp.infolist():
                name = info.filename
                s3.client.put_object(
                    Bucket = self.bucket_name,
                    Key = self.landing_directory + '/' + name,
                    Body = temp.open(name).read()
                )
            
            
        elif not self.unzip:
            print('Will not unzip')
            s3.client.put_object(
                Bucket = self.bucket_name,
                Key = self.landing_directory + '/' + self.file_name,
                Body = self.res.content
            )