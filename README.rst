fluentcms-suit
==============

A collection of template overrides to get django-fluent-pages_ (including django-parler_) to play nice with django-suit_.

.. image:: https://img.shields.io/pypi/v/fluentcms-suit.svg
    :target: https://pypi.python.org/pypi/fluentcms-suit/

.. image:: https://img.shields.io/pypi/dm/fluentcms-suit.svg
    :target: https://pypi.python.org/pypi/fluentcms-suit/

.. image:: https://img.shields.io/github/license/bashu/fluentcms-suit.svg
    :target: https://pypi.python.org/pypi/fluentcms-suit/

Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: shell

    pip install fluentcms-suit

Backend Configuration
---------------------

First make sure the project is configured for django-fluent-pages_ and django-suit_.

Then add the following settings:

.. code-block:: python

    INSTALLED_APPS += (
        'fluentcms_suit',  # must be before `fluent*` apps and after `suit` app
    )

Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-suit: https://github.com/darklow/django-suit
.. _django-fluent-pages: https://github.com/edoburu/django-fluent-pages
.. _django-parler: https://github.com/darklow/django-parler
