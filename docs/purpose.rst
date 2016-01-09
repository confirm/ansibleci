Purpose
=======

We've created ``ansibleci`` to run CI tests against an existing Ansible project before changes are merged into the active development tree.

Most of the time we're working with ``git`` and we make use of pull/merge requests in Git platforms like GitHub, GitLab or Stash.
When users sent pull/merge requests to merge their changes into the active development tree, someone had to check their commits in advance.
While some of the changes are quite complex to check automatically, we noticed that a lot of the issues we had with changes could easily be tested in a most automated way.

So we started a new CI project to test if the commited changes meet our guidelines. For example if every task is properly tagged or if there are existing Readme files for all roles.

Feel free to use this CI framework for your own standalone Ansible project, integrate it in your own Travis CI or Gitlab CI.
We try to provide some default tests which we're using every day. However, you can easily create new tests which meet your personal requirements.

Made with ♥ for the community.
