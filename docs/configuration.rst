Configuration
=============

Out of the box
--------------

``ansibleci`` can work out of the box if you meet the following requirements:

* the ``BASEDIR`` points to the root of your Ansible project
* your roles directory is called ``roles/`` and is located directly in the ``BASEDIR``

If you meet all the requirements above then ``ansibleci`` can work out of the box. However, you might want to configure your `custom settings <#custom-settings>`_.

Defaults
--------

``ansibleci`` is designed to be flexible and dynamic, therefor not everything is hard coded in tests.
To get an overview over all customisable settings you should have a look at the `defaults.py <https://github.com/confirm/ansibleci/blob/develop/ansibleci/defaults.py>`_.

**IMPORTANT:** Do not change the defaults because they're part of the core. Read the next chapter to customise the settings.

Custom settings
---------------

While the `defaults <#defaults>`_ are part of the core, you can easily overwrite them by creating a new Python file / module. Just run ``ansibleci`` with the ``--config my.python.module`` CLI argument and your module will automatically be loaded and evaluated.

Of course you've access to the full power of Python in your module, which means you can easily overwrite variables or even ``remove()`` or ``append()`` items to existing lists.
Here's an example of a ``settings.py`` located in your current working directory:

.. code-block:: python

    from ansibleci.defaults import *

    ENABLED_TESTS.remove('ansibleci.tests.readme.Readme')
    ENABLED_TESTS.append('yourcimodule.guidelines.Guidelines')

You should be able to run ``ansibleci`` with this ``settings.py`` module by executing:

.. code-block:: bash

    ansibleci --config=settings <ANSIBLE PROJECT BASEDIR>

Please note that ``settings.py`` is `ignored by the git repository <https://github.com/confirm/ansibleci/blob/develop/.gitignore>`_, so you can easily create a ``settings.py`` file without accidentally committing it.
