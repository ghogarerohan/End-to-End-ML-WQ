# Entity is return type of function
# Entity is prepared with the help of dataclass  and Dataclass is decorator  

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path