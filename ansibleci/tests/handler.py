from ansibleci.test import Test
import os


class Handler(Test):
    '''
    This test checks if all notified handlers in roles are really existing.
    '''

    def run(self):
        '''
        Run method which will be called by the framework.
        '''
        self.roles = self.helper.get_roles()

        notifies = self.get_notifies()
        handlers = self.get_handlers()

        for role, notifies in notifies.iteritems():
            for notify in notifies:
                kwargs = {'role': role, 'notify': notify}
                if notify in handlers:
                    self.passed('Handler "{notify}" of role {role} found'.format(**kwargs))
                else:
                    self.failed('Handler "{notify}" of role {role} not found'.format(**kwargs))

    def parse_yaml_files(self, dir_path, param):
        result = []

        if not os.path.isdir(dir_path):
            return []

        for filename in os.listdir(dir_path):

            path  = os.path.join(dir_path, filename)
            items = self.helper.read_yaml(path)

            for item in items:
                if param in item:
                    item = item[param]
                    if isinstance(item, list):
                        result.extend(item)
                    else:
                        result.append(item)

        return result

    def get_notifies(self):
        notifies = {}

        for role in self.roles:
            name, relpath, abspath = role
            dir_path               = os.path.join(abspath, 'tasks')
            role_notifies          = self.helper.get_yaml_items(dir_path=dir_path, param='notify')
            if role_notifies:
                notifies[name] = role_notifies

        return notifies

    def get_handlers(self):
        handlers = []

        for role in self.roles:
            name, relpath, abspath = role
            dir_path               = os.path.join(abspath, 'handlers')
            handlers.extend(self.helper.get_yaml_items(dir_path=dir_path, param='name'))

        return handlers
