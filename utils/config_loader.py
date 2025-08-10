import os
import yaml
from pathlib import Path

def load_config(config_path: str = "config/config.yaml") -> dict:
    """Load configuration from YAML file
    
    Args:
        config_path (str): Path to config file, using forward slashes
        
    Returns:
        dict: Configuration dictionary
    """
    # Get absolute path to config file
    root_dir = Path(__file__).parent.parent
    config_file = os.path.join(root_dir, config_path)
    
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config