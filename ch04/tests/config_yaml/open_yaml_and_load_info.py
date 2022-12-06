import yaml

with open("config.yaml", "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

print(type(config))
print(config)
print(config.get('api_url', 'http://localhost'))

if config.get('file') is not None:
    if config.get('file').get('folder') is not None:
        if config.get('file').get('folder').get('test') is not None:
            print(config.get('file').get('folder').get('test'))


def get_value_from_yamldict(key, yaml_dict):
    """Get the value from dictionary created from YAML"""
    parameters = key.split('.')
    yaml_dict_recursive = yaml_dict
    for parameter in parameters:
        try:
            yaml_dict_recursive = yaml_dict_recursive.get(parameter)
        except AttributeError as exception:
            print(exception)
            yaml_dict_recursive = None
            break

    return yaml_dict_recursive


print(get_value_from_yamldict('api_url', config))
print(get_value_from_yamldict('file.folder.test', config))
