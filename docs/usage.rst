Usage
=====

The usage of ``ansibleci`` is also quite simple.

Standalone
----------

To use ``ansibleci`` as a standalone tool to test your Ansible project you've to make sure you've `installed <installation.html>`_ it properly.

To test your Ansible project you've to run:

.. code-block:: bash

    ansibleci <ANSIBLE PROJECT BASEDIR>

If you've `installed the package via pip <installation.html#pypi-pip>`_ you should already have the ``ansibleci`` script located at ``/usr/local/bin/ansibleci``. 
Just make sure you've ``/usr/local/bin`` in your ``PATH`` environment variable or call it with the absolute path.

However, if you've installed it manually via `github release <installation.html#github-release>`_ or `git repository <installation.html#git-repository>`_ you've to run a slightly different command:

.. code-block:: bash

    bin/ansibleci <ANSIBLE PROJECT BASEDIR>

Please note that you might need to `configure <configuration.html>`_ ``ansibleci`` first.

Python module
-------------

Because ``ansibleci`` is a Python module by nature, it can be used within any of your existing Python scripts.

Have a look at the `API documentation <api.html>`_ and the `writing tests guide <writing-tests.html>`_.
You can also have a look at the `ansibleci <https://github.com/confirm/ansibleci/tree/develop/ansibleci>`_ module and read the **class and method descriptions**.

Here's an example how to use the ``ansibleci`` Python module in your own Python script:

.. code-block:: python

    from ansibleci.config import Config
    from ansibleci.runner import Runner
    import myapp.settings

    # Create a new ansibleci Config instance, which is used by the Runner.
    config = Config(load_defaults=True)

    # Add your own settings module to the Config instance.
    # Your own settings will overwrite the defaults.
    config.add_module(myapp.mysettings)

    # Manually set config parameters on the Config instance.
    config.BASEDIR = '/my/ansible/project/dir/'

    # Create a new runner instance and run the tests.
    Runner(config).run()

Of course you can also have a look at the existing `ansibleci script in the github repository <https://github.com/confirm/ansibleci/blob/develop/bin/ansibleci>`_.
