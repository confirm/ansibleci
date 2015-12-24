# -*- coding: utf-8 -*-
from ansibleci.test import Test
import os


class Tag(Test):
    '''
    This test checks if all tasks are properly tagged.
    '''

    def run(self):
        '''
        Run method which will be called by the framework.
        '''
        self.roles = self.helper.get_roles()

        for role in self.roles:
            name, relpath, abspath = role
            dir_path = os.path.join(abspath, 'tasks')
            items = self.helper.get_yaml_items(dir_path)

            for item in items:
                kwargs = {
                    'task': self.helper.get_item_identifier(item),
                     'role': name
                }
                if 'tags' in item:
                    if self.config.TAG_ROLE_NAME:
                    	tags = item['tags']
                    	if (isinstance(tags, list) and name in tags) or tags == name:
                            self.passed('Task "{task}" in role {role} is tagged with the role name'.format(**kwargs))
                        else:
                            self.failed('Task "{task}" in role {role} is not tagged with the role name'.format(**kwargs))
                    else:
                    	self.passed('Task "{task}" in role {role} is tagged'.format(**kwargs))
                else:
                    self.failed('Task "{task}" in role {role} is untagged'.format(**kwargs))
