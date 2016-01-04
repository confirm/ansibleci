# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 confirm IT solutions
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import sys
from subprocess import check_call, CalledProcessError


class Logger(object):
    '''
    Logger class which is used to print log messages to stdout and stderr.
    '''

    COLOR_GREEN      = '\033[92m'
    COLOR_GREEN_BOLD = '\033[1;92m'
    COLOR_RED        = '\033[91m'
    COLOR_RED_BOLD   = '\033[1;91m'
    COLOR_END        = '\033[0m'

    def __init__(self):
        '''
        Class constructor which determines if the terminal supports colors.
        '''
        try:
            check_call('[ "$(tput colors)" -ge 8 ]', shell=True)
            self.color_term = True
        except CalledProcessError:
            self.color_term = False

    def _log(self, message, stream, color=None, newline=False):
        '''
        Logs the message to the sys.stdout or sys.stderr stream.

        When color is defined and the TERM environemnt variable contains the
        string "color", then the output will be colored.
        '''

        if color and self.color_term:
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
