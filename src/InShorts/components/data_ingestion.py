import os
import urllib.request as request
import zipfile
from InShorts.logging import logger
from InShorts.utils.common import get_size
from pathlib import Path
from InShorts.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
        # print(self.config.source_URL)
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL, 
                filename = self.config.local_data_file)
            logger.info(f"Downloaded file {filename} with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        print(self.config.local_data_file)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)