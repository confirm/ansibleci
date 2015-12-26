# -*- coding: utf-8 -*-
import sys
import os

#
# Ansible paths.
#

# Basedir which should point to an Ansible project.
BASEDIR = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), '..'))

# Roles directory path, relativ to BASEDIR.
ROLES = 'roles/'

#
# A list of tests to run.
#

ENABLED_TESTS = [
    'ansibleci.tests.readme.Readme',
    'ansibleci.tests.handler.Handler',
    'ansibleci.tests.tag.Tag',
]

#
# Settings for ansibleci.tests.readme.
#

# Name of the role's Readme file.
README_FILENAME = 'README.md'

# Should the default vars be checked?
README_CHECK_DEFAULTS = True

#
# Settings for ansibleci.tests.tag.
#

# Should the tag name be identical with the role name?
TAG_ROLE_NAME = True
