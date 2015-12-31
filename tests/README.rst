=====
Tests
=====

This directory is a Django project, with ``testapp`` is an example app that
contains the tests and support code.

You can run Nexus locally with a simple SQLite database setup with:

.. code-block:: bash

    PYTHONPATH=..:. django-admin.py runserver --settings=settings.dev

This automatically adds the username 'admin' with password 'password' so you
can login locally at ``/admin/`` and peruse nexus at ``/nexus/``. You can also
manipulate ``PYTHONPATH`` further to add other modules you might be testing,
e.g. if you have a ``gargoyle`` checkout in the same folder as ``nexus``, use:

.. code-block:: bash

    PYTHONPATH=../../gargoyle:..:. django-admin.py runserver --settings=settings.dev

You'll need to change ``settings/base.py`` to add it there too, plus any
dependencies must be available too.
