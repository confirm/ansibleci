from ansibleci.test import Test
import os


class Handler(Test):
    '''
    This test checks if all notified handlers in roles are really existing.
    '''

    def run(self):
        '''
        Runs all tests defined in the config's ENABLED_TESTS list.
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

    def get_notifies(self):
        '''
        Returns all task notifies in form of a dict, while the key is the role
        name and the value is the notified handler string.
        '''
        notifies = {}

        for name, path in self.roles.iteritems():
            dir_path      = os.path.join(path, 'tasks')
            role_notifies = self.helper.get_yaml_items(dir_path=dir_path, param='notify')
            if role_notifies:
                notifies[name] = role_notifies

        return notifies

    def get_handlers(self):
        '''
        Returns all handlers in a simple list.
        '''
        handlers = []

        for name, path in self.roles.iteritems():
            dir_path = os.path.join(path, 'handlers')
            handlers.extend(self.helper.get_yaml_items(dir_path=dir_path, param='name'))

        return handlers
