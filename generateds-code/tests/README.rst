============
Unit Tests
============

How to run the unit test
==========================

To run the unit tests, do::

    $ cd tests/         # this directory
    $ pytest-3 -vv .

If you need to sync the tests with code changes, do::

    $ ./generateDS_test.py
    $ ./copy_all
    $ (cd EnumImport && ./copy_enum_import.sh)

You will need to use Python 3 and not Python 2.7 to run the unit
tests.  The unit tests will run under Python 2.7, but the tests fail.
That's because of (1) differences in the comments at the
top of generated files; (2) some ordering differences, possibly
because of dicts; etc. all of which do not matter when you actually
run the generated code, I believe.
