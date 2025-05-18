from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass
class Config:
    calendar_to_sync: str
    google_crendentials_path: Path
    disable_encryption: bool

    @staticmethod
    def load() -> 'Config':
        # load the configration from json file that can be passed as a environment varaiable path
        # or from the default path
        import os
        import json
        config_path = Path(os.getenv('CALENDAR_SYNC_CONFIG_PATH', 'config.json')).expanduser()
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        return Config(
            calendar_to_sync=config_data.get('calendar_to_sync', 'primary'),
            google_crendentials_path=Path(config_data.get('google_crendentials_path', 'credentials.json')),
            disable_encryption=config_data.get('disable_encryption', False)
        )

