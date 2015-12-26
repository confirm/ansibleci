# -*- coding: utf-8 -*-
from ansibleci.test import Test
from ansibleci.logger import Logger
from ansibleci.helper import Helper


class Runner:
    '''
    Runner class which executes all tests.
    '''

    def __init__(self, config):
        '''
        Class constructor which caches the config instance for later access and
        creates the Logger and Helper instances.
        '''
        self.config     = config
        self.logger     = Logger()
        self.helper     = Helper(config=config)
        self.has_passed = True

    def get_test_classes(self):
        '''
        Returns a list of all enabled test classes.

        The method will only lookup the test classes on the first invoke and
        cache them for all further lookups.
        '''

        try:
            return self.test_classes

        except AttributeError:

            self.test_classes = []

            for test in self.config.ENABLED_TESTS:

                # Get module and class name.
                chunks     = test.split('.')
                modulename = '.'.join(chunks[:-1])
                clsname    = chunks[-1]

                # Sanity check for existing module.
                try:
                    module = __import__(modulename, fromlist=[modulename])
                except ImportError as e:
                    raise ImportError('Could not import {module} ({message})'.format(module=modulename, message=e.message))

                # Sanity check for existing class.
                try:
                    cls = getattr(module, clsname)
                except AttributeError:
                    raise AttributeError('Test module {module} has no class named {clsname}'.format(module=modulename, clsname=clsname))

                # Sanity check for class inheritance.
                if not issubclass(cls, Test):
                    raise Exception('Test class {test} must be a subclass of ansibleci.test.Test'.format(test=test))

                self.test_classes.append(cls)

            return self.test_classes

    def run(self):
        '''
        Runs all enabled tests.
        '''
        # Run all tests.
        for cls in self.get_test_classes():

            # Print informational message.
            self.logger.info('Running {cls.__name__} test...'.format(cls=cls))

            # Create new test instance.
            test = cls(runner=self)

            # Run test and evaluate result.
            if test._run():
                self.logger.passed('Test {cls.__name__} succeeded!'.format(cls=cls))
            else:
                self.logger.failed('Test {cls.__name__} failed!'.format(cls=cls))
                self.has_passed = False

        # Print summary.
        if self.has_passed:
            self.logger.passed('Summary: All tests passed!')
        else:
            self.logger.failed('Summary: One or more tests failed!')

        return self.has_passed
