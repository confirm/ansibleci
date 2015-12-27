Writing tests
=============

You can easily write own test modules / classes by inheriting from the `ansibleci.test.Test class <https://github.com/confirm/ansibleci/blob/develop/ansibleci/test.py>`_.
Just have a look at the existing `test modules <https://github.com/confirm/ansibleci/tree/develop/ansibleci/tests>`_ for an example.

To run your own test make sure you add your new test module / class to the ``ENABLED_TESTS`` config list.