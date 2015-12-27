Built-in tests
==============

Please note that you can control the enabled tests with the ``ENABLED_TESTS`` settings parameter.

ansibleci.tests.handler.Handler
-------------------------------

Test to check if all defined handlers in ``tasks/*`` are really available in one of the ``handlers/*`` files.

ansibleci.tests.readme.Readme
-----------------------------

Test to check if all roles have a Readme file in place.

If the ``README_CHECK_DEFAULTS`` config flag is set to ``True``, then it will also check if the role's default variables are mentioned in the role's Readme file.

The name of the Readme file is controled with the ``README_FILENAME`` config variable

ansibleci.tests.tag.Tag
-----------------------

Test to check if all tasks are tagged.

If the ``TAG_ROLE_NAME`` config flag is set to ``True``, the test will also make sure that all tasks are tagged with the role's name.