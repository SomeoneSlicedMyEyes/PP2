from os import path
from configparser import ConfigParser
from collections import namedtuple


DatabaseConfig = namedtuple('DatabaseConfig', 'host database user password')

def load_database_config(filename='lab10/database.ini', section='postgresql') -> DatabaseConfig:
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return DatabaseConfig(**config)