Usage
=====

The usage of ``ansibleci`` is also quite simple.

Standalone
----------

To use ``ansibleci`` as a standalone tool to test your Ansible project you've to make sure you've installed it properly.

If you've installed it via `github release <installation.html#github-release>`_ or by `using the git repository <installation.html#git-repository>`_, then you should already have a version of the ``test.py`` Python script. Though, if you've installed it via ``pip`` you should obtain an initial `test.py version from our git repository <https://raw.githubusercontent.com/confirm/ansibleci/develop/test.py>`_.

We recommend you create a ``test/`` directory in the root directory of your Ansible project and put all the test files inside this directory. Then run:

.. code-block:: bash

    ./test.py

Please note that you might need to `configure <configuration.html>`_ ``ansibleci`` first.

Python module
-------------

Because ``ansibleci`` is a Python module by nature, it can be used within any of your existing Python scripts.

There's currently no API documentation available. However, you can easily have a look at the ``ansibleci`` module and read the **class and method descriptions**.

Here's an example how to use the ``ansibleci`` Python module in your script:

.. code-block:: python

    from ansibleci.config import Config
    from ansibleci.runner import Runner
    import myapp.settings

    # Create a new ansibleci Config instance, which is used by the Runner.
    config = Config(load*defaults=True)

    # Add your own settings module to the Config instance.
    # Your own settings will overwrite the defaults.
    config.add_module(myapp.mysettings)

    # Manually set config parameters on the Config instance.
    config.BASEDIR = '/my/ansible/project/dir/'

    # Create a new runner instance and run the tests.
    Runner(config).run()

Alternatively you can have a look at the `test.py script in the github repository <https://github.com/confirm/ansibleci/blob/develop/test.py>`_.