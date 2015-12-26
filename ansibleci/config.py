# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
