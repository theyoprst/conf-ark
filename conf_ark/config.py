from pathlib import Path
from typing import List
from dataclasses import dataclass

import yaml


@dataclass
class Config:
    """Configuration data object."""
    include: List[str]

    @classmethod
    def from_file(cls, path: str | Path) -> "Config":
        """
        Load configuration from a YAML file.

        Args:
            path: Path to the configuration file

        Returns:
            Config object with loaded data

        Raises:
            FileNotFoundError: If config file doesn't exist
            ValueError: If no paths are specified in config
        """
        config_file = Path(path).expanduser()
        if not config_file.exists():
            raise FileNotFoundError(f"Config file not found: {config_file}")

        with open(config_file) as f:
            config_data = yaml.safe_load(f)

        include_paths = config_data.get("include", [])
        if not include_paths:
            raise ValueError("No paths specified in config file")

        return cls(include=include_paths)
