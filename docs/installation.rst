Installation
============

Installing ``ansibleci`` is quite simple and you've several ways to get it on your system.

PyPI / pip
----------

The most simple way to install ``ansibleci`` is by using ``pip`` - the Python package manager:

.. code-block:: bash

    pip install ansibleci

If you don't have direct internet access or ``pip`` on your system, you can easily download it directly from `PyPI <https://pypi.python.org/pypi/ansibleci>`_.

github release
--------------

To manually download a github release, browse to the `releases page <https://github.com/confirm/ansibleci/releases>`_ and fetch a ``.zip`` or ``.tar.gz`` file.
Unpack the file on your system and you're ready to go.

git repository
--------------

Alternatively you can use the `git repository <https://github.com/confirm/ansibleci>`_ directly, so you're always up-to-date with the latest changes.

Clone the repository:


.. code-block:: bash

    git clone https://github.com/confirm/ansibleci.git
    cd ansibleci/

You can switch between branches and versions by executing:

.. code-block:: bash

    git checkout BRANCH|TAG

Please note that we're using `Vincent Driessen's gitflow model <http://nvie.com/posts/a-successful-git-branching-model/>`_, which means:

* the ``develop`` branch is always our **bleeding edge development branch**
* the ``master`` branch is always our **latest stable branch**
* ``release-*`` branches are **only temporary** and will be removed once the release is tagged
* we're using **tags** (aka ``vMAJOR.MINOR.BUGFIX``) to create new **releases**
