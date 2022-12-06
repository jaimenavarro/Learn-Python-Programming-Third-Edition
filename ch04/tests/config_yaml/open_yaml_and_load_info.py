import yaml
from customer import Customer, Customers

try:
    with open("config.yaml", "r") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
except OSError as exception:
    print(exception)
    exit(1)

print(type(config))
print(config)
print(config.get('api_url', 'http://localhost'))

################################################################
# Create object from yaml configuration
################################################################
customer = Customer(config.get('object').get('name'),
                    config.get('object').get('email'))

print(type(customer))
print(customer.__str__())

#####################################################
# Create list object from yaml configuration
#####################################################
customers = config.get('list')
customers_list = Customers(customers)

if config.get('file') is not None:
    if config.get('file').get('folder') is not None:
        if config.get('file').get('folder').get('test') is not None:
            print(config.get('file').get('folder').get('test'))


def get_value_from_yamldict(key, yaml_dict):
    """Get the value from dictionary created from YAML
            :param key: key we want to extract from the dictionary
            :param yaml_dict: dictionary created with YAML file.
            :return: yaml_dict[key] or None
    """
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

