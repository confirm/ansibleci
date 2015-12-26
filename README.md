Purpose
=======

We've created _Ansible CI tests_ to run CI tests against an existing Ansible project before changes are merged into the active development tree.

Most of the time we're working with `git` and we make use of pull/merge requests in Git platforms like GitHub, GitLab or Stash.
When users sent pull/merge requests to merge their changes into the active development tree, someone had to check their commits in advance.
While some of the changes are quite complex to check automatically, we noticed that a lot of the issues we had with changes could easily be tested in a most automated way.

So we started a new CI project to test if the commited changes meet our guidelines. For example if every task is properly tagged or if there are existing Readme files for all roles.

Feel free to use this CI framework for your own standalone Ansible project, integrate it in your own Travis CI or Gitlab CI.
We try to provide some default tests which we're using every day. However, you can easily create new tests which meet your personal requirements.

Installation
============

Install via PyPi / pip
----------------------

You can install _Ansible CI tests_ via `pip` - the Python package manager:

```bash
pip install ansibleci
```

Clone git repository
--------------------

To use the [git repository](https://github.com/confirm/ansible-ci-tests) you've to clone it:

```bash
git clone https://github.com/confirm/ansible-ci-tests.git
cd ansible-ci-tests/
```

You can switch between branches and versions by executing:

```bash
git checkout BRANCH|TAG
```

Please note that we're using [Vincent Driessen's gitflow model](http://nvie.com/posts/a-successful-git-branching-model/), which means:

* the `develop` branch is always our __bleeding edge development branch__
* the `master` branch is always our __latest stable branch__
* `release-*` branches are __only temporary__ and will be removed once the release is tagged
* we're using __tags__ (aka `vMAJOR.MINOR.BUGFIX`) to create new __releases__

Download release
----------------

To manually download a release, browse to the [releases page](https://github.com/confirm/ansible-ci-tests/releases) and fetch `.zip` or `.tar.gz` file.
Unpack the file on your system and you're ready to go.

Usage
=====

Standalone
----------

To use _Ansible CI tests_ as a standalone module you've to [install](#installation) it first, then you can run it by executing:

```bash
./test.py
```

You might need to configure [configure](#configuration) it before it works.

__Hint:__ If you've installed _Ansible CI tests_ via `pip` then you might need to download the [test.py script](test.py) manually.

Python module
-------------

_Ansible CI tests_ is a Python module and can be used in any Python script. Make sure you've [installed](#installation) the `ansibleci/` directory as __system-wide Python module__ (e.g. in `site-packages`), in your __Python virtualenv__ or in your current __project directory__.

There's currently no API documentation available. However, you can easily have a look at the `ansibleci` module and read the __class and method descriptions__.

Here's an example how to use the `ansibleci` Python module in your script:

```python
from ansibleci.config import Config
from ansibleci.runner import Runner
import myapp.settings

# Create a new ansibleci Config instance, which is used by the Runner.
config = Config(load_defaults=True)

# Add your own settings module to the Config instance.
# Your own settings will overwrite the defaults.
config.add_module(myapp.mysettings)

# Create a new runner instance and run the tests.
Runner(config).run()
```

Alternatively you can have a look at the [test.py script](test.py).

Configuration
=============

Defaults
--------

_Ansible CI tests_ is designed to be flexible and dynamic, therefor not everything is hard coded in tests.
To get an overview over all customisable settings you should have a look at the [defaults](ansibleci/defaults.py).

__IMPORTANT:__ Do not change the defaults because they're part of the core. Read the next chapter to customise the settings.

Custom settings
---------------

While the [defaults](ansibleci/defaults.py) are part of the core, you can easily overwrite them by specifying a `settings.py` next to the `test.py`.
The `test.py` script will automatically load your `settings.py` and evaluate the settings.
In `settings.py` you can easily overwrite the defaults and add new settings for your own test modules.

Please note that you've the power of Python in your `settings.py`, which means you can easily `remove()` or `append()` items to existing lists.
Here's an example of a `settings.py`:

```python
from ansibleci.defaults import *

ROLES = '../../ansible-confirm/roles/'

ENABLED_TESTS.remove('ansibleci.tests.readme.Readme')
ENABLED_TESTS.append('confirmci.guidelines.Guidelines')
```

Tests
=====

Please note that you can control the enabled tests with the `ENABLED_TESTS` [settings](#custom-settings) list.

ansibleci.tests.handler.Handler
-------------------------------

Test to check if all defined handlers in `tasks/*` are really available in one of the `handlers/*` files.

ansibleci.tests.readme.Readme
-----------------------------

Test to check if all roles have a Readme file in place.

If the `README_CHECK_DEFAULTS` config flag is set to `True`, then it will also check if the role's default variables are mentioned in the role's Readme file.

The name of the Readme file is controled with the `README_FILENAME` config variable

ansibleci.tests.tag.Tag
-----------------------

Test to check if all tasks are tagged.

If the `TAG_ROLE_NAME` config flag is set to `True`, the test will also make sure that all tasks are tagged with the role's name.

Writing own tests
=================

You can easily write own test modules / classes by inheriting from the [ansibleci.test.Test class](ansibleci/test.py).

Just have a look at the existing test modules for an example and make sure you add your new test module / class to the `ENABLED_TESTS` config list.

Contribution
============

We would be happy to get new contributors. Feel free to open issues and send us merge requests.

Please note that we use [Vincent Driessen's gitflow model](http://nvie.com/posts/a-successful-git-branching-model/), so make sure you create proper feature branches.

All __branches must be properly named__, which means:

* `develop` is the bleeding-edge __development branch__
* `master` is the latest __stable branch__
* `hotfix-*` branches are __hotfix branches__
* `release-*` branches are __release branches__

__Feature branches__ have no fix naming scheme, though their name should describe the feature accordingly.

We're using __semantic versioning__, which means:

* version __tags__ are named `vMAJOR.MINOR.BUGFIX`
* __release branches__ are named `release-MAJOR.MINOR`

Also make sure you use __proper commit messages__ and __prefix__ them with:

* `FEATURE: Added new foobar feature`
* `BUGFIX: Fixed foobar bug`
* `DOCS: Updated the documentation for foobar`
* `REFACTOR: Refactored code of foobar` _which didn't affect the meaning of the code itself_

If there's an issue available (especially for bugs) make sure you mention the __issue number__ it in the git commit message as well:

* `FEATURE #42: Added new foobar feature`
* `BUGFIX #42: Fixed foobar bug`

License
=======

This project is licensed under [MIT](http://opensource.org/licenses/MIT).
