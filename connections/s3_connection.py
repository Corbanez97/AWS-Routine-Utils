import s3fs

class S3Connection:
    
    def __init__(self, bucket_name: str, key: str, secret: str) -> None:
        self.bucket_name = bucket_name
        self.s3 = s3fs.S3FileSystem(key = key, secret = secret)
        
    def get(self, source_path: str):
        return self.s3.open(path = source_path, mode = 'rb')
        
    def upload(self , source_file, final_path: str):
        self.file = source_file
        self.final_path = self.s3.open(path = final_path, mode = 'wb')
        return self.final_path.write(source_file)
        
    def move(self, source_path: str, final_path: str):
        self.source_path = self.s3.open(path = source_path, mode = 'rb')
        self.final_path = self.s3.open(path = final_path, mode = 'wb')
        return self.final_path.write(self.source_path.read())
    
    def delete(self, source_path: str):
        return self.s3.rm(path = source_path)