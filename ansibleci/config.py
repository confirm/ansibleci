# -*- coding: utf-8 -*-
class Config:
    '''
    Configuration class which can be used to load configuration parameters from
    a Python module and query them later.
    '''

    def __init__(self, load_defaults=True):
        '''
        Class constructor which initializes the internal configuration dict.
        '''
        self.config = {}

        if load_defaults:
            import ansibleci.defaults
            self.add_module(ansibleci.defaults)

    def __str__(self):
        '''
        Returns a string of all config parameters.
        '''
        return ', '.join(self.config.keys())

    def __getattr__(self, attr):
        '''
        Returns a configuration parameter.
        '''
        try:
            return self.config[attr]
        except KeyError:
            raise KeyError('Config parameter {} doesn\'t exist'.format(attr))

    def add_module(self, module):
        '''
        Adds configuration parameters from a Python module.
        '''
        for key, value in module.__dict__.iteritems():
            if key[0:2] != '__':
                self.config[key] = value
