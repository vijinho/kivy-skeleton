Skeleton
========

This app is a skeleton app for development in Python/Kivy.

It runs from Android version 2.2 and is available on Google Play at:

https://play.google.com/store/apps/details?id=com.urunu.skeleton

Features
--------
-

Setup
-----

-  ``$ pip install --editable .``
-  ``nosetests`` - run 'nose' tests in tests/

Manual Database Setup
~~~~~~~~~~~~~~~~~~~~~
If you wish to setup the database manually instead of automatically when the
application runs:

Command Line Usage
------------------

Type ``skeleton`` or failing that:

::

    $ python skeleton.py --help 

    Usage: skeleton [OPTIONS] COMMAND [ARGS]...

    Options:
      -v, --verbose
      -l, --logfile FILENAME
      --help                  Show this message and exit.

-  ``skeleton COMMAND --help``
-  ``sqlite3 data/aphorisms.db`` see http://www.sqlite.org/cli.html

Running the Kivy App
--------------------

-  On Mac OS X: ``kivy main.py`` - On other platforms it may 'just work'
   with ``python main.py``
-  Alternatively, run .

See Also
--------

-  https://travis-ci.org/vijinho/skeleton - Travis Build Test

This app is written in Python using the Kivy library for
cross-platform support (Android, IOS, Windows, Linux, Mac OSX). See
http://kivy.org/docs/guide/packaging.html for instructions on packaging
the application for the different platforms.

(c) Copyright 2014 Vijay Mahrra http://about.me/vijay.mahrra
