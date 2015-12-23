import os
import yaml

class Helper:

    def __init__(self, config):
        self.config = config

    def get_roles(self):
        '''
        Returns all roles in a list of tuples with the following structure:

            (role_name, relativ_path, absolute_path)
        '''
        roles = []

        for entry in os.listdir(self.config.ROLES):
            relpath = os.path.join(self.config.ROLES, entry)
            if os.path.isdir(relpath):
                roles.append((entry, relpath, os.path.abspath(relpath)))

        return roles


    def read_yaml(self, filename):
        '''
        Reads and parses a YAML file and returns the content.
        '''
        with open(filename, 'r') as f:
            return yaml.load(f)

