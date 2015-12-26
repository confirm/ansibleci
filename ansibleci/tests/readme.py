from ansibleci.test import Test
import os


class Readme(Test):
    '''
    This test checks all README.md files.
    '''

    def run(self):
        '''
        Run method which will be called by the framework.
        '''
        self.roles = self.helper.get_roles()
        self.test_readme()

    def test_readme(self):
        '''
        Tests the existence of role's README files and if the README files
        exists it will call the test_defaults() for each role.
        '''
        readme_filename = self.config.README_FILENAME

        for name, path in self.roles.iteritems():
            readme = os.path.join(path, readme_filename)
            if os.path.isfile(readme):
                self.passed('Readme file for role {role} is existing'.format(role=name))
                self.test_defaults(name=name, path=path, readme=readme)
            else:
                self.failed('Readme file for role {role} is missing'.format(role=name))

    def test_defaults(self, name, path, readme):
        '''
        Tests if all variables in the defaults/main.yml are documented in the
        role's Readme file.
        '''
        if not self.config.README_CHECK_DEFAULTS:
            return

        defaults = os.path.join(path, 'defaults/main.yml')

        if not os.path.isfile(defaults):
            return

        with open(readme, 'r') as f:
            readme_content = f.read()

        for var in self.helper.read_yaml(defaults).keys():
            kwargs = {'var': var, 'role': name}
            if var in readme_content:
                self.passed('Default variable {var} of role {role} is mentioned in role\'s Readme file'.format(**kwargs))
            else:
                self.failed('Default variable {var} of role {role} is not mentioned in role\'s Readme file'.format(**kwargs))
