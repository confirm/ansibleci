# -*- coding: utf-8 -*-
class Test(object):
    '''
    This is the abstract class for all tests, which means all concrete test
    classes must inherit from this class.
    '''

    def __init__(self, runner):
        '''
        Class constructor which sets the runner instance.
        '''
        self.runner     = runner
        self.config     = runner.config
        self.helper     = runner.helper
        self.has_passed = True

    def passed(self, message):
        '''
        Marks a (sub-)test as passed.
        This will not change the result of the whole test.
        '''
        self.runner.logger.test_passed(message)

    def failed(self, message):
        '''
        Marks a (sub-)test as failed.
        This will change the result of the whole test to FAILED.
        '''
        self.runner.logger.test_failed(message)
        self.has_passed = False

    def _run(self):
        '''
        Runs the test and returns a boolean if the test has passed or not.
        '''
        if not hasattr(self, 'run'):
            raise AttributeError('Test {test} has no run() method implemented'.format(test=self.__class__.__name__))

        self.run()

        return self.has_passed