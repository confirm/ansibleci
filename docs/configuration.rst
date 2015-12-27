Configuration
=============

Out of the box
--------------

``ansibleci`` can work out of the box if you meet the following requirements:

* you've created a new sub directory (e.g. ``test/``) in the root directory of your Ansible project
* you've put the `test.py script <https://github.com/confirm/ansibleci/blob/develop/test.py>`_ inside this directory
* you've either `installed ansibleci via pip <installation.html#pypi-pip>`_ OR manually added the `ansible ci directory <https://github.com/confirm/ansibleci/tree/develop/ansibleci>`_ inside your ``test/`` directory (next to the ``test.py`` script)
* your roles directory is called ``roles/`` and is located on the root directory of your Ansible project

If you meet all the requirements above then ``ansibleci`` can work out of the box. However, you might want to configure your `custom settings <#custom-settings>`_.

Defaults
--------

``ansibleci`` is designed to be flexible and dynamic, therefor not everything is hard coded in tests.
To get an overview over all customisable settings you should have a look at the `defaults.py <https://raw.githubusercontent.com/confirm/ansibleci/develop/ansibleci/defaults.py>`_.

**IMPORTANT:** Do not change the defaults because they're part of the core. Read the next chapter to customise the settings.

Custom settings
---------------

While the `defaults <#defaults>`_ are part of the core, you can easily overwrite them by specifying a ``settings.py`` next to the ``test.py``.
The `test.py script <https://github.com/confirm/ansibleci/blob/develop/test.py>`_ will automatically load and evaluate your ``settings.py``, where you can easily overwrite the defaults and add new settings for your own test modules.

Please note that you've the power of Python in your ``settings.py``, which means you can easily overwrite variables and even ``remove()`` or ``append()`` items to existing lists.
Here's an example of a ``settings.py``:

.. code-block:: python

    from ansibleci.defaults import *

    BASEDIR = '/my/ansible/project/dir/'

    ENABLED_TESTS.remove('ansibleci.tests.readme.Readme')
    ENABLED_TESTS.append('yourcimodule.guidelines.Guidelines')