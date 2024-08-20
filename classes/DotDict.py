import yaml

class DotDict(dict):
    """A dictionary that supports dot notation and can load from a YAML config file or a dictionary."""
    
    def __init__(self, config_path=None, data=None):
        if config_path:
            self.load_from_yaml(config_path)
        elif data:
            self.update(_dict_to_dotdict(data))
    
    def load_from_yaml(self, yaml_file):
        """Loads data from a YAML file and updates the DotDict."""
        with open(yaml_file, 'r') as file:
            config_dict = yaml.safe_load(file)
        
        self.update(_dict_to_dotdict(config_dict))
    
    def __getattr__(self, attr):
        return self.get(attr)
    
    def __setattr__(self, key, value):
        self.__setitem__(key, value)
    
    def __delattr__(self, item):
        self.__delitem__(item)
    
    def __getstate__(self):
        return self.__dict__
    
    def __setstate__(self, state):
        self.__dict__ = state

def _dict_to_dotdict(d):
    """Recursively converts a dictionary to a DotDict."""
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = _dict_to_dotdict(v)
    return d
