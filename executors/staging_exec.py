import boto3


class StagingExecutor:
    
    def __init__(self, parent_directory: str, dump_directory: str, archive_or_delete: str = "archive", py_exec_path: str = None, py_exec_args: dict = None) -> None:
        self.parent = parent_directory
        self.dump = dump_directory
        self.archive_or_delete = archive_or_delete
        self.py_exec_path = py_exec_path
        self.py_exec_args = py_exec_args

    def transfer(self) -> None:
        
        if not self.py_exec_path:
            print('No transformation required. Moving file using only parent and dump')
        
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
            print('File from landing will be moved to archive folder')
        
        elif self.archive_or_delete == 'delete':
            print('File will be deleted from landing')