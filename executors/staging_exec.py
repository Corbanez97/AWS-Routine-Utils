import json
from connections.s3_connection import S3Connection

class StagingExecutor:
    
    def __init__(self, source_path: str, final_path: str, archive_or_delete: str = "archive", py_exec_path: str = None, py_exec_args: dict = None) -> None:
        self.source_path = source_path
        self.final_path = final_path
        self.archive_or_delete = archive_or_delete
        self.py_exec_path = py_exec_path
        self.py_exec_args = py_exec_args
        ## this atribute should be set up by the DataLake/DataWarehouse class
        with open('keys/connex.json', 'r') as temp:
            connex = json.load(temp)
        self.s3 = S3Connection(bucket_name = 'lake-s3-dev/', key = connex['DEV']['s3']['key'], secret = connex['DEV']['s3']['secret'])
        

    def transfer(self) -> None:
        
        if not self.py_exec_path:
            self.s3.move(self.s3.bucket_name + self.source_path, self.s3.bucket_name + self.final_path)
            
        elif self.py_exec_path:
            import sys
            sys.path.insert(1, self.py_exec_path)
            import py_exec
            
            if not self.py_exec_args:
                print('Python Executor does not require arguments')
            
            elif self.py_exec_args:
                print(f'Python Executor is running with the following parameters:\n{self.py_exec_args}')
                py_exec.main(self.parent, self.dump, **self.py_exec_args)
                
    def post_staging(self) -> None:
                
        if self.archive_or_delete == 'archive':
            print(f'File from landing will be moved to archive folder: {self.final_path.split("/", 1)[-1]}')
            self.s3.move(self.s3.bucket_name + self.source_path, self.s3.bucket_name + "archive/" + self.final_path.split("/", 1)[-1])
            self.s3.delete(self.s3.bucket_name + self.source_path)
            
        elif self.archive_or_delete == 'delete':
            print('File will be deleted from landing')
            self.s3.delete(self.s3.bucket_name + self.source_path)
        