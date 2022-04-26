import requests, zipfile, io


class DownloaderExecutor:
    '''
    This class creates a downloading object and transports it to a landing folder.
    '''
    def __init__(self, requests_arguments: dict, landing_directory: str, unzip: str = None) -> None:
        self.requests_arguments = requests_arguments ##A dictionary such as: {"url": URL, "params": PARAMS, ...}
        self.landing_directory = landing_directory ##With file name in case of unzipped, without in case of zipped
        self.unzip = unzip
        self.res = None
        
        # self.py_exec_path = py_exec_path
        # self.py_exec_args = py_exec_args
        
    def download(self) -> None:
        self.res = requests.get(**self.requests_arguments)
        print(self.res)
        
        if self.unzip == 'unzip':
            print('Will have to unzip')
            temp = zipfile.ZipFile(io.BytesIO(self.res.content))
            temp.extractall(self.landing_directory)
            
            
        elif not self.unzip:
            print('Will not unzip')
            with open(self.landing_directory, 'wb') as temp:
                temp.write(self.res.content)