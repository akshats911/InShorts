from InShorts.constants import *
from InShorts.utils.common import read_yaml, create_directiories
from InShorts.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath),
        self.params = read_yaml(params_filepath)
        create_directiories([self.config[0].artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # print(self.config[0].data_ingestion)
        config = self.config[0].data_ingestion
        create_directiories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config

