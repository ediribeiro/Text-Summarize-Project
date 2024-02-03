import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from pathlib import Path
from textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(
        self,
        config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f'Downloaded {filename} to {headers}')
        else:
            logger.info(f'File {get_size(Path(self.config.local_data_file))} size, already exists')
            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f'Extracted {unzip_path} to {self.config.root_dir}')