# -*- coding: utf-8 -*-
import os
import yaml


class Helper:
    '''
    Helper class which provides some helper methods.
    '''

    def __init__(self, config):
        '''
        Class constructor which caches the config instance for later access.
        '''
        self.config = config

    def get_roles_path(self):
        '''
        Returns the absolute path to the roles/ directory, while considering
        the BASEDIR and ROLES config variables.
        '''
        return os.path.abspath(os.path.join(self.config.BASEDIR, self.config.ROLES))

    def get_roles(self):
        '''
        Returns a key-value dict with a roles, while the key is the role name
        and the value is the absolute role path.
        '''
        roles = {}
        path  = self.get_roles_path()

        for entry in os.listdir(path):
            rolepath = os.path.join(path, entry)
            if os.path.isdir(rolepath):
                roles[entry] = rolepath

        return roles

    def read_yaml(self, filename):
        '''
        Reads and parses a YAML file and returns the content.
        '''
        with open(filename, 'r') as f:
            return yaml.load(f)

    def get_yaml_items(self, dir_path, param=None):
        '''
        Loops through the dir_path and parses all YAML files inside the
        directory.

        If no param is defined, then all YAML items will be returned
        in a list. If a param is defined, then all items will be scanned for
        this param and a list of all those values will be returned.
        '''

        result = []

        if not os.path.isdir(dir_path):
            return []

        for filename in os.listdir(dir_path):

            path  = os.path.join(dir_path, filename)
            items = self.read_yaml(path)

            for item in items:
                if param:
                    if param in item:
                        item = item[param]
                        if isinstance(item, list):
                            result.extend(item)
                        else:
                            result.append(item)
                else:
                    result.append(item)

        return result

    def get_item_identifier(self, item):
        '''
        Returns the identifier of a (task) item, which by default is the name
        param of the item. If no name param is defined then the method will
        return "unknown".

        @todo: Update this method to consider other params when name is not
        defined (e.g. "include").
        '''
        try:
            return item['name']
        except AttributeError:
            return 'unknown'
