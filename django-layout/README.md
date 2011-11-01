Django @Ovid@ -- A Django project created by Django Layout.
===

Django @Ovid@ is...

## BUILD

This runs `python setup.py develop` (more or less).

    ./build.sh

    # Create the initial database.
    ./bin/django-migrate.sh
    ./bin/django-load.sh

    # Create a dummy SSL certificate.
    ./bin/make-ssl-cert.sh

    ./bin/lighttpd.sh start
    sensible-browser http://localhost:8080
    ./bin/lighttpd.sh stop

To use the admin site, run (only once):

    ./bin/django-manage.sh createsuperuser

Then, later on, each time a model changes run:

    ./bin/django-migrate.sh

## TEST

This uses `nosetests` to run the unit tests, and enables the built-in
coverage report.

    ./tests.sh
    sensible-browser ./coverage/index.html

## INSTALL

There is nothing to install.

## DEBUG

The layout used by Django @Ovid@ depends on that a particular
environment has been setup (see `etc/common`). For this reason several
wrapper scripts have been provided to help when working on the
command-line. For example:

    $ ./bin/python.sh
    >>>

## REQUIREMENTS

As tested on [Ubuntu 11.04](http://ubuntu.com/). See also [Ubuntu
Setup](https://github.com/software6/ubuntu-setup).

 * [python 2.7](http://www.python.org/)
 * [python-setuptools 0.6](http://packages.python.org/distribute/)
 * [python-nose 1.0](http://code.google.com/p/python-nose/)
 * [python-coverage 3.4](http://nedbatchelder.com/code/coverage/)
 * [python-django 1.3](http://www.djangoproject.com/)
 * [lighttpd 1.4](http://www.lighttpd.net/)
 * [python-flup 1.0](http://www.saddi.com/software/flup/)
 * [spawn-fcgi 1.6](http://redmine.lighttpd.net/projects/spawn-fcgi)
 * [sqlite3 3.7](http://www.sqlite.org/)
 * [ssl-cert 1.0](http://www.openssl.org/)
 * [jquery 1.5](http://www.jquery.com/)

## OPTIONAL

 * [pylint 0.23](http://www.logilab.org/project/pylint)

## CONTRIBUTE

TODO: https://github.com/.../django-@ovid@

## LICENSE

Django @Ovid@ is brought to you by TODO: Who? under the TODO: What?
License.

## CREATED BY

https://github.com/software6/django-layout
