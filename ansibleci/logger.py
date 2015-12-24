# -*- coding: utf-8 -*-
import os
import sys


class Logger:
    '''
    Logger class which is used to print log messages to stdout and stderr.
    '''

    COLOR_GREEN      = '\033[92m'
    COLOR_GREEN_BOLD = '\033[1;92m'
    COLOR_RED        = '\033[91m'
    COLOR_RED_BOLD   = '\033[1;91m'
    COLOR_END        = '\033[0m'

    def _log(self, message, stream, color=None, newline=False):
        '''
        Logs the message to the sys.stdout or sys.stderr stream.

        When color is defined and the TERM environemnt variable contains the
        string "color", then the output will be colored.
        '''

        if color and 'TERM' in os.environ and 'color' in os.environ['TERM']:
            colorend = Logger.COLOR_END
        else:
            color = colorend = ''

        stream.write('{color}{message}{colorend}\n'.format(
            color=color,
            message=message,
            colorend=colorend
        ))

        if newline:
            sys.stdout.write('\n')

        stream.flush()

    def _log_test(self, prefix, message, stream, color):
        '''
        Wrapper method to passed a test message from test_passed() or test_failed() to
        the _log method.
        '''
        return self._log(
            message='    {prefix}: {message}'.format(prefix=prefix, message=message),
            color=color,
            stream=stream
        )

    def info(self, message):
        '''
        Logs an informational message to stdout.

        This method should only be used by the Runner.
        '''
        return self._log(
            message=message.upper(),
            stream=sys.stdout
        )

    def passed(self, message):
        '''
        Logs as whole test result as PASSED.

        This method should only be used by the Runner.
        '''
        return self._log(
            message=message.upper(),
            stream=sys.stdout,
            color=Logger.COLOR_GREEN_BOLD,
            newline=True
        )

    def failed(self, message):
        '''
        Logs as whole test result as FAILED.

        This method should only be used by the Runner.
        '''
        return self._log(
            message=message.upper(),
            stream=sys.stderr,
            color=Logger.COLOR_RED_BOLD,
            newline=True
        )

    def test_passed(self, message):
        '''
        Logs an PASSED message from inside a test.
        '''
        return self._log_test(
            prefix='PASSED',
            message=message,
            stream=sys.stdout,
            color=Logger.COLOR_GREEN
        )

    def test_failed(self, message):
        '''
        Logs an FAILED message from inside a test.
        '''
        return self._log_test(
            prefix='FAILED',
            message=message,
            stream=sys.stderr,
            color=Logger.COLOR_RED
        )
