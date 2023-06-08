from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) #for holding data and making sure the content of the class dont change (immutable):
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path