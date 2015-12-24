# -*- coding: utf-8 -*-

#
# A list of tests to run.
#

ENABLED_TESTS = [
    'ansibleci.tests.readme.Readme',
    'ansibleci.tests.handler.Handler',
    'ansibleci.tests.tag.Tag',
]

#
# Ansible paths.
#

ROLES = '../roles'

#
# Settings for ansibleci.tests.readme.
#

# Name of the role's Readme file.
README_FILENAME='README.md'

# Should the default vars be checked?
README_CHECK_DEFAULTS = True

#
# Settings for ansibleci.tests.tag.
#

# Should the tag name be identical with the role name?
TAG_ROLE_NAME = True
