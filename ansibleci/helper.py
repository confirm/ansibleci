# -*- coding: utf-8 -*-
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
        try:
            return item['name']
        except AttributeError:
            return 'unknown'
